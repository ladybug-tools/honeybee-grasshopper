# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Daylight Coefficient Grid-based Daylight Recipe.
Use this recipe to set up annual daylight analysis.

-

    Args:
        _skymtx: A sky matrix or a sky vector. Find honeybee skies under 02::Daylight::Light Sources.
        _analysisGrids: A list of Honeybee analysis grids.
        _analysisType_: Analysis type. [0] illuminance(lux), [1] radiation (kwh),
            [2] luminance (Candela).
        _dmtxPar_: Radiance parameters for Daylight matrix calculation. Find
            Radiance parameters node under 03::Daylight::Recipe.
        reuseDmtx_: A boolean to indicate if you want the analysis to use the daylight
            coeff matrix results from the previous study if available.
    Returns:
        readMe!: Reports, errors, warnings, etc.
        analysisRecipe: Annual analysis recipe. Connect this recipe to Run Radiance
            Analysis to run a annual analysis.
"""

ghenv.Component.Name = "HoneybeePlus_DC Grid-based Daylight Recipe"
ghenv.Component.NickName = 'DCoeffGBRecipe'
ghenv.Component.Message = 'VER 0.0.02\nJUL_29_2017'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '03 :: Daylight :: Recipe'
ghenv.Component.AdditionalHelpFromDocStrings = "3"

#import honeybee
#reload(honeybee.radiance.recipe.daylightcoeff.gridbased)

try:
    from honeybee.radiance.recipe.daylightcoeff.gridbased import DaylightCoeffGridBased
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))


if _skymtx and _analysisGrids and _analysisGrids[0] != None:
    reuseDmtx_ = bool(reuseDmtx_)
    analysisRecipe = DaylightCoeffGridBased(
        _skymtx, _analysisGrids, _analysisType_, _dmtxPar_, reuseDmtx_)