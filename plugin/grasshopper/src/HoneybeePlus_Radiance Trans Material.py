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
        _r_ref_: Reflectance for red. The value should be between 0 and 1
        _g_ref_: Reflectance for green . The value should be between 0 and 1.
        _b_ref_: Reflectance for blue. The value should be between 0 and 1.
        _spec_ref_: Reflected Spacularity.  This is the fraction of reflected light
            that is specular. The reflected specularity of common uncoated
            glass is around .06, Matte = suggested min 0,
            Satin = suggested max 0.07 (Default: 0). Specularity fractions
            greater than 0.1 are not realistic (Default: 0).
        _rough_: Roughness is specified as the rms slope of surface facets.
            A value of 0 corresponds to a perfectly smooth surface, and a 
            value of 1 would be a very rough surface. Roughness values 
            greater than 0.2 are not very realistic. (Default: 0).
        _diff_trans_: The transmitted diffuse component. This is the fraction of transmitted
            light that is transmitted diffusely in as scattering fashion.
        _spec_trans_: The transmitted specular component. This is the fraction of transmitted 
            light that is not diffusely scattered.
        _modifier_: Material modifier (Default: void).
    Returns:
        material: Radiance trans material
"""

ghenv.Component.Name = "HoneybeePlus_Radiance Trans Material"
ghenv.Component.NickName = 'radTransMat'
ghenv.Component.Message = 'VER 0.0.06\nJUL_07_2020'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '01 :: Daylight :: Materials'
ghenv.Component.AdditionalHelpFromDocStrings = "2"

try:
    from honeybee_plus.radiance.material.trans import Trans
except ImportError as e:
    raise ImportError('\nFailed to import honeybee_plus:\n\t{}'.format(e))

if _name:
    name = _name
    r_ref = 0.35 if _r_ref_ is None else _r_ref_
    g_ref = 0.35 if _g_ref_ is None else _g_ref_
    b_ref = 0.35 if _b_ref_ is None else _b_ref_
    ref_spacularity = 0 if _spec_ref_ is None else _spec_ref_
    roughness = 0 if _rough_ is None else _rough_
    diff_trans = 0.15 if _diff_trans_ is None else _diff_trans_
    spec_trans = 0.15 if _spec_trans_ is None else _spec_trans_
    modifier = _modifier_ or "void"
    material = Trans.from_reflected_spacularity(name, r_ref, g_ref, b_ref,
                                                ref_spacularity, roughness,
                                                diff_trans, spec_trans, modifier)
