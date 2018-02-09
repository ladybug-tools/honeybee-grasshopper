"""Collection of methods for Honeybee geometry operations in Grasshopper."""
from collections import namedtuple

try:
    import Rhino as rc
except ImportError as e:
    pass


# ------------------------- Required functions -----------------------------------------
#  In order to create a plus library you must overwrite these three methods.
#  The structure of arguments and returns should stay the same.
# --------------------------------------------------------------------------------------
# TODO(someone!): Implement triangulate
def extract_geometry_points(geometries, meshing_parameters=None):
    """Calculate list of points for a Grasshopper geometry.

    For planar surfaces the length of the list will be only 1. For non-planar
    surfaces or surfaces with internal edges it will be a number of lists.

    Args:
        geometries: List of meshes or Breps
        meshing_parameters: Optional Rhino meshing_parameters. This will only be used if
            the surface is non-planar or has an internal edge and needs to be meshed.
            Default:
                Rhino.Geometry.meshing_parameters.Coarse; SimplePlanes = True for planar
                surfaces; Rhino.Geometry.meshing_parameters.Smooth for non-planar
                surfaces
    Returns:
        A Collection of (geometry, points) in which each geometry is coupled by points.
        For planar surfaces the length of the points list will be only 1. For
        non-planar surfaces, meshes or surfaces with internal edges it will be multiple
        lists.
    """
    if not hasattr(geometries, '__iter__'):
        geometries = (geometries,)

    for geometry in geometries:

        if isinstance(geometry, rc.Geometry.Mesh):
            yield extract_mesh_points((geometry,))
        elif isinstance(geometry, rc.Geometry.Brep):
            yield extract_brep_points(geometry, meshing_parameters)
        else:
            raise TypeError(
                'Input surface should be a Mesh or a Brep not {}.'.format(type(geometry))
            )


def xyz_to_geometrical_points(xyz_points):
    """convert a sequence of (x, y, z) values to Grasshopper points.

    Input should be list of lists of points.
    """
    for xyz_list in xyz_points:
        for xyz in xyz_list:
            yield rc.Geometry.Point3d(xyz[0], xyz[1], xyz[2])


def polygon(point_list):
    """Return a polygon from points."""
    return rc.Geometry.Polyline(point_list).ToNurbsCurve()


# ------------------------- End of honeybee[+] methods -----------------------------
# ------------------------------ Utilities -----------------------------------------
def is_planar(geometry, tol=1e-3):
    """Check if a surface in planar."""
    return geometry.Faces[0].is_planar(tol)


def extract_brep_points(brep, meshing_parameters=None, tol=1e-3):
    """Extract points from Brep."""
    meshing_parameters = meshing_parameters or rc.Geometry.meshing_parameters.Coarse
    for fid in xrange(brep.Faces.Count):
        geometry = brep.Faces[fid].DuplicateFace(False)
        if not brep.Faces[fid].is_planar(tol):
            meshes = rc.Geometry.Mesh.CreateFromBrep(geometry, meshing_parameters)
            yield next(extract_mesh_points(meshes))
        else:
            # planar surface
            pts = geometry.DuplicateVertices()
            # sort points anti clockwise
            # this is only important for energy simulation and won't make a difference
            # for Radiance

            # To sort the points we find border of the surface and evaluate points
            # on border and use the parameter value to sort them
            border = rc.Geometry.Curve.JoinCurves(geometry.DuplicateEdgeCurves(True))

            if len(border) > 1:
                # mesh the surface
                meshing_parameters.SimplePlanes = True
                meshes = rc.Geometry.Mesh.CreateFromBrep(geometry, meshing_parameters)
                yield next(extract_mesh_points(meshes))
            else:
                # In some strange cases Rhino returns a single point for the surface
                if len(pts) == 1:
                    pts = (p.Location for p in border[0].Points)

                points_sorted = sorted(pts, key=lambda pt: border[0].ClosestPoint(pt)[1])
                # make sure points are anti clockwise
                if not is_points_sorted_anticlockwise(
                        points_sorted,
                        get_surface_center_pt_and_normal(geometry).normal_vector):
                    points_sorted.reverse()
                # return sorted points
                # Wrap in a list as Honeybee accepts list of list of points
                yield geometry, (points_sorted,)


