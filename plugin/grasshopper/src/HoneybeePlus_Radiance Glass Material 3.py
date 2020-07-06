# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Radiance Glass Material from visible transmitance for red, green and blue

-

    Args:
        _name: Material name.
        _r_vis_: Visible transmittance for red channel (0..1).
        _g_vis_: Visible transmittance for green channel (0..1).
        _b_vis_: Visible transmittance for blue channel (0..1).
    Returns:
        material: Radiance glass material.
"""

ghenv.Component.Name = "HoneybeePlus_Radiance Glass Material 3"
ghenv.Component.NickName = 'radGlassMat3'
ghenv.Component.Message = 'VER 0.0.06\nJUL_07_2020'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '01 :: Daylight :: Materials'
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from honeybee_plus.radiance.material.glass import Glass
except ImportError as e:
    raise ImportError('\nFailed to import honeybee_plus:\n\t{}'.format(e))

if _name:
    _r_vis_ = 0.6 if _r_vis_ is None else _r_vis_
    _g_vis_ = 0.6 if _g_vis_ is None else _g_vis_
    _b_vis_ = 0.6 if _b_vis_ is None else _b_vis_
    material = Glass(_name, _r_vis_, _g_vis_, _b_vis_)
