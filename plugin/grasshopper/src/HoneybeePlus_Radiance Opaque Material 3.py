# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Radiance Opaque Material from Single Reflectance Value

-

    Args:
        _name: Material name
        _r_ref_: Diffuse reflectance for red channel
        _g_ref_: Diffuse reflectance for green channel
        _b_ref_: Diffuse reflectance for blue channel
        _spec_: Fraction of reflected light that is specular. The reflected specularity
            of common uncoated glass is around .06, Matte = suggested min 0,
            Satin = suggested max 0.07 (Default: 0). Specularity fractions
            greater than 0.1 are not realistic (Default: 0).
        _rough_:  Roughness is specified as the rms slope of surface facets.
            A value of 0 corresponds to a perfectly smooth surface, and a 
            value of 1 would be a very rough surface. Roughness values 
            greater than 0.2 are not very realistic. (Default: 0).
    Returns:
        material: Radiance opaque material
"""

ghenv.Component.Name = "HoneybeePlus_Radiance Opaque Material 3"
ghenv.Component.NickName = 'radOpaqueMat3'
ghenv.Component.Message = 'VER 0.0.05\nOCT_22_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '01 :: Daylight :: Materials'
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from honeybee.radiance.material.plastic import Plastic
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))

if _name:
    r_reflectance = 0 if _r_ref_ is None else _r_ref_
    g_reflectance = 0 if _g_ref_ is None else _g_ref_
    b_reflectance = 0 if _b_ref_ is None else _b_ref_
    material = Plastic(_name, _r_ref_, _g_ref_, _b_ref_, _spec_, _rough_)