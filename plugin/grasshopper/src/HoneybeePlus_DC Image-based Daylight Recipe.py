# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Annual daylight coefficient image-based recipe.

-

    Args:
        _skymtx: A sky matrix or a sky vector. Find honeybee skies under 02::Daylight::Light Sources.
        _views: A list of Honeybee views.
        _analysis_type_: Analysis type. [0] illuminance(lux), [1] radiation (kwh),
            [2] luminance (Candela).
        _dmtx_par_: Radiance parameters for Image-based analysis. Find Radiance
            parameters node under 03::Daylight::Recipes.
        reuse_dmtx_: A boolean to indicate if you want the analysis to use the daylight
            coeff matrix results from the previous study if available (default: False).
    Returns:
        analysis_recipe: Annual analysis recipe. Connect this recipe to Run Radiance
            Analysis to run a annual analysis.
"""

ghenv.Component.Name = "HoneybeePlus_DC Image-based Daylight Recipe"
ghenv.Component.NickName = 'DCoeffIBRecipe'
ghenv.Component.Message = 'VER 0.0.06\nJUL_07_2020'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '03 :: Daylight :: Recipe'
ghenv.Component.AdditionalHelpFromDocStrings = "3"

try:
    from honeybee_plus.radiance.recipe.daylightcoeff.imagebased import DaylightCoeffImageBased
except ImportError as e:
    raise ImportError('\nFailed to import honeybee_plus:\n\t{}'.format(e))


if _skymtx and _views:
    # check inputs
    assert _skymtx.sky_density < 2, ValueError(
        'Due to Windows limitations on the maximum number of files that can be\n'
        ' open concurrently image-based analysis only works with skyDensity of 1.')
    
    analysis_recipe = DaylightCoeffImageBased(
        _skymtx, _views, _analysis_type_, _dmtx_par_,
        reuse_daylight_mtx=reuse_dmtx_)