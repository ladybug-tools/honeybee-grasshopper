# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Occupancy Schedule

-

    Args:
        _analysisGrid: An analysis grid output from run Radiance analysis.
        _index_: An integer to pick the sensor from the analysis grid (default: 0).
    Returns:
        position: Position of the sensor
        sensor: Sensor object. Use this sensor to generate blind schedules for
            annual daylight analysis.
"""

ghenv.Component.Name = "HoneybeePlus_Occupancy Schedule"
ghenv.Component.NickName = 'occSchdule'
ghenv.Component.Message = 'VER 0.0.02\nJUL_15_2017'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '00 :: Create'
ghenv.Component.AdditionalHelpFromDocStrings = "3"

from honeybee.schedule import Schedule

schedule = Schedule.fromAnalysisPeriod()