# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Honeybee Window Surface

-

    Args:
        _geo: A list of input geometry.
        names_: A name or a list of names for input geometry. If the name is not
            provided Honeybee will assign a random name to the surface.
        rad_mat_: A Radiance material. If radiance matrial is not provided the
            component will use the type to assign the default material 
            (%60 transmittance)for the surface.
        ep_prop_: EnergyPlus properties.
    Returns:
        report: Reports, errors, warnings, etc.
        HB_win_srf: Honeybee window surface. Use this surface directly for daylight
            simulation or add it to a honeybee surface or a honeybee zone for
            energy simulation.
"""

ghenv.Component.Name = "HoneybeePlus_Honeybee Window Surface"
ghenv.Component.NickName = 'HBWinSrf'
ghenv.Component.Message = 'VER 0.0.05\nOCT_22_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '00 :: Create'
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from honeybee.hbfensurface import HBFenSurface
    from honeybee.radiance.properties import RadianceProperties
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))

if len(_geo)!=0 and _geo[0]!=None:
    is_name_set_by_user = False
    if names_:
        is_name_set_by_user = True

    if rad_mat_:
        assert not rad_mat_.is_opaque, \
            TypeError('Radiance material must be a Window material not {}.'.format(type(m)))
        rad_prop_ = RadianceProperties(rad_mat_)
    else:
        rad_prop_ = RadianceProperties()

    ep_prop_ = None
    HB_win_srf = HBFenSurface.from_geometry(names_, _geo, is_name_set_by_user, rad_prop_, ep_prop_)