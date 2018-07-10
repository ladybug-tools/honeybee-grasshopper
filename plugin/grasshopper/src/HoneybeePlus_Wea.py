# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
epw2wea

-

    Args:
        _epwFile = Fullpath to epw weather file.
        timestep_: An integer representing the timestep with which to make the 
            WEA object.  Default is set to 1 for 1 step per hour of the year.
    Returns:
        readMe!: Reports, errors, warnings, etc.
        wea: A wea object from epw file.
"""

ghenv.Component.Name = "HoneybeePlus_Wea"
ghenv.Component.NickName = 'Wea'
ghenv.Component.Message = 'VER 0.0.04\nJUL_10_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '02 :: Daylight :: Light Sources'
ghenv.Component.AdditionalHelpFromDocStrings = "3"

try:
    from ladybug.wea import Wea
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))

if _epwFile:
    if timestep_ == None:
        timestep_ = 1
    wea = Wea.from_epw_file(_epwFile, timestep_)