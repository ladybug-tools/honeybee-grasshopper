# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Honeybee Window Group

A window group is a group of HBWindow surfaces which will be grouped together
for 3-phase daylight analysis. View matrix will be calculated for all the Window
surfaces in a group once. Window surfaces in a group shoudl have the same normal
direction, and same BSDF materials will be assigned to all the windows in this
group.
-

    Args:
        _geo: A list of input geometry.
        name_: A name for this surface. If the name is not provided Honeybee will
            assign a random name to the surface.
        rad_mat_: A Radiance material. If radiance matrial is not provided the
            component will use the type to assign the default material 
            (%60 transmittance)for the surface.
        ep_prop_: EnergyPlus properties.
    Returns:
        report: Reports, errors, warnings, etc.
        HBWinSrf: Honeybee window surface. Use this surface directly for daylight
            simulation or add it to a honeybee surface or a honeybee zone for
            energy simulation.
"""

ghenv.Component.Name = "HoneybeePlus_Honeybee Window Group"
ghenv.Component.NickName = 'HBWinGroup'
ghenv.Component.Message = 'VER 0.0.06\nJUL_07_2020'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '00 :: Create'
ghenv.Component.AdditionalHelpFromDocStrings = "1"


try:
    from honeybee_plus.hbdynamicsurface import HBDynamicSurface
    from honeybee_plus.radiance.properties import RadianceProperties
except ImportError as e:
    raise ImportError('\nFailed to import honeybee_plus:\n\t{}'.format(e))

if _name and len(_geo)!=0 and _geo[0]!=None:

    if rad_mat_:
        assert not rad_mat_.is_opaque, \
            TypeError('Radiance material must be a Window material not {}.'.format(type(m)))
        rad_prop_ = RadianceProperties(rad_mat_)
    else:
        rad_prop_ = RadianceProperties()

    ep_prop_ = None
    _type_ = 5  # in the interface we use dynamic surfaces only for fenestration
    is_type_set_by_user = True
    is_name_set_by_user = True
    
    HB_win_group = HBDynamicSurface.from_geometry(
        _name, _geo, _type_, is_name_set_by_user, is_type_set_by_user, rad_prop_,
        ep_prop_, states_, group=True)
