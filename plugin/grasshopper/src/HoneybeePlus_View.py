# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Honeybee View.

-

    Args:
        _name: View name.
        _v_location: Set the view point (-vp) to (x, y, z). This is the focal
            point of a perspective view or the center of a parallel projection.
            Default: (0, 0, 0)
        _v_direction: Set the view direction (-vd) vector to (x, y, z). The
            length of this vector indicates the focal distance as needed by
            the pixle depth of field (-pd) in rpict. Default: (0, 0, 1)
        _v_up_vector_: Set the view up (-vu) vector (vertical direction) to (x, y, z).
            Default: (0, 1, 0)
        _view_type_: Set view type (-vt) to one of the choices below.
                0 Perspective (v)
                1 Hemispherical fisheye (h)
                2 Parallel (l)
                3 Cylindrical panorma (c)
                4 Angular fisheye (a)
                5 Planisphere [stereographic] projection (s)
            For more detailed description about view types check rpict manual
            page: (http://radsite.lbl.gov/radiance/man_html/rpict.1.html)
        _h_view_angle_: Set the view horizontal size (-vs). For a perspective
            projection (including fisheye views), val is the horizontal field
            of view (in degrees). For a parallel projection, val is the view
            width in world coordinates.
        _v_view_angle_: Set the view vertical size (-vv). For a perspective
            projection (including fisheye views), val is the horizontal field
            of view (in degrees). For a parallel projection, val is the view
            width in world coordinates.
        _x_resolution_: Set the maximum x resolution (-x) to an integer.
        _y_resolution_: Set the maximum y resolution (-y) to an integer.
        
    Returns:
        view: Use this to create a view based analysis.
"""

ghenv.Component.Name = "HoneybeePlus_View"
ghenv.Component.NickName = 'view'
ghenv.Component.Message = 'VER 0.0.05\nOCT_22_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '00 :: Create'
ghenv.Component.AdditionalHelpFromDocStrings = "3"

try:
    from honeybee.radiance.view import View
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))


if _v_location and _v_direction:
    _location = (_v_location.X, _v_location.Y, _v_location.Z)
    _direction = (_v_direction.X, _v_direction.Y, _v_direction.Z)
    _up_vector = (_v_up_vector_.X, _v_up_vector_.Y, _v_up_vector_.Z)
    view = View(_name, _location, _direction, _up_vector, _view_type_,
                _h_view_angle_, _v_view_angle_, _x_resolution_, _y_resolution_)