# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Write honeybee objects to a Radiance file.

-

    Args:
        _HB_objects: A list of honeybee objects.
        _folder: Path to targert folder (e.g. c:\ladybug\context).
        _file_name: File name as a string.
        _write: Set to True to write the file.
    Returns:
        readMe!: Reports, errors, warnings, etc.
        rad_file: Fullpath to the radiance file. Use this file to create a radiance
            scene.
"""

ghenv.Component.Name = "HoneybeePlus_Write HBObjects to Radiance"
ghenv.Component.NickName = 'HBToRad'
ghenv.Component.Message = 'VER 0.0.05\nOCT_22_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '00 :: Create'
ghenv.Component.AdditionalHelpFromDocStrings = "3"

try:
    from honeybee.radiance.radfile import RadFile
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))


if _HB_objects and _folder and _file_name and _write:
    rf = RadFile(_HB_objects)
    rad_file = rf. write(_folder, _file_name, mkdir=True)