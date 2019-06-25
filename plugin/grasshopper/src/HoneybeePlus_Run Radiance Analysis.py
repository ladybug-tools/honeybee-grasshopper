# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Run Radiance Analysis

-

    Args:
        _analysis_recipe: Radiance analysis recipe. You can find the recipes under
            tab 03 | Daylight | Recipe.
        _HB_objects: A flatten list of Honeybee surfaces and zones.
        rad_scene_: A honeybee radiance scene that will be considered as the context
            for honeybee objects. Use Radiance Scene component to create a radScene.
        _folder_: An optional folder to save the files for this analysis.
        _name_: An optional name for this analysis.
        _write: Set to True to write the files to the folder.
        run_: Set to True to run the analysis. You can only run the analysis if
            _write is also set to True.
    Returns:
        report: Reports, errors, warnings, etc.
        outputs: Outputs of the analysis. Outputs can be a list of image
            collections or a list of analysis grids.
"""

ghenv.Component.Name = "HoneybeePlus_Run Radiance Analysis"
ghenv.Component.NickName = 'runRadiance'
ghenv.Component.Message = 'VER 0.0.05\nJUN_25_2019'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '04 :: Daylight :: Daylight'
ghenv.Component.AdditionalHelpFromDocStrings = "1"


try:
    _HB_objects.Flatten()
    _HB_objects = _HB_objects.Branch(0)
except AttributeError:
    # the case for Dynamo
    pass

if _HB_objects and [0] is not None and _analysis_recipe and _write:
    try:
        for obj in _HB_objects:
            assert hasattr(obj, 'isHBObject')
    except AssertionError:
        raise ValueError("\n{} is not a valid Honeybee object.".format(obj))
   
    assert hasattr(_analysis_recipe, 'isAnalysisRecipe'), \
        ValueError("\n{} is not a Honeybee recipe.".format(_analysis_recipe))

    if _write == True:
        # Add Honeybee objects to the recipe
        _analysis_recipe.hb_objects = _HB_objects
        _analysis_recipe.scene = rad_scene_

        batchFile = _analysis_recipe.write(_folder_, _name_)

    if _write == True and run_ == True:
        if _analysis_recipe.run(batchFile, False):
            try:
                outputs = _analysis_recipe.results()
            except StopIteration:
                raise ValueError(
                    'Length of the results is smaller than the analysis grids '
                    'point count [{}]. In case you have changed the analysis'
                    ' Grid you must re-calculate daylight/view matrix!'
                    .format(_analysis_recipe.total_point_count)
                )