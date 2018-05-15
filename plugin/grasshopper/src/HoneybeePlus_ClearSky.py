# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Convert a stat file into a WEA object with an original ASHRAE Clear Sky.

-

    Args:
        _location = The output from the importEPW or constructLocation component.
            This is essentially a list of text summarizing a location on the
            earth.
        clearness_: A factor that will be multiplied by the output of the model.
            This is to help account for locations where clear, dry skies predominate
            (e.g., at high elevations) or, conversely, where hazy and humid conditions
            are frequent. See Threlkeld and Jordan (1958) for recommended values.
            Typical values range from 0.95 to 1.05 and are usually never more than 1.2.
            Default is set to 1.0.
        timestep_: An integer representing the timestep with which to make the
            WEA object.  Default is set to 1 for 1 step per hour of the year.
    Returns:
        readMe!: Reports, errors, warnings, etc.
        wea: A wea object from stat file. This wea object represents an original 
            ASHRAE Clear Sky, which is intended to determine peak solar load and
            sizing parmeters for HVAC systems.
"""

ghenv.Component.Name = "HoneybeePlus_ClearSky"
ghenv.Component.NickName = 'ClearSky'
ghenv.Component.Message = 'VER 0.0.04\nMAY_14_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '02 :: Daylight :: Light Sources'
ghenv.Component.AdditionalHelpFromDocStrings = "0"

try:
    from ladybug.wea import Wea
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))

if _location:
    if timestep_ == None:
        timestep_ = 1
    if clearness_ == None:
        clearness_ = 1
    wea = Wea.ashrae_clear_sky(_location, clearness_, timestep_)