def extract_mesh_points(meshes):
    """Extract points from a mesh."""
    for mesh in meshes:
        yield mesh, tuple(
            tuple(mesh.Vertices[face[i]] for i in range(4))
            if face.IsQuad else
            tuple(mesh.Vertices[face[i]] for i in range(3))
            for face in mesh.Faces
        )


def vectors_cross_product(vector1, vector2):
    """Calculate cross product of two vectors."""
    return vector1.X * vector2.X + \
        vector1.Y * vector2.Y + vector1.Z * vector2.Z


def is_points_sorted_anticlockwise(sorted_points, normal):
    """Check if an ordered list of points are anti-clockwise."""
    vector0 = rc.Geometry.Vector3d(sorted_points[1] - sorted_points[0])
    vector1 = rc.Geometry.Vector3d(sorted_points[-1] - sorted_points[0])
    pts_normal = rc.Geometry.Vector3d.CrossProduct(vector0, vector1)

    # in case points are anti-clockwise then normals should be parallel
    if vectors_cross_product(pts_normal, normal) > 0:
        return True
    else:
        return False


def get_surface_center_pt_and_normal(geometry):
    """Calculate center point and normal for a hb_surface.

    Args:
        hb_surface: A Honeybee surface

    Returns:
        Returns a tuple as (center_pt, normal_vector)
    """
    brep_face = geometry.Faces[0]
    if brep_face.is_planar and brep_face.IsSurface:
        u_domain = brep_face.Domain(0)
        v_domain = brep_face.Domain(1)
        center_u = (u_domain.Min + u_domain.Max) / 2
        center_v = (v_domain.Min + v_domain.Max) / 2

        center_pt = brep_face.PointAt(center_u, center_v)
        normal_vector = brep_face.NormalAt(center_u, center_v)
    else:
        centroid = rc.Geometry.AreaMassProperties.Compute(brep_face).Centroid
        uv = brep_face.ClosestPoint(centroid)
        center_pt = brep_face.PointAt(uv[1], uv[2])
        normal_vector = brep_face.NormalAt(uv[1], uv[2])

    SurfaceData = namedtuple('SurfaceData', 'center_pt normal_vector')

    return SurfaceData(center_pt, normal_vector)


def check_planarity(hb_surface, tolerance=1e-3):
    """Check planarity of a hb_surface.

    Args:
        hb_surface: A Honeybee surface
        tolerance: A float number as tolerance (Default: 1e-3)

    Returns:
        True is the surface is planar, otherwise return False.
    """
    try:
        return hb_surface.geometry.Faces[0].is_planar(tolerance)
    except AttributeError as e:
        raise TypeError("Input is not a hb_surface: %s" % str(e))


def check_for_internal_edge(hb_surface):
    """Check if the surface has an internal edge.

    For surfaces with internal edge surfaces needs to be meshed to extract the points.

    Args:
        hb_surface: A Honeybee surface

    Returns:
        True is the surface has an internal edge, otherwise return False.

    """
    # I believe there should be a direct method in RhinoCommon to indicate if a
    # surface is an open brep but since I couldn't find it I'm using this method
    # if Surface has no intenal edges the length of joined border is 1
    try:
        edges = hb_surface.geometry.DuplicateEdgeCurves(True)
    except AttributeError as e:
        raise TypeError("Input is not a hb_surface: %s" % str(e))
    else:
        border = rc.Geometry.Curve.JoinCurves(edges)
        if len(border) > 1:
            return True
        else:
            return False
