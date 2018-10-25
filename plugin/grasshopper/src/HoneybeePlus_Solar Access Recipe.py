# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Solar access recipe.

-

    Args:
        _sun_vectors: A list of vectors that represents sun vectors. You can use
            Ladybug sunpath to generate the vectors for any time of the year. If
            you're generating the vectors in a different way make sure that the
            vectors are looking downwards from the sun (e.g. z < 0).
        _hoys: A list of hours of the year.
        _analysis_grids: List of honeybee analysis grids. Use Analysis grid component
            which you can find under 00 :: Create to create them.
        _timestep_: Timstep for sun vectors. Default is 1 which means each sun vector
            represents an hour of time.
    Returns:
        readMe!: Reports, errors, warnings, etc.
        analysis_recipe: Sunlight hours analysis recipe. Connect this recipe to
            Run Radiance Simulation to run a sunlight hours analysis.
"""

ghenv.Component.Name = "HoneybeePlus_Solar Access Recipe"
ghenv.Component.NickName = 'solarAccessRecipe'
ghenv.Component.Message = 'VER 0.0.05\nOCT_22_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '03 :: Daylight :: Recipe'
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from honeybee.radiance.recipe.solaraccess.gridbased import SolarAccessGridBased
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))


if _sun_vectors and _sun_vectors[0] is not None and \
    _hoys and _hoys[0] is not None and _analysis_grids \
    and _analysis_grids[0] is not None:
    # set a sunlight hours analysis recipe together if there are points
    analysis_recipe = SolarAccessGridBased(
        _sun_vectors, _hoys, _analysis_grids, _timestep_)