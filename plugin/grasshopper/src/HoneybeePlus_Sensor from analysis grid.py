# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Sensor from analysis grid

-

    Args:
        _analysis_grid: An analysis grid output from a Radiance analysis.
        _index_: An integer to pick the index of the sensor in the analysis_grid (default: 0).
    Returns:
        position: Position of the sensor
        sensor: Sensor object. Use this sensor to generate blind schedules for
            annual daylight analysis.
"""

ghenv.Component.Name = "HoneybeePlus_Sensor from analysis grid"
ghenv.Component.NickName = 'sensor'
ghenv.Component.Message = 'VER 0.0.06\nJUL_07_2020'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '04 :: Daylight :: Daylight'
ghenv.Component.AdditionalHelpFromDocStrings = "2"


try:
    from ladybug_rhino.fromgeometry import from_point3d
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))

if _analysis_grid:
    if _analysis_grid.digit_sign == 1:
        _analysis_grid.load_values_from_files()

    id = _index_ if _index_ is not None else 0
    sensor = _analysis_grid[id]
    position = from_point3d(sensor.location)
