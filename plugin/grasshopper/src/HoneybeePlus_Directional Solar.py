# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Evaluate unobstructed solar radiation on a surface facing any direction
at every timestep of a Wea.

-

    Args:
        _wea: A Honeybee Wea object.
        _alt_: A number between -90 and 90 that represents the altitude at which
            radiation is being evaluated in degrees.
            A value of 0 denotes a surface facing the horizon and a value of
            90 denotes a surface is facing straight up. Default is 90 for straight up.
        _az_: A number between 0 and 360 that represents the azimuth at which
            radiation is being evaluated in degrees.
            A value of 0 means North, 90 means East, 180 means South, and
            270 means West.  Default is 180 for south facing.
        _g_ref_: A number between 0 and 1 that represents the ground reflectance.
            Default is set to 0.2.
        iso_t_: Set to "True" to use an isotropic sky model, which assumes that
            diffuse radiation is evenly distributed across the sky and is 
            suitable for both cloudy and clear skies.  Set to "False" to use
            an anisotropic sky model, that places more diffuse radiation near
            the solar disc and is more accourate for clear skies but is not 
            suitable for cloudy skies.  The default is set to "True" of an 
            isotropic sky model.
    Returns:
        readMe!: Reports, errors, warnings, etc.
        total: A list of total solar irradiance at each timestep of the WEA.
        dir: A list of direct solar irradiance at each timestep of the WEA.
        diff: A list of diffuse solar irradiance at each timestep of the WEA.
        ref: A list of ground reflected solar irradiance at each
            timestep of the WEA.
"""

ghenv.Component.Name = "HoneybeePlus_Directional Solar"
ghenv.Component.NickName = 'directionSolar'
ghenv.Component.Message = 'VER 0.0.05\nJAN_24_2019'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '02 :: Daylight :: Light Sources'
ghenv.Component.AdditionalHelpFromDocStrings = "0"

if _wea is not None and hasattr(_wea, 'isWea'):
    # set defaults
    _alt_ = 90 if _alt_ is None else _alt_
    _az_ = 180 if _az_ is None else _az_
    _g_ref_ = 0.2 if _g_ref_ is None else _g_ref_
    iso_t_ = True if iso_t_ is None else iso_t_
    
    # compute solar on surface
    total, dir, diff, ref = \
        _wea.directional_irradiance(_alt_, _az_, _g_ref_, iso_t_)
