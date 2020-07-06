# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Occupancy Schedule from hourly values.

-

    Args:
        _values: Schedule values.
        hoys_: List of hours of the year for this values (default: 0-8759).
    Returns:
        schedule: Honeybee Schedule.
"""

ghenv.Component.Name = "HoneybeePlus_Occupancy Schedule"
ghenv.Component.NickName = 'occSchedule'
ghenv.Component.Message = 'VER 0.0.06\nJUL_07_2020'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '00 :: Create'
ghenv.Component.AdditionalHelpFromDocStrings = "3"

try:
    from honeybee_plus.schedule import Schedule
except ImportError as e:
    raise ImportError('\nFailed to import honeybee_plus:\n\t{}'.format(e))

if _values:
    schedule = Schedule(_values, hoys_)