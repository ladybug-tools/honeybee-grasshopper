# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Hourly results for an analysis grid for a single hour of the year.

-

    Args:
        _analysisGrid: An analysis grid output from run Radiance analysis.
        hoy_: An hour of the year (default: first available hour).
        blindState_: Blind states for light sources as a tuples. You can use
            If left empty the first state of each window group will be used.
        _mode_: An integer between 0-2. 0 returns that total values, 1 returns
            diret values if available and 2 returns sky + diffuse values if
            available.
    Returns:
        values: List of hourly values for each sensor.
"""

ghenv.Component.Name = "HoneybeePlus_Hourly Values"
ghenv.Component.NickName = 'hourlyValues'
ghenv.Component.Message = 'VER 0.0.03\nAUG_04_2017'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '04 :: Daylight :: Daylight'
ghenv.Component.AdditionalHelpFromDocStrings = "4"

from ladybug.dt import DateTime

try:
    from honeybee.radiance.recipe.solaraccess.gridbased import SolarAccessGridBased
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))

if _analysisGrid:
    _modes = ('total', 'direct', 'diffuse')
    _mode_ = _mode_ or 0
    hoy_ = hoy_ or _analysisGrid.hoys[0]
    assert _mode_ < 3, '_mode_ can only be 0: total, 1: direct or 2: sky.'

    try:
        states = eval(blindState_)
    except Exception as e:
        if blindState_:
            raise TypeError('Failed to read blindState_:\n{}'.format(e))
        states = None
    
    print('Loading {} values for {}.'.format(_modes[_mode_], DateTime.fromHoy(hoy_)))
    
    if _mode_ < 2:
        values = (v[_mode_] for v in _analysisGrid.combinedValueById(hoy_, states))
    else:
        cValues = _analysisGrid.combinedValueById(hoy_, states)
        values = (v[0] - v[1] for v in cValues)