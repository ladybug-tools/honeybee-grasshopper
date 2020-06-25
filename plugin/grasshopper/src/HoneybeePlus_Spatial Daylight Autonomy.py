# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Calculate Spatial Daylight Autonomy (sDA).

As per IES-LM-83-12 Spatial Daylight Autonomy (sDA) is a metric describing
annual sufficiency of ambient daylight levels in interior environments.
It is defined as the percent of an analysis area (the area where calcuations
are performed -typically across an entire space) that meets a minimum
daylight illuminance level for a specified fraction of the operating hours
per year. The sDA value is expressed as a percentage of area.

    Args:
        _analysis_grid: An analysis grid output from run Radiance analysis.
        blind_states_: List of state ids for all the sources for input hoys.
            If you want a source to be removed set the state to -1. As per
            IES-LM-83-12 the blinds must be closed at any point of time that
            more than 2% of analysis points recieve direct sunlight.
        _occ_schedule_: An annual occupancy schedule. As per IES-LM-83 the
            schedule should be 8am to 6pm (10 hours during the day).
        _threshold_: Threshhold for daylight autonomy in lux (default: 300).
        _target_DA_: Minimum target percentage for daylight autonomy (default: 50).

    Returns:
        report: Reports, errors, warnings, etc.
        sDA: Spatial daylight autonomy as percentage of area for each analysis
            grid.
        DA: Daylight autonomy for each point in each analysis grid.
        prblm_Pts: A list of problematic test points with spatial daylight autonomy
            less then targetDA.
"""

ghenv.Component.Name = "HoneybeePlus_Spatial Daylight Autonomy"
ghenv.Component.NickName = 'sDA'
ghenv.Component.Message = 'VER 0.0.05\nMAR_28_2020'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '04 :: Daylight :: Daylight'
ghenv.Component.AdditionalHelpFromDocStrings = "3"

try:
    from ladybug_rhino.fromgeometry import from_point3d
except ImportError as e:
    raise ImportError('\nFailed to import ladybug_rhino:\n\t{}'.format(e))

if _analysis_grid:
    states = _analysis_grid.parse_blind_states(blind_states_)
    sDA, DA, prblm_Pts = _analysis_grid.spatial_daylight_autonomy(
         _threshold_, _target_DA_, states, _occ_schedule_
    )

    prblm_pts = (from_point3d(s.location) for s in prblm_Pts)
