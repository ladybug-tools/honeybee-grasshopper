# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Typical Occupancy Schedule based on space program.

-

    Args:
        _type_: 0 > Office
    Returns:
        schedule: Annual schedule.
"""

ghenv.Component.Name = "HoneybeePlus_Occupancy Schedule by Type"
ghenv.Component.NickName = 'occSchduleByType'
ghenv.Component.Message = 'VER 0.0.02\nJUL_20_2017'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '00 :: Create'
ghenv.Component.AdditionalHelpFromDocStrings = "3"

try:
    from honeybee.schedule import Schedule
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))

_type_ = _type_ or 0
schedule = Schedule.fromAnalysisPeriod()