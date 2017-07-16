# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Three-pahse daylight Recipe.

-

    Args:
        _skymtx: A sky matrix or a sky vector. Find honeybee skies under 02::Daylight::Light Sources.
        _analysisGrids: A list of Honeybee analysis grids.
        _analysisType_: Analysis type. [0] illuminance(lux), [1] radiation (kwh),
            [2] luminance (Candela).
        _vmtxPar_: RfluxMtx parameters for view coefficient calculation.
        _dmtxPar_: RfluxMtx parameters for daylight coefficient calculation.
        reuseVmtx_: A boolean to indicate if you want the analysis to use the view
            coeff matrix results from the previous study if available.
        reuseDmtx_: A boolean to indicate if you want the analysis to use the daylight
            coeff matrix results from the previous study if available.
    Returns:
        readMe!: Reports, errors, warnings, etc.
        analysisRecipe: Three-pahse analysis recipe. Connect this recipe to Run
            Radiance Analysis.
"""

ghenv.Component.Name = "HoneybeePlus_Grid-Based Three-Phase Daylight Recipe"
ghenv.Component.NickName = 'threePhaseGBRecipe'
ghenv.Component.Message = 'VER 0.0.02\nJUL_15_2017'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '03 :: Daylight :: Recipe'
ghenv.Component.AdditionalHelpFromDocStrings = "4"


try:
    from honeybee.radiance.recipe.threephase.gridbased import ThreePhaseGridBased
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))


if _skymtx and _analysisGrids:
    reuseVmtx_ = reuseVmtx_ or True
    reuseDmtx_ = reuseDmtx_ or True
    analysisRecipe = ThreePhaseGridBased(
        _skymtx, _analysisGrids, _analysisType_, _vmtxPar_, _dmtxPar_,
        reuseVmtx_, reuseDmtx_)