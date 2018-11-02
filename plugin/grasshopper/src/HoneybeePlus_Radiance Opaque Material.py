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
        _name: Material name as a text string.
        _reflect_: Diffuse reflectance as a number between 0 and 1.
        _spec_: Fraction of reflected light that is specular. The reflected specularity
            of common uncoated glass is around .06, Matte = suggested min 0,
            Satin = suggested max 0.07 (Default: 0). Specularity fractions
            greater than 0.1 are not realistic (Default: 0).
        _rough_: Roughness is specified as the rms slope of surface facets.
            A value of 0 corresponds to a perfectly smooth surface, and a 
            value of 1 would be a very rough surface. Roughness values 
            greater than 0.2 are not very realistic. (Default: 0).
    Returns:
        material: Radiance opaque material
"""

ghenv.Component.Name = "HoneybeePlus_Radiance Opaque Material"
ghenv.Component.NickName = 'radOpaqueMat'
ghenv.Component.Message = 'VER 0.0.05\nOCT_22_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '01 :: Daylight :: Materials'
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from honeybee.radiance.material.plastic import Plastic
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))

if _name:
    _reflect_ = 0.35 if _reflect_ is None else _reflect_
    material = Plastic.by_single_reflect_value(
        _name, _reflect_, _spec_, _rough_)