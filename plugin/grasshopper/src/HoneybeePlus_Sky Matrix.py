# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Sky Matrix.

-

    Args:
        north_: An angle in degrees between 0-360 to indicate north direction
            (Default: 0).
        _wea: Ladybug Wea object.
        _skyDensity_: A positive intger for sky density. [1] Tregenza Sky,
            [2] Reinhart Sky, etc. (Default: 1)
        hoys_: Optional list of hours for generating the sky matrix (Default: 0..8759)
    Returns:
        readMe!: Reports, errors, warnings, etc.
        skyMTX: Sky matrix for multi-phase daylight analysis.
"""

ghenv.Component.Name = "HoneybeePlus_Sky Matrix"
ghenv.Component.NickName = 'skyMatrix'
ghenv.Component.Message = 'VER 0.0.01\nDEC_05_2016'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '02 :: Daylight :: Light Sources'
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from honeybee.radiance.sky.skymatrix import SkyMatrix
except ImportError as e:
    msg = '\nFailed to import honeybee. Did you install honeybee on your machine?' + \
            '\nYou can download the installer file from github: ' + \
            'https://github.com/ladybug-analysis-tools/honeybee-plus/tree/master/plugin/grasshopper/samplefiles' + \
            '\nOpen an issue on github if you think this is a bug:' + \
            ' https://github.com/ladybug-analysis-tools/honeybee-plus/issues'
        
    raise ImportError('{}\n\t{}'.format(msg, e))

if _wea:
    skyMTX = SkyMatrix(_wea, _skyDensity_, north_, hoys_)