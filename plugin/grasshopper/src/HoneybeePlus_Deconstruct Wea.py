# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Deconstruct a Wea object into lists of direct, diffuse, and golbal radiation
at each timestep of the file.

-

    Args:
        _wea = A Honeybeeplus WEA object.
    Returns:
        readMe!: Reports, errors, warnings, etc.
        dir: A list of direct normal radiation at each timestep of the WEA.
         diff: A list of diffuse sky solar radiation at each timestep of the WEA.
         srfRef: A list of ground reflected solar radiation at each timestep of the WEA.
"""

ghenv.Component.Name = "HoneybeePlus_Deconstruct Wea"
ghenv.Component.NickName = 'DecnstrWea'
ghenv.Component.Message = 'VER 0.0.04\nJUN_05_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '02 :: Daylight :: Light Sources'
ghenv.Component.AdditionalHelpFromDocStrings = "0"

if _wea is not None and hasattr(_wea, 'isWea'):
    globH = _wea.get_global_horizontal_radiation()
    
    dir = [float(x) for x in _wea.direct_normal_radiation]
    diff = [float(x) for x in _wea.diffuse_horizontal_radiation]
    glob = [float(x) for x in globH]