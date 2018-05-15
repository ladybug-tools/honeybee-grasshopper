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
        _reflect_: Diffuse reflectance
        _spec_: Specularity values above 0.1 are uncommon
        _rough_: Roughness values above 0.2 are uncommon
    Returns:
        readMe!: Reports, errors, warnings, etc.
        material: Radiance opaque material
"""

ghenv.Component.Name = "HoneybeePlus_Radiance Opaque Material"
ghenv.Component.NickName = 'radOpaqueMaterial'
ghenv.Component.Message = 'VER 0.0.05\nMAR_14_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '01 :: Daylight :: Materials'
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from honeybee.radiance.material.plastic import Plastic
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))

if _name:
    _reflect_ = _reflect_ or 0.35
    material = Plastic.by_single_reflect_value(
        _name, _reflect_, _spec_, _rough_)