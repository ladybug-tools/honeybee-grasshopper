# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Radiance Glass Material from Visible Transmitance

-

    Args:
        _name: Material name
        _t_vis_: Visible transmittance (0..1)
    Returns:
        material: Radiance glass material
"""

ghenv.Component.Name = "HoneybeePlus_Radiance Glass Material"
ghenv.Component.NickName = 'radGlassMat'
ghenv.Component.Message = 'VER 0.0.06\nJUL_07_2020'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '01 :: Daylight :: Materials'
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from honeybee_plus.radiance.material.glass import Glass
except ImportError as e:
    raise ImportError('\nFailed to import honeybee_plus:\n\t{}'.format(e))

if _name:
    _t_vis_ = 0.6 if _t_vis_ is None else _t_vis_
    material = Glass.by_single_trans_value(_name, _t_vis_)
