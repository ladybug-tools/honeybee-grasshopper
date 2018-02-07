# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Calculate spacial daylight autonomy (sDA).

As per IES-LM-83-12 Spatial Daylight Autonomy (sDA) is a metric describing
annual sufficiency of ambient daylight levels in interior environments.
It is defined as the percent of an analysis area (the area where calcuations
are performed -typically across an entire space) that meets a minimum
daylight illuminance level for a specified fraction of the operating hours
per year. The sDA value is expressed as a percentage of area.

    Args:
        _analysisGrid: An analysis grid output from run Radiance analysis.
        blindStates_: List of state ids for all the sources for input hoys.
            If you want a source to be removed set the state to -1. As per
            IES-LM-83-12 the blinds must be closed at any point of time that
            more than 2% of analysis points recieve direct sunlight.
        _occSchedule_: An annual occupancy schedule. As per IES-LM-83 the
            schedule should be 8am to 6pm (10 hours during the day).
        _threshold_: Threshhold for daylight autonomy in lux (default: 300).
        _targetDA_: Minimum target percentage for daylight autonomy (default: 50).

    Returns:
        sDA: Spatial daylight autonomy as percentage of area for each analysis
            grid.
        DA: Daylight autonomy for each point in each analysis grid.
        prblmPts: A list of problematic test points with spatial daylight autonomy
            less then targetDA.
"""

ghenv.Component.Name = "HoneybeePlus_Spatial Daylight Autonomy"
ghenv.Component.NickName = 'sDA'
ghenv.Component.Message = 'VER 0.0.03\nFEB_07_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '04 :: Daylight :: Daylight'
ghenv.Component.AdditionalHelpFromDocStrings = "3"

try:
    import ladybug.geometry as lg
except ImportError as e:
    raise ImportError('\nFailed to import ladybug:\n\t{}'.format(e))

if _analysisGrid:
    states = _analysisGrid.parse_blind_states(blindStates_)
    sDA, DA, prblmPts = _analysisGrid.spatial_daylight_autonomy(
         _threshold_, _targetDA_, states, _occSchedule_
    )
    prblmPts = (lg.point(s.location.x, s.location.y, s.location.z) for s in prblmPts)