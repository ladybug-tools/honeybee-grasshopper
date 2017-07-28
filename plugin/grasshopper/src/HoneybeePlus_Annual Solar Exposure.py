# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Calculate annual solar exposure (ASE).

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

    Returns:
        Success: True if you meet target area based on target hours.
        ASE: Number of hours of annual solar exposure for each test point.
        perArea: Percentage area that doesn't meet the target.
        prblmPts: A list of problematic test points.
        prblmHrs: Problematic hours for each point.
"""

ghenv.Component.Name = "HoneybeePlus_Annual Solar Exposure"
ghenv.Component.NickName = 'ASE'
ghenv.Component.Message = 'VER 0.0.02\nJUL_28_2017'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '04 :: Daylight :: Daylight'
ghenv.Component.AdditionalHelpFromDocStrings = "3"

try:
    import ladybug.geometry as lg
    import ladybug.output as output
except ImportError as e:
    raise ImportError('\nFailed to import ladybug:\n\t{}'.format(e))

if _analysisGrid:
    states = _analysisGrid.parseBlindStates(blindStates_)
    success, ASE, perArea, prblmPts, prblmHrs = _analysisGrid.annualSolarExposure(
         _threshold_, states, _occSchedule_, _targetHrs_, _targetArea_
    )

    prblmPts = (lg.point(s.location.x, s.location.y, s.location.z) for s in prblmPts)
    # convert list of lists to data tree
    prblmHrs = output.listToTree(prblmHrs, ghenv.Component.RunCount - 1)
