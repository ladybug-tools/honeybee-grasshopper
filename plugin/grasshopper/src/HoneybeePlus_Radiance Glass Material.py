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
        _tVis_: Visible transmittance (0..1)
    Returns:
        readMe!: Reports, errors, warnings, etc.
        material: Radiance glass material
"""

ghenv.Component.Name = "HoneybeePlus_Radiance Glass Material"
ghenv.Component.NickName = 'radGlassMaterial'
ghenv.Component.Message = 'VER 0.0.05\nMAY_14_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '01 :: Daylight :: Materials'
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from honeybee.radiance.material.glass import Glass
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))

if _name:
    _tVis_ = _tVis_ or 0.6
    material = Glass.by_single_trans_value(_name, _tVis_)
