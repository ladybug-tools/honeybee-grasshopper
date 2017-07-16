# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Annual Daylight Metrics

-

    Args:
        _analysisGrid: An analysis grid output from run Radiance analysis.
        _index_: An integer to pick the sensor from the analysis grid (default: 0).
    Returns:
        position: Position of the sensor
        sensor: Sensor object. Use this sensor to generate blind schedules for
            annual daylight analysis.
"""

ghenv.Component.Name = "HoneybeePlus_Annual Daylight Metrics"
ghenv.Component.NickName = 'annDayMetrics'
ghenv.Component.Message = 'VER 0.0.02\nJUL_15_2017'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '04 :: Daylight :: Daylight'
ghenv.Component.AdditionalHelpFromDocStrings = "3"

if _analysisGrid:
    states = tuple(eval(t) for t in blinds_state_)
    DA, CDA, UDI, UDI_less, UDI_more = \
        _analysisGrid.annualMetrics(_DA_thresholds_, _UDI_min_max_, states,
                            _occSchedule_)