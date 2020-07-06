# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Radiance Scene.

Use this class to create a base for the radiance studies by using a number
of radiance files. The main advantage of creating a scene is to avoid re-creating
the geometries and writing the files in parametric studies.

-

    Args:
        _rad_files: List of radiance files. Valid files are *.rad, *.mat and *.oct.
        _copy_local_: Set to True to copy the files to the analysis folder (Default: True).
        _overwrite_: Set to True to overwrite the files if already exist (Default: True).
    Returns:
        rad_scene: A Radiance Scene that can be plugged into a Radiance Analysis in order
            to account for surrounding context.
"""

ghenv.Component.Name = "HoneybeePlus_Radiance Scene"
ghenv.Component.NickName = 'radScene'
ghenv.Component.Message = 'VER 0.0.06\nJUL_07_2020'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '00 :: Create'
ghenv.Component.AdditionalHelpFromDocStrings = "3"

try:
    from honeybee_plus.radiance.staticscene import StaticScene
except ImportError as e:
    raise ImportError('\nFailed to import honeybee_plus:\n\t{}'.format(e))

if _rad_files and _rad_files[0] is not None:
    rad_scene = StaticScene(_rad_files, _copy_local_, _overwrite_)