# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Annual daylight analysis recipe.

Use this recipe to set up annual daylight analysis for scenes with no
window groups.

-

    Args:
        _skymtx: A sky matrix or a sky vector. Find honeybee skies under 02::Daylight::Light Sources.
        _analysis_grids: A list of Honeybee analysis grids.
        _analysis_type_: Analysis type. [0] illuminance(lux), [1] radiation (kwh),
            [2] luminance (Candela).
        _dmtx_par_: Radiance parameters for Daylight matrix calculation. Find
            Radiance parameters node under 03::Daylight::Recipe.
        reuse_dmtx_: A boolean to indicate if you want the analysis to use the daylight
            coeff matrix results from the previous study if available (default: False).
    Returns:
        analysis_recipe: Annual analysis recipe. Connect this recipe to Run Radiance
            Analysis to run a annual analysis.
"""

ghenv.Component.Name = "HoneybeePlus_Annual Daylight Recipe"
ghenv.Component.NickName = 'annualDLRecipe'
ghenv.Component.Message = 'VER 0.0.05\nOCT_22_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '03 :: Daylight :: Recipe'
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from honeybee.radiance.recipe.annual.gridbased import GridBased
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))


if _skymtx and _analysis_grids and _analysis_grids[0] is not None:
    reuse_dmtx_ = bool(reuse_dmtx_)
    analysis_recipe = GridBased(
        _skymtx, _analysis_grids, _analysis_type_, _dmtx_par_, reuse_dmtx_)