# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Mass addition of values for a grid. This component is articularly useful for
solar access and radiation studies.

-

    Args:
        _analysis_grid: An analysis grid output from run Radiance analysis.
        hoys_: An optional list of hours for hours of the year if you don't want
            the analysis to be calculated for all the hours.
        blind_states_: A list of blind states for light sources as tuples for
            hours of the year. You can use Dynamic Blinds Schedule component
            to generate this schedule. If left empty the first state of each
            window group will be used.
        _mode_: An integer between 0-2 representing the type of value to output.
            0 = total values
            1 = direct values (if available)
            2 = diffuse sky + reflected values (if available).
    Returns:
        report: Reports, errors, warnings, etc.
        values: A list of cumulative values for each sensor.
"""

ghenv.Component.Name = "HoneybeePlus_Cumulative Value"
ghenv.Component.NickName = 'cumValue'
ghenv.Component.Message = 'VER 0.0.05\nAPR_27_2019'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '04 :: Daylight :: Daylight'
ghenv.Component.AdditionalHelpFromDocStrings = "4"

if _analysis_grid:
    _modes = ('total', 'direct', 'diffuse')
    _mode_ = _mode_ or 0
    hoys_ = hoys_ or _analysis_grid.hoys

    assert _mode_ < 3, '_mode_ can only be 0: total, 1: direct or 2: sky.'

    states = _analysis_grid.parse_blind_states(blind_states_)

    print('Loading sum of {} values.'.format(_modes[_mode_]))
    
    if _mode_ < 2:
        values = (v[_mode_] for v in
                  _analysis_grid.sum_values_by_id(hoys_, blinds_state_ids=states))
    else:
        cValues = _analysis_grid.sum_values_by_id(hoys_, blinds_state_ids=states)
        values = (v[0] - v[1] for v in cValues)