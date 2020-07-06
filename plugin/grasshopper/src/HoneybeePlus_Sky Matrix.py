# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
A sky matrix representing sky conditions over multiple hours of the year.

-

    Args:
        name_: An optional suffix for sky name. The suffix will be added at the
            end of the standard name. Use this input to customize the new and
            avoid sky being overwritten by other skymatrix components.
        north_: An angle in degrees between 0-360 to indicate north direction
            (Default: 0).
        _wea: Ladybug WEA object.
        _density_: A positive intger for sky density. [1] Tregenza Sky,
            [2] Reinhart Sky, etc. (Default: 1)
        hoys_: Optional list of hours for generating the sky matrix (Default: 0...8759)
    Returns:
        skymtx: Sky matrix for multi-phase daylight analysis.
"""

ghenv.Component.Name = "HoneybeePlus_Sky Matrix"
ghenv.Component.NickName = 'skyMatrix'
ghenv.Component.Message = 'VER 0.0.06\nJUL_07_2020'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '02 :: Daylight :: Light Sources'
ghenv.Component.AdditionalHelpFromDocStrings = "2"

try:
    from honeybee_plus.radiance.sky.skymatrix import SkyMatrix
except ImportError as e:
    raise ImportError('\nFailed to import honeybee_plus:\n\t{}'.format(e))


if _wea:
    skymtx = SkyMatrix(_wea, _density_, north_, hoys_, suffix=name_)