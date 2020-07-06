# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
A point-in-time custom sky.

    Args:
        north_: A number between 0 and 360 that represents the degrees off from
            the y-axis to make North. The default North direction is set to the
            Y-axis (default: 0 degrees).
        _location: A Ladybug location.
        _dir_rad: Direct radiation in W/m2.
        _dif_rad:  Diffuse radiation in W/m2.
        _month_: Input a number to indicate month (1..12) (default: 6).
        _day_: Input a number to indicate day (1..31) (default: 21).
        _hour_: Input a number to indicate hour (0..23) (default: 12).
    Returns:
        sky: Honeybee sky. You can use this sky to create a point-in-time
            daylight recipe.

"""

ghenv.Component.Name = "HoneybeePlus_Custom Sky"
ghenv.Component.NickName = 'customSky'
ghenv.Component.Message = 'VER 0.0.06\nJUL_07_2020'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '02 :: Daylight :: Light Sources'
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from honeybee_plus.radiance.sky.climatebased import ClimateBased
    from ladybug.location import Location
except ImportError as e:
    raise ImportError('\nFailed to import honeybee_plus:\n\t{}'.format(e))

if _location and _dir_rad is not None and _dif_rad is not None:
    if not hasattr(_location, 'isLocation'):
        _location = Location.fromLocation(_location)
    
    # set default values if they are not set
    north_ = 0 if north_ is None else north_
    _month_ = 6 if _month_ is None else _month_
    _day_ = 21 if _day_ is None else _day_
    _hour_ = 12 if _hour_ is None else _hour_
    sky = ClimateBased(_location, _month_, _day_, _hour_, _dir_rad, _dif_rad, north_)