# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Compute the sunobstructed olar radiation facing any direction at
each timestep of a Wea.


The calculation method of this component is faster than running a full Ladybug
Solar Radiation Analysis but this comes at the cost of not being able to account
for obstructions that block the sun.
-

    Args:
        _wea = A Honeybeeplus WEA object.
        _alt_: A number between -90 and 90 that represents the
            altitude at which radiation is being evaluated in degrees.
            A value of 0 denotes a surface facing the horizon and a value of
            90 denotes a surface is facing straight up.
            Default is 90 for straight up.
        _az_: A number between 0 and 360 that represents the
            azimuth at wich radiation is being evaluated in degrees.
            A value of 0 means North, 90 means East, 180 means South, and
            270 means West.  Default is 180 for south facing.
        _gRef_: A number between 0 and 1 that represents the ground reflectance.
            Default is set to 0.2.
        isoT_: Set to "True" to use an isotropic sky model, which assumes that
            diffuse radiation is evenly distributed across the sky and is 
            suitable for both cloudy and clear skies.  Set to "False" to use
            an anisotropic sky model, that places more diffuse radiation near
            the solar disc and is more accourate for clear skies but is not 
            suitable for cloudy skies.  The default is set to "True" of an 
            isotropic sky model.
    Returns:
        readMe!: Reports, errors, warnings, etc.
        total: A list of total solar radiation at each timestep of the WEA.
        dir: A list of direct solar radiation at each timestep of the WEA.
        diff: A list of diffuse solar radiation at each timestep of the WEA.
        ref: A list of ground reflected solar radiation at each
            timestep of the WEA.
"""

ghenv.Component.Name = "HoneybeePlus_Directional Solar"
ghenv.Component.NickName = 'DirectionSolar'
ghenv.Component.Message = 'VER 0.0.04\nJUL_10_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '02 :: Daylight :: Light Sources'
ghenv.Component.AdditionalHelpFromDocStrings = "0"

if _wea is not None and hasattr(_wea, 'isWea'):
    # set defaults
    if _alt_ is None:
        _alt_ = 90
    if _az_ is None:
        _az_ = 180
    if _gRef_ is None:
        _gRef_ = 0.2
    if isoT_ is None:
        isoT_ = True
    
    # compute solar on surface
    total, dir, diff, ref = \
        _wea.directional_radiation(_alt_, _az_, _gRef_, isoT_)
    
    # convert to float values
    total = [float(x) for x in total]
    dir = [float(x) for x in dir]
    diff = [float(x) for x in diff]
    ref = [float(x) for x in ref]

