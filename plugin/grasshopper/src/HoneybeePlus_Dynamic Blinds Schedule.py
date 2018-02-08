# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Dynamic Blinds Schedule

-

    Args:
        _sensor: A single sensor from the analsysi Grid.
        _blindCombs_: Suggested blind state combinations of window groups for meeting the logic.
            States can be one of the following:
            -1 = No light from window source (opaque)
            0 = Normal window state (typically transparent)
            1 = The first shade state (assuming one has been assigned)
            2 = the second shade state (assuming one has been assigned)
            ... etc.
            Put each state as a tuple that has a length equal to the number of
            window groups in the model (check the report output of this component to see
            the order of the window groups). For instance (0, 0, 1) indicates that the 
            first and second window groups are at state 0 and the third window group is
            at state 1. If you plug in a list of tuples, honeybee will try to meet the logic 
            by first using the first tuple in the list.  If that doesn't work, the second 
            tuple will be used, etc.
            The default is the longest combination of all window groups.
            For example if you have 3 window groups. The first with 1 state,
            the second with 3 states and the last with 2 states. The combinations
            are (0,0,0), (0,1,1) and (0,2,1). State -1 will never be assigned
            by default.
        _logic_: Blinds logic. You can use ill, ill_dir and h(our) as input
            values. Default is ill > 3000. You can also overwrite the logic
            by opening the components and edit 'checkLogic' function.
        data_: optional data to pass along side the values which can be used
            to set-up the logic. This input yet needs to be tested.
    Returns:
        blindStates: Selected blind states based on input logic.
        blindStIndex: Index of selected blind state from input _blindStates_.
        illumTotal: Sensor total illuminance values.
        illumDirect: Sensor direct illuminance values. This value won't be available
            for 3-Phase recipe.
        success: A boolean that shows if the logic is satisfied by using the current
            combinations of shadings.
"""

ghenv.Component.Name = "HoneybeePlus_Dynamic Blinds Schedule"
ghenv.Component.NickName = 'dynBlindSchd'
ghenv.Component.Message = 'VER 0.0.04\nFEB_07_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '04 :: Daylight :: Daylight'
ghenv.Component.AdditionalHelpFromDocStrings = "2"

import copy

if _sensor:
    sensor = _sensor
    
    # print the details to help user set up the combination
    print(sensor.details)
    
    if _logic_:
    
        logic = compile('r = {}'.format(_logic_), '<string>', 'exec')
        data = data_
        def checkLogic(ill, ill_dir, hour, *data, **kwargs):
            exec(logic)
            return r
    
        setattr(sensor, 'logic', checkLogic)
    else:
        setattr(sensor, 'logic', sensor._logic)

    
    states = sensor.parse_blind_states(_blindCombs_)
    results = sensor.blinds_state(sensor.hoys, states)
    if results:
        blindStates = (str(d) for d in results[0])  # tuple is not a standard GH Type
        blindStIndex = results[1]
        illumTotal = results[2]
        illumDirect = results[3]
        success = results[4]