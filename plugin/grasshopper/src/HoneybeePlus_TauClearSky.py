# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Convert a stat file into a WEA file with an ASHRAE Clear Sky.

-

    Args:
        _statFile = Fullpath to stat file (typically next to the epw file).
    Returns:
        readMe!: Reports, errors, warnings, etc.
        wea: A wea object from stat file. This wea object represents an ASHRAE Revised 
            Clear Sky ("Tau Model"), which is intended to determine peak solar load 
            and sizing parmeters for HVAC systems. The "Tau Model" uses monthly 
            optical depths found within a .stat file.
"""

ghenv.Component.Name = "HoneybeePlus_TauClearSky"
ghenv.Component.NickName = 'TauClearSky'
ghenv.Component.Message = 'VER 0.0.04\nMAY_13_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '02 :: Daylight :: Light Sources'
ghenv.Component.AdditionalHelpFromDocStrings = "3"

try:
    from ladybug.wea import Wea
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))

if _statFile:
    wea = Wea.from_stat_file(_statFile)