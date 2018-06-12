# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Compute the solar radiation falling on an unobstructed surface that faces any
direction at each timestep of a Wea.


The calculation method of this component is faster than running a full Ladybug
Solar Radiation Analysis but this comes at the cost of not being able to account
for obstructions that block the sun.
-

    Args:
        _wea = A Honeybeeplus WEA object.
        _sAlt_: A number between -90 and 90 that represents the altitude that a 
            surface is facing in degrees.  A value of 0 means the surface is 
            facing the horizon and a value of 90 means a surface is facing 
            straight up.  Default is 90 for a surface facing straight up.
        _sAz_: A number between 0 and 360 that represents the azimuth that a 
            surface is facing in degrees.  A value of 0 means North, 90 means 
            East, 180 means South, and 270 means West.  Default is 180 for a 
            south facing window.
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
        srfTotal: A list of total solar radiation on the surface at each 
            timestep of the WEA.
        srfDir: A list of direct solar radiation on the surface at each 
            timestep of the WEA.
         srfDiff: A list of diffuse sky solar radiation on the surface at each 
            timestep of the WEA.
         srfRef: A list of ground reflected solar radiation on the surface at
            each timestep of the WEA.
"""

ghenv.Component.Name = "HoneybeePlus_Solar On Surface"
ghenv.Component.NickName = 'SolarOnSrf'
ghenv.Component.Message = 'VER 0.0.04\nJUN_11_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '02 :: Daylight :: Light Sources'
ghenv.Component.AdditionalHelpFromDocStrings = "0"

if _wea is not None and hasattr(_wea, 'isWea'):
    # set defaults
    if _sAlt_ is None:
        _sAlt_ = 90
    if _sAz_ is None:
        _sAz_ = 180
    if _gRef_ is None:
        _gRef_ = 0.2
    if isoT_ is None:
        isoT_ = True
    
    # compute solar on surface
    srfTotal, srfDir, srfDiff, srfRef = \
        _wea.radiation_on_surface(_sAlt_, _sAz_, _gRef_, isoT_)
    
    # convert to float values
    srfTotal = [float(x) for x in srfTotal]
    srfDir = [float(x) for x in srfDir]
    srfDiff = [float(x) for x in srfDiff]
    srfRef = [float(x) for x in srfRef]

