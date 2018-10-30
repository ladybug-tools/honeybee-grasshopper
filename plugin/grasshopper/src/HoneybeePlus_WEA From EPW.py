# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Create a WEA object from an EPW.

-

    Args:
        _epw_file = Fullpath to epw weather file.
        timestep_: An integer representing the timestep with which to make the 
            WEA object.  Default is set to 1 for 1 step per hour of the year.
    Returns:
        wea: A wea object from epw file.
"""

ghenv.Component.Name = "HoneybeePlus_WEA From EPW"
ghenv.Component.NickName = 'WEA'
ghenv.Component.Message = 'VER 0.0.05\nOCT_22_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '02 :: Daylight :: Light Sources'
ghenv.Component.AdditionalHelpFromDocStrings = "3"

try:
    from ladybug.wea import Wea
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))

if _epw_file:
    timestep_ = 1 if timestep_ is None else timestep_
    wea = Wea.from_epw_file(_epw_file, timestep_)