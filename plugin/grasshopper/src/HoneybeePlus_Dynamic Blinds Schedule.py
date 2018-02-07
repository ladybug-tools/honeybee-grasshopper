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
        _blindCombs_: Suggested states combinations for sources. Default is
            the longest combination between all the window groups. Put each
            state as a tuple. Check the sensor output for sources and possible
            states. For instance (0, 0, 1) indicates the first and second window
            groups are at state 0 and the third window group is at state 1.
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