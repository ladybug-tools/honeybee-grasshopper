# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
A uniform sky with certain illuminance.

    Args:
        _value: Desired value for sky horizontal illuminance in lux
            (default: 10000).
    Returns:
        sky: Honeybee sky. You can use this sky to create a point-in-time
            daylight recipe.

"""

ghenv.Component.Name = "HoneybeePlus_Certain Illuminance"
ghenv.Component.NickName = 'certainIllum'
ghenv.Component.Message = 'VER 0.0.06\nJUL_07_2020'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '02 :: Daylight :: Light Sources'
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from honeybee_plus.radiance.sky.certainIlluminance import CertainIlluminanceLevel
except ImportError as e:
    raise ImportError('\nFailed to import honeybee_plus:\n\t{}'.format(e))

_value_ = 10000 if _value_ is None else _value_
sky = CertainIlluminanceLevel(_value_)
