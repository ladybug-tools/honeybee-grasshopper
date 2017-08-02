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
    Returns:
        readMe!: Reports, errors, warnings, etc.
        wea: A wea object from epw file.
"""

ghenv.Component.Name = "HoneybeePlus_Wea"
ghenv.Component.NickName = 'Wea'
ghenv.Component.Message = 'VER 0.0.03\nAUG_04_2017'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '02 :: Daylight :: Light Sources'
ghenv.Component.AdditionalHelpFromDocStrings = "3"

try:
    from ladybug.wea import Wea
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))

if _epwFile:
    wea = Wea.fromEpwFile(_epwFile)