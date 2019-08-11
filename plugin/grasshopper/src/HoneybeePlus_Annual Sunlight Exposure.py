# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Calculate annual sunlight exposure (ASE).

As per IES-LM-83-12, ASE is the percent of sensors that are
found to be exposed to more than 1000lux of direct sunlight for
more than 250hrs per year. For LEED credits no more than 10% of
the points in the grid should fail this measure.
-

    Args:
        _analysis_grid: An analysis grid output from run Radiance analysis.
        blind_states_: List of state ids for all the sources for input hoys.
            If you want a source to be removed set the state to -1. ASE must
            be calculated without dynamic blinds but you can use this option
            to study the effect of different blind states.
        _occ_schedule_: An annual occupancy schedule.
        _threshold_: Threshhold for solar exposure in lux (default: 1000).
        _target_hrs_: Minimum target hours for each point (default: 250).
        _target_area_: Minimum target area percentage for this grid (default: 10)

    Returns:
        report: Reports, errors, warnings, etc.
        success: True if you meet target area based on target hours.
        ASE: Number of hours of annual sunlight exposure for each test point.
        per_area: Percentage area that doesn't meet the target.
        prblm_pts: A list of problematic test points.
        prblm_hrs: Problematic hours for each point.
        legend_par: Suggested legend parameters for Annual Sunlight Exposure.
"""

ghenv.Component.Name = "HoneybeePlus_Annual Sunlight Exposure"
ghenv.Component.NickName = 'ASE'
ghenv.Component.Message = 'VER 0.0.05\nAUG_10_2019'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '04 :: Daylight :: Daylight'
ghenv.Component.AdditionalHelpFromDocStrings = "3"

try:
    import ladybug.geometry as lg
    import ladybug.output as output
    import ladybug.legend as lp
    import ladybug.color as color
except ImportError as e:
    raise ImportError('\nFailed to import ladybug:\n\t{}'.format(e))


col = color.Colorset.original()
legend_par = lp.LegendParameters(0, 250, colors=col)

if _analysis_grid:
    states = _analysis_grid.parse_blind_states(blind_states_)
    success, ASE, per_area, prblm_pts, prblm_hrs = \
        _analysis_grid.annual_sunlight_exposure(
            _threshold_, states, _occ_schedule_, _target_hrs_, _target_area_
        )

    prblm_pts = (lg.point(s.location.x, s.location.y, s.location.z) for s in prblm_pts)
    # convert list of lists to data tree
    try:
        prblm_hrs = output.list_to_tree(prblm_hrs, ghenv.Component.RunCount - 1)
    except NameError:
        # dynamo
        pass