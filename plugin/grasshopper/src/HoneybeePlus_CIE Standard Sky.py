# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
A point-in-time standard Radiance CIE sky.

    Args:
        north_: A number between 0 and 360 that represents the degrees off from
            the y-axis to make North. The default North direction is set to the
            Y-axis (default: 0 degrees).
        _location: A Ladybug location.
        _month_: Input a number to indicate month (1..12) (default: 6).
        _day_: Input a number to indicate day (1..31) (default: 21).
        _hour_: Input a number to indicate hour (0..23) (default: 12).
        _type_: An integer between 0..5 to indicate CIE Sky Type (default: 0).
            [0] Sunny with sun, [1] sunny without sun, [2] intermediate with sun
            [3] intermediate without sun, [4] cloudy sky, [5] uniform sky (default: 0)
    Returns:
        sky: Honeybee sky. You can use this sky to create a point-in-time
            daylight recipe.

"""

ghenv.Component.Name = "HoneybeePlus_CIE Standard Sky"
ghenv.Component.NickName = 'CIESky'
ghenv.Component.Message = 'VER 0.0.05\nOCT_22_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '02 :: Daylight :: Light Sources'
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from honeybee.radiance.sky.cie import CIE
    from ladybug.location import Location
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))

if _location:
    if not hasattr(_location, 'isLocation'):
        _location = Location.from_location(_location)
    # set default values if they are not set
    north_ = 0 if north_ is None else north_
    _type_ = 0 if _type_ is None else _type_
    _month_ = 6 if _month_ is None else _month_
    _day_ = 21 if _day_ is None else _day_
    _hour_ = 12 if _hour_ is None else _hour_
    sky = CIE(_location, _month_, _day_, _hour_, north_, _type_)
