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
        _analysisGrid: An analysis grid output from run Radiance analysis.
        _index_: An integer to pick the sensor from the analysis grid (default: 0).
    Returns:
        position: Position of the sensor
        sensor: Sensor object. Use this sensor to generate blind schedules for
            annual daylight analysis.
"""

ghenv.Component.Name = "HoneybeePlus_Sensor from analysis grid"
ghenv.Component.NickName = 'sensor'
ghenv.Component.Message = 'VER 0.0.02\nJUL_15_2017'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '04 :: Daylight :: Daylight'
ghenv.Component.AdditionalHelpFromDocStrings = "2"

try:
    import Rhino.Geometry.Point3d as P
    import Rhino.Geometry.Sphere as S
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))

if _analysisGrid:
    id = _index_ or 0
    sensor = _analysisGrid[id]
    p = P(sensor.location.x, sensor.location.y, sensor.location.z)
    position = S(p, 0.5)