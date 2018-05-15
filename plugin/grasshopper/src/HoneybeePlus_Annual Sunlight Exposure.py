# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Calculate annual sunlight exposure (ASE).

As per IES-LM-83-12 ASE is the percent of sensors that are
found to be exposed to more than 1000lux of direct sunlight for
more than 250hrs per year. For LEED credits no more than 10% of
the points in the grid should fail this measure.
-

    Args:
        _analysisGrid: An analysis grid output from run Radiance analysis.
        blindStates_: List of state ids for all the sources for input hoys.
            If you want a source to be removed set the state to -1. ASE must
            be calculated without dynamic blinds but you can use this option
            to study the effect of different blind states.
        _occSchedule_: An annual occupancy schedule.
        _threshold_: Threshhold for solar exposure in lux (default: 1000).
        _targetHrs_: Minimum targe hours for each point (default: 250).
        _targetArea_: Minimum target area percentage for this grid (default: 10)
        legendPar: Suggested legend parameters for Annual Sunlight Exposure.

    Returns:
        Success: True if you meet target area based on target hours.
        ASE: Number of hours of annual sunlight exposure for each test point.
        perArea: Percentage area that doesn't meet the target.
        prblmPts: A list of problematic test points.
        prblmHrs: Problematic hours for each point.
"""

ghenv.Component.Name = "HoneybeePlus_Annual Sunlight Exposure"
ghenv.Component.NickName = 'ASE'
ghenv.Component.Message = 'VER 0.0.05\nMAY_14_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '04 :: Daylight :: Daylight'
ghenv.Component.AdditionalHelpFromDocStrings = "3"

try:
    import ladybug.geometry as lg
    import ladybug.output as output
    import ladybug.legendparameters as lp
    import ladybug.color as color
except ImportError as e:
    raise ImportError('\nFailed to import ladybug:\n\t{}'.format(e))


col = color.Colorset.original()
legendPar = lp.LegendParameters((0, 250), colors=col)

if _analysisGrid:
    states = _analysisGrid.parse_blind_states(blindStates_)
    success, ASE, perArea, prblmPts, prblmHrs = \
        _analysisGrid.annual_sunlight_exposure(
            _threshold_, states, _occSchedule_, _targetHrs_, _targetArea_
        )

    prblmPts = (lg.point(s.location.x, s.location.y, s.location.z) for s in prblmPts)
    # convert list of lists to data tree
    try:
        prblmHrs = output.list_to_tree(prblmHrs, ghenv.Component.RunCount - 1)
    except NameError:
        # dynamo
        pass