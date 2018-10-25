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
        _wea = A Honeybee WEA object.
    Returns:
        readMe!: Reports, errors, warnings, etc.
        dir: A list of direct normal radiation values at each timestep of the WEA.
        diff: A list of diffuse sky solar radiation values at each timestep of the WEA.
        glob: A list of global horizontal radiation values at each timestep of the WEA.
"""

ghenv.Component.Name = "HoneybeePlus_Deconstruct Wea"
ghenv.Component.NickName = 'decnstrWea'
ghenv.Component.Message = 'VER 0.0.05\nOCT_22_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '02 :: Daylight :: Light Sources'
ghenv.Component.AdditionalHelpFromDocStrings = "0"

if _wea is not None and hasattr(_wea, 'isWea'):
    dir = _wea.direct_normal_radiation
    diff = _wea.diffuse_horizontal_radiation
    glob = _wea.global_horizontal_radiation