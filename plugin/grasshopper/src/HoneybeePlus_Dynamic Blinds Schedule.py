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
        _analysisGrid: An analysis grid output from run Radiance analysis.
        _index_: An integer to pick the sensor from the analysis grid (default: 0).
    Returns:
        position: Position of the sensor
        sensor: Sensor object. Use this sensor to generate blind schedules for
            annual daylight analysis.
"""

ghenv.Component.Name = "HoneybeePlus_Dynamic Blinds Schedule"
ghenv.Component.NickName = 'dynBlindSchd'
ghenv.Component.Message = 'VER 0.0.02\nJUL_15_2017'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '04 :: Daylight :: Daylight'
ghenv.Component.AdditionalHelpFromDocStrings = "2"

import copy

if _sensor:
    sensor = _sensor
    
    # print the details to help user set up the 
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

#    states = tuple(eval(t) for t in _combs_)
#    print states
    results = sensor.blindsState(sensor.hoys, _combs_)
    if results:
        blinds_state = (str(d) for d in results[0])  # tuple is not a standard GH Type
        blinds_index = results[1]
        illum = results[2]
        illum_dir = results[3]
        success = results[4]