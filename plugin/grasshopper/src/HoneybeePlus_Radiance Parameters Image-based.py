# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>


"""
Radiance parameters library for analysis recipes.

Check here for more details: http://radsite.lbl.gov/radiance/refer/Notes/rpict_options.html
Here is my favorite presentation by John Mardaljevic: http://radiance-online.org/community/workshops/2011-berkeley-ca/presentations/day1/JM_AmbientCalculation.pdf

-

    Args:
        _complexity_: 0 > low, 1 > Medium, 2 > High
        _recipe_type: 0 > Point-in-time, 1 > Daylight Coeff., 2 > 3Phase, 3 > 5Phase
        rad_opt_par_: Use this input to set other Radiance parameters as needed.
            You must follow Radiance's standard syntax (e.g. -ps 1 -lw 0.01)
        vmtx_opt_par_: Use this input to set other Radiance parameters for view matrix
            calculation as needed. You must follow Radiance's standard syntax
            (e.g. -ps 1 -lw 0.01).
        dmtx_opt_par_: Use this input to set other Radiance parameters for daylight
            matrix calculation as needed. You must follow Radiance's standard syntax
            (e.g. -ps 1 -lw 0.01).
        smtx_opt_par_: Use this input to set other Radiance parameters for sun
            matrix calculation as needed. You must follow Radiance's standard syntax
            (e.g. -ps 1 -lw 0.01).
    Returns:
        rad_par: Radiance parameters.
        vmtx_par: Radiance parameters for view matrix calculation.
        dmtx_par: Radiance parameters for daylight matrix calculation.
        smtx_par: Radiance parameters for direct sun matrix calculation.
"""

ghenv.Component.Name = "HoneybeePlus_Radiance Parameters Image-based"
ghenv.Component.NickName = 'RADParImageBased'
ghenv.Component.Message = 'VER 0.0.06\nJUL_07_2020'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '03 :: Daylight :: Recipe'
ghenv.Component.AdditionalHelpFromDocStrings = "5"

try:
    from honeybee_plus.radiance.recipe import parameters as param
except ImportError as e:
    raise ImportError('\nFailed to import honeybee_plus:\n\t{}'.format(e))
    

_complexity_ = _complexity_ or 0
_recipe_type_ = _recipe_type_ or 0

rad_par, vmtx_par, dmtx_par, smtx_par = \
    param.get_radiance_parameters_image_based(_complexity_, _recipe_type_)
    
if rad_opt_par_ and rad_par:
    rad_par.import_parameter_values_from_string(rad_opt_par_)

if vmtx_opt_par_ and vmtx_par:
    vmtx_par.import_parameter_values_from_string(vmtx_opt_par_)

if dmtx_opt_par_ and dmtx_par:
    dmtx_par.import_parameter_values_from_string(dmtx_opt_par_)

if smtx_opt_par_ and smtx_par:
    smtx_par.import_parameter_values_from_string(smtx_opt_par_)    