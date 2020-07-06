# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
A sky vector representing sky conditions at a single hour of the year.

-

    Args:
        north_: An angle in degrees between 0-360 to indicate north direction
            (Default: 0).
        _wea: Ladybug WEA object.
        _density_: A positive intger for sky density. [1] Tregenza Sky,
            [2] Reinhart Sky, etc. (Default: 1)
        _month_: A number to indicate month (1..12) (default: 6).
        _day_: A number to indicate day (1..31) (default: 21).
        _hour_: A number to indicate hour (0..23) (default: 12).
    Returns:
        sky_vec: Sky vector for multi-phase daylight analysis.
"""

ghenv.Component.Name = "HoneybeePlus_Sky Vector"
ghenv.Component.NickName = 'skyVector'
ghenv.Component.Message = 'VER 0.0.06\nJUL_07_2020'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '02 :: Daylight :: Light Sources'
ghenv.Component.AdditionalHelpFromDocStrings = "2"

try:
    from honeybee_plus.radiance.sky.skymatrix import SkyMatrix
    from ladybug.dt import DateTime
except ImportError as e:
    raise ImportError('\nFailed to import honeybee_plus:\n\t{}'.format(e))
        
    raise ImportError('{}\n\t{}'.format(msg, e))

if _wea:
    north_ = 0 if north_ is None else north_
    _month_ = 6 if _month_ is None else _month_
    _day_ = 21 if _day_ is None else _day_
    _hour_ = 12 if _hour_ is None else _hour_
    dt = DateTime(_month_, _day_, _hour_)
    _density_ = _density_ or 1

    sky_vec = SkyMatrix(_wea, _density_, north_, (int(dt.hoy),),
                       suffix=str(int(dt.hoy)))
