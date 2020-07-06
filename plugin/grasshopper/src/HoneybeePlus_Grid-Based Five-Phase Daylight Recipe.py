# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Annual five-pahse daylight recipe.

-

    Args:
        _skymtx: A sky matrix or a sky vector. Find honeybee skies under 02::Daylight::Light Sources.
        _analysis_grids: A list of Honeybee analysis grids.
        _analysis_type_: Analysis type. [0] illuminance(lux), [1] radiation (kwh),
            [2] luminance (Candela).
        _vmtx_par_: RfluxMtx parameters for view coefficient calculation.
        _dmtx_par_: RfluxMtx parameters for daylight coefficient calculation.
        reuse_vmtx_: A boolean to indicate if you want the analysis to use the view
            coeff matrix results from the previous study if available.
        reuse_dmtx_: A boolean to indicate if you want the analysis to use the daylight
            coeff matrix results from the previous study if available (default: False).
    Returns:
        analysis_recipe: Five-pahse analysis recipe. Connect this recipe to Run
            Radiance Analysis.
"""

ghenv.Component.Name = "HoneybeePlus_Grid-Based Five-Phase Daylight Recipe"
ghenv.Component.NickName = 'fivePhaseGBRecipe'
ghenv.Component.Message = 'VER 0.0.06\nJUL_07_2020'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '03 :: Daylight :: Recipe'
ghenv.Component.AdditionalHelpFromDocStrings = "4"

try:
    from honeybee_plus.radiance.recipe.fivephase.gridbased import FivePhaseGridBased
except ImportError as e:
    raise ImportError('\nFailed to import honeybee_plus:\n\t{}'.format(e))


if _skymtx and _analysis_grids:
    reuse_vmtx_ = bool(reuse_vmtx_)
    reuse_dmtx_ = bool(reuse_dmtx_)
    assert _analysis_type_ == 0, \
        ValueError('3Phase recipe currently only supports illuminance simulation.')
    analysis_recipe = FivePhaseGridBased(
        _skymtx, _analysis_grids, _analysis_type_, _vmtx_par_, _dmtx_par_,
        reuse_vmtx_, reuse_dmtx_)