# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Honeybee Surface

-

    Args:
        _geo: A list of input geometries.
        names_: A name or a list of names for input geometry. If the name is not
            provided Honeybee will assign a random name to the surface.
        _type_: Surface type. Surface type will be used to set the material and
            construction for the surface if they are not assigned by user.
            0   Wall           0.5 UndergroundWall
            1   Roof           1.5 UndergroundCeiling
            2   Floor          2.25 UndergroundSlab
            2.5 SlabOnGrade    2.75 ExposedFloor
            3   Ceiling        4   AirWall
            5   Window         6   Context
        rad_mat_: Radiance material. If radiance matrial is not provided the component
            will use the type to assign the default material for the surface. If type
            is also not assigned by user. Honeybee will guess the type of the surface
            based on surface normal vector direction at the center of the surface.
        ep_prop_: EnergyPlus properties. If EnergyPlus properties is not provided the
            component will use the "type" to assign the EnergyPlus properties for this
            surface. If type is also not assigned by user Honeybee will guess the type
            of the surface based on surface normal vector direction at the center of
            the surface, and sets EnergyPlus properties based on the type.
        
    Returns:
        report: Reports, errors, warnings, etc.
        HB_srf: Honeybee surface. Use this surface directly for daylight simulation
            or to create a Honeybee zone for Energy analysis.
"""

ghenv.Component.Name = "HoneybeePlus_Honeybee Surface"
ghenv.Component.NickName = 'HBSurface'
ghenv.Component.Message = 'VER 0.0.06\nJUL_07_2020'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '00 :: Create'
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from honeybee_plus.hbsurface import HBSurface
    from honeybee_plus.radiance.properties import RadianceProperties
except ImportError as e:
    raise ImportError('\nFailed to import honeybee_plus:\n\t{}'.format(e))


if len(_geo)!=0 and _geo[0]!=None:
    is_name_set_by_user = False
    if names_:
        is_name_set_by_user = True
        
    is_type_set_by_user = True
    if not _type_:
        is_type_set_by_user = False
    
    radProp_ = RadianceProperties(rad_mat_) if rad_mat_ else RadianceProperties()
    
    ep_prop_ = None
    
    HB_srf = HBSurface.from_geometry(names_, _geo, _type_, is_name_set_by_user,
                                    is_type_set_by_user, radProp_, ep_prop_)
