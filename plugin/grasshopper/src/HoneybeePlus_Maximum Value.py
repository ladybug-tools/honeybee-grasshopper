# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Maximum values for a grid.
-

    Args:
        _analysis_grid: An analysis grid output from run Radiance analysis.
        hoys_: An optional list of hours for hours of the year if you don't want
            the analysis to be calculated for all the hours.
        blind_states_: A list of blind states for light sources as tuples for
            hours of the year. You can use Dynamic Blinds Schedule component
            to generate this schedule. If left empty the first state of each
            window group will be used.
        _mode_: An integer between 0-2. 0 returns that total values, 1 returns
            diret values if available and 2 returns sky + diffuse values if
            available.
    Returns:
        values: A list of maximum values for each sensor.
"""

ghenv.Component.Name = "HoneybeePlus_Maximum Value"
ghenv.Component.NickName = 'maxValue'
ghenv.Component.Message = 'VER 0.0.05\nOCT_22_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '04 :: Daylight :: Daylight'
ghenv.Component.AdditionalHelpFromDocStrings = "4"

if _analysis_grid:
    _modes = ('total', 'direct', 'diffuse')
    _mode_ = _mode_ or 0
    assert _mode_ < 3, '_mode_ can only be 0: total, 1: direct or 2: sky.'
    states = _analysis_grid.parse_blind_states(blind_states_)
    print('Calculating max values from {} values.'.format(_modes[_mode_]))
    if _mode_ < 2:
        values = (v[_mode_] for v in _analysis_grid.max_values_by_id(blinds_state_ids=states))
    else:
        cValues = _analysis_grid.max_values_by_id(blinds_state_ids=states)
        values = (v[0] - v[1] for v in cValues)