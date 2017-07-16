# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Radiance Opaque Material from Single Reflectance Value

-

    Args:
        _name: Material name
        _rRef_: Diffuse reflectance for red channel
        _gRef_: Diffuse reflectance for green channel
        _bRef_: Diffuse reflectance for blue channel
        _spec_: Specularity values above 0.1 are uncommon
        _rough_: Roughness values above 0.2 are uncommon
    Returns:
        readMe!: Reports, errors, warnings, etc.
        material: Radiance opaque material
"""

ghenv.Component.Name = "HoneybeePlus_Radiance Opaque Material 3"
ghenv.Component.NickName = 'radOpaqueMaterial3'
ghenv.Component.Message = 'VER 0.0.01\nJUL_15_2017'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '01 :: Daylight :: Materials'
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from honeybee.radiance.material.plastic import PlasticMaterial
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))

if _name:
    _rRef_ = _rRef_ or 0.35
    _gRef_ = _gRef_ or 0.35
    _bRef_ = _bRef_ or 0.35
    material = PlasticMaterial(_name, _rRef_, _gRef_, _bRef_, _spec_, _rough_)