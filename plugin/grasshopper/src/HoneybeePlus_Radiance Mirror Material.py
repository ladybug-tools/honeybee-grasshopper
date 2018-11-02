# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Radiance Mirror Material from Single Reflectance Value

-

    Args:
        _name: Material name
        _reflect_: Mirror reflectance as a number between 0 and 1.
    Returns:
        material: Radiance mirror material
"""

ghenv.Component.Name = "HoneybeePlus_Radiance Mirror Material"
ghenv.Component.NickName = 'radMirrorMat'
ghenv.Component.Message = 'VER 0.0.05\nOCT_22_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '01 :: Daylight :: Materials'
ghenv.Component.AdditionalHelpFromDocStrings = "0"

try:
    from honeybee.radiance.material.mirror import Mirror
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))

if _name:
    _reflect_ = 0.35 if _reflect_ is None else _reflect_
    material = Mirror.by_single_reflect_value(_name, _reflect_)