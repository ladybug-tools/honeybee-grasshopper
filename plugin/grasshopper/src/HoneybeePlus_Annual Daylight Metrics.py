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
         blindStates_: List of state ids for all the sources for input hoys.
            If you want a source to be removed set the state to -1. ASE must
            be calculated without dynamic blinds but you can use this option
            to study the effect of different blind states.
        _occSchedule_: An annual occupancy schedule.
        _threshold_: Threshhold for daylight autonomy in lux (default: 300).
        _minmax_: A list for min, max value for useful daylight illuminance
                (default: (100, 3000)).

    Returns:
        DA: Daylight autonomy. The percentage of time that each sensor
            recieves equal or more than the threshold.
        CDA: Continuous daylight autonomy.
        UDI: Useful daylight illuminance. The percentage of time that illuminace
            falls between minimum and maximum thresholds.
        UDILess: The percentage of time that illuminace falls less than minimum
            threshold.
        UDIMore: The percentage of time that illuminace falls more than maximum
            threshold.
"""

ghenv.Component.Name = "HoneybeePlus_Annual Daylight Metrics"
ghenv.Component.NickName = 'annualMetrics'
ghenv.Component.Message = 'VER 0.0.02\nJUL_20_2017'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '04 :: Daylight :: Daylight'
ghenv.Component.AdditionalHelpFromDocStrings = "3"

if _analysisGrid:
    states = tuple(eval(t) for t in blinds_state_)
    DA, CDA, UDI, UDILess, UDIMore = _analysisGrid.annualMetrics(
        _threshold_, _minmax_, blindStates_, _occSchedule_
    )