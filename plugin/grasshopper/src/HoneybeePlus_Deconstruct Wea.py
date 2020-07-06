# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Deconstruct a Wea object into lists of direct, diffuse, and golbal irradiance
at each timestep of the file.

-

    Args:
        _wea = A Honeybee WEA object.
    Returns:
        readMe!: Reports, errors, warnings, etc.
        dir: A list of direct normal irradiance values at each timestep of the WEA.
        diff: A list of diffuse sky solar irradiance values at each timestep of the WEA.
        glob: A list of global horizontal irradiance values at each timestep of the WEA.
"""

ghenv.Component.Name = "HoneybeePlus_Deconstruct Wea"
ghenv.Component.NickName = 'decnstrWea'
ghenv.Component.Message = 'VER 0.0.06\nJUL_07_2020'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '02 :: Daylight :: Light Sources'
ghenv.Component.AdditionalHelpFromDocStrings = "0"

if _wea is not None and hasattr(_wea, 'isWea'):
    dir = _wea.direct_normal_irradiance
    diff = _wea.diffuse_horizontal_irradiance
    glob = _wea.global_horizontal_irradiance