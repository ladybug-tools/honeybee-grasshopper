# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Annual Daylight Metrics.

-

    Args:
        _analysis_grid: An analysis grid output from run Radiance analysis.
         blind_states_: List of state ids for all the sources for input hoys.
            If you want a source to be removed set the state to -1. You can use
            this option to study the effect of different blind states.
        _occ_schedule_: An annual occupancy schedule.
        _threshold_: Threshhold for daylight autonomy in lux (default: 300).
        _min_max_: A list for min, max value for useful daylight illuminance
                (default: (100, 3000)).

    Returns:
        report: Reports, errors, warnings, etc.
        DA: Daylight autonomy. The percentage of time that each sensor
            recieves equal or more than the threshold.
        CDA: Continuous daylight autonomy.
        UDI: Useful daylight illuminance. The percentage of time that illuminace
            falls between minimum and maximum thresholds.
        UDI_less: The percentage of time that illuminace falls less than minimum
            threshold.
        UDI_more: The percentage of time that illuminace falls more than maximum
            threshold.
        legend_par: Suggested legend parameters for annual metrics.
"""

ghenv.Component.Name = "HoneybeePlus_Annual Daylight Metrics"
ghenv.Component.NickName = 'annualMetrics'
ghenv.Component.Message = 'VER 0.0.05\nOCT_22_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '04 :: Daylight :: Daylight'
ghenv.Component.AdditionalHelpFromDocStrings = "3"

try:
    import ladybug.legendparameters as lp
    import ladybug.color as color
except ImportError as e:
    raise ImportError('\nFailed to import ladybug:\n\t{}'.format(e))

col = color.Colorset.nuanced()
legend_par = lp.LegendParameters((0, 100), colors=col)

if _analysis_grid:
    states = _analysis_grid.parse_blind_states(blind_states_)
    DA, CDA, UDI, UDI_less, UDI_more = _analysis_grid.annual_metrics(
        _threshold_, _min_max_, states, _occ_schedule_
    )