# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Five-pahse daylight Recipe.

-

    Args:
        _skymtx: A sky matrix or a sky vector. Find honeybee skies under 02::Daylight::Light Sources.
        _analysisGrids: A list of Honeybee analysis grids.
        _analysisType_: Analysis type. [0] illuminance(lux), [1] radiation (kwh),
            [2] luminance (Candela).
        _radiancePar_: Radiance parameters for Grid-based analysis. Find Radiance
            parameters node under 03::Daylight::Recipes.
    Returns:
        readMe!: Reports, errors, warnings, etc.
        analysisRecipe: Five-pahse analysis recipe. Connect this recipe to Run
            Radiance Analysis.
"""

ghenv.Component.Name = "HoneybeePlus_Grid-Based Five-Phase Daylight Recipe"
ghenv.Component.NickName = 'fivePhaseGBRecipe'
ghenv.Component.Message = 'VER 0.0.03\nAUG_04_2017'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '03 :: Daylight :: Recipe'
ghenv.Component.AdditionalHelpFromDocStrings = "4"

#import honeybee
#reload(honeybee.radiance.recipe.daylightcoeff.gridbased)
#reload(honeybee.radiance.recipe.threephase.gridbased)
#reload(honeybee.radiance.recipe.fivephase.gridbased)

try:
    from honeybee.radiance.recipe.fivephase.gridbased import FivePhaseGridBased
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))


if _skymtx and _analysisGrids:
    reuseVmtx_ = bool(reuseVmtx_)
    reuseDmtx_ = bool(reuseDmtx_)
    assert _analysisType_ == 0, \
        ValueError('3Phase recipe currently only supports illuminance simulation.')
    analysisRecipe = FivePhaseGridBased(
        _skymtx, _analysisGrids, _analysisType_, _vmtxPar_, _dmtxPar_,
        reuseVmtx_, reuseDmtx_)