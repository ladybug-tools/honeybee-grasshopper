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
        _rVis_: Visible transmittance for red channel (0..1).
        _gVis_: Visible transmittance for green channel (0..1).
        _bVis_: Visible transmittance for blue channel (0..1).
    Returns:
        readMe!: Reports, errors, warnings, etc.
        material: Radiance glass material.
"""

ghenv.Component.Name = "HoneybeePlus_Radiance Glass Material 3"
ghenv.Component.NickName = 'radGlassMaterial3'
ghenv.Component.Message = 'VER 0.0.04\nFEB_07_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '01 :: Daylight :: Materials'
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from honeybee.radiance.material.glass import GlassMaterial
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))

if _name:
    _rVis_ = _rVis_ or 0.6
    _gVis_ = _gVis_ or 0.6
    _bVis_ = _bVis_ or 0.6
    material = GlassMaterial(_name, _rVis_, _gVis_, _bVis_)
