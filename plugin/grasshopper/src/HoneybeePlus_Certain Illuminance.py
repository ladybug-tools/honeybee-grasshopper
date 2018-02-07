# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Sky with certain illuminance.

    Args:
        _value: Desired value for sky horizontal illuminance in lux
            (default: 10000).
    Returns:
        sky: Honeybee sky. You can use this sky to create a grid-based daylight
            recipe.

"""

ghenv.Component.Name = "HoneybeePlus_Certain Illuminance"
ghenv.Component.NickName = 'certainIllum'
ghenv.Component.Message = 'VER 0.0.04\nFEB_07_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '02 :: Daylight :: Light Sources'
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from honeybee.radiance.sky.certainIlluminance import CertainIlluminanceLevel
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))

_value_ = _value_ or 10000
sky = CertainIlluminanceLevel(_value_)
