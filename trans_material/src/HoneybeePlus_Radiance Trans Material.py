# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Radiance Trans Material

-

    Args:
        _name: Material name
        _r_reflectance_:Reflectance for red. The value should be between 0 and 1 (Default: 0)
        _g_reflectance_:Reflectance for green . The value should be between 0 and 1 (Default: 0)
        _b_reflectance_:Reflectance for blue. The value should be between 0 and 1 (Default: 0)
        _reflected_spacularity_:Fraction of reflected spacular. The reflected specularity of common uncoated glass is around .06, Matte = min 0, Satin = suggested max 0.07 (Default: 0).
        _roughness_: Roughness is specified as the rms slope of surface facets. A value of 0 corresponds to a perfectly smooth surface, and a value of 1 would be a very rough surface. Roughness values greater than 0.2 are not very realistic. (Default: 0).
        _transmitted_diff_:The transmitted diffuse component is the fraction of transmitted light that is transmitted diffusely in as scattering fashion.
        _transmitted_spec_:The transmitted specular component is the fraction of transmitted light that is not diffusely scattered.
        _modifier_:Material modifier (Default: void).
    Returns:
        readMe!: Reports, errors, warnings, etc.
        material: Radiance trans material
"""

ghenv.Component.Name = "HoneybeePlus_Radiance Trans Material"
ghenv.Component.NickName = 'radTransMaterial'
ghenv.Component.Message = 'VER 0.0.05\nAUG_14_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '01 :: Daylight :: Materials'
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from honeybee.radiance.material.trans import Trans
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))

if _name:
    name = _name
    r_reflectance = 0 if _r_reflectance_ is None else _r_reflectance_
    g_reflectance = 0 if _g_reflectance_ is None else _g_reflectance_
    b_reflectance = 0 if _b_reflectance_ is None else _b_reflectance_
    reflected_spacularity = 0.5 if _reflected_spacularity_ is None else _reflected_spacularity_
    roughness = 0 if _roughness_ is None else _roughness_
    transmitted_diff = 0.5 if _transmitted_diff_ is None else _transmitted_diff_
    transmitted_spec = 0.5 if _transmitted_spec_ is None else _transmitted_spec_
    modifier = _modifier_ or "void"
    material = Trans.from_reflected_spacularity(name, r_reflectance, g_reflectance, b_reflectance, reflected_spacularity, roughness, transmitted_diff, transmitted_spec, modifier)
