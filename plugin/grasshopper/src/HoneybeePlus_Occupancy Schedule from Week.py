# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Typical Occupancy Schedule based on typical week.

-

    Args:
        _occHours_: Start and end hour of work day as a tuple. Default is (8, 17).
        _offHours_: A list of hours that building is unoccupied during the occupancy
            period everyday (e.g. lunch break). Default is an hour lunch break at
            (12, 13). Use -1 for no break during the day.
        _weekend_: A list of numbers to indicate the weekend days. [0] None, [1-7] MON
            to SUN. Default is 6, 7 (SAT, SUN).
        _defValue_: Default value for occupancy hours (Default: 1).
    Returns:
        schedule: Annual schedule.
        values: Annual hourly values for this schedule. Use this output to double
            check the results. Use 3d chart to visualize the values.
"""

ghenv.Component.Name = "HoneybeePlus_Occupancy Schedule from Week"
ghenv.Component.NickName = 'occSchduleWeek'
ghenv.Component.Message = 'VER 0.0.02\nJUL_27_2017'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '00 :: Create'
ghenv.Component.AdditionalHelpFromDocStrings = "3"

try:
    from honeybee.schedule import Schedule
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))

schedule = Schedule.fromWorkdayHours(
    _occHours_, _offHours_, _weekend_, _defValue_)

values = schedule.values