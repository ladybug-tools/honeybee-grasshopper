# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Annual radiation analysis

-

    Args:
        _skymtx: A sky matrix or a sky vector. Find honeybee skies under 02::Daylight::Light Sources.
        _analysisGrids: A list of Honeybee analysis grids.
        _dmtxPar_: Radiance parameters for Daylight matrix calculation. Find
            Radiance parameters node under 03::Daylight::Recipe.
        reuseDmtx_: A boolean to indicate if you want the analysis to use the daylight
            coeff matrix results from the previous study if available (default: False).
    Returns:
        readMe!: Reports, errors, warnings, etc.
        analysisRecipe: Annual analysis recipe. Connect this recipe to Run Radiance
            Analysis to run a annual analysis.
"""

ghenv.Component.Name = "HoneybeePlus_Annual Radiation Recipe"
ghenv.Component.NickName = 'radiationRecipe'
ghenv.Component.Message = 'VER 0.0.04\nFEB_07_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '03 :: Daylight :: Recipe'
ghenv.Component.AdditionalHelpFromDocStrings = "1"


#import honeybee
#reload(honeybee.radiance.recipe.recipedcutil)
#reload(honeybee.radiance.recipe.daylightcoeff.gridbased)
#reload(honeybee.radiance.recipe.radiation.gridbased)
try:
    from honeybee.radiance.recipe.radiation.gridbased import GridBased
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))


if _skymtx and _analysisGrids and _analysisGrids[0] != None:
    reuseDmtx_ = bool(reuseDmtx_)
    analysisRecipe = GridBased(_skymtx, _analysisGrids, _dmtxPar_, reuseDmtx_)