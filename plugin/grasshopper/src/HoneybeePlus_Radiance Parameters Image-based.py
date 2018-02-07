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
        _recipeType: 0 > Point-in-time, 1 > Daylight Coeff., 2 > 3Phase, 3 > 5Phase
        radOptPar_: Use this input to set other Radiance parameters as needed.
            You must follow Radiance's standard syntax (e.g. -ps 1 -lw 0.01)
        vmtxOptPar_: Use this input to set other Radiance parameters for view matrix
            calculation as needed. You must follow Radiance's standard syntax
            (e.g. -ps 1 -lw 0.01).
        dmtxOptPar_: Use this input to set other Radiance parameters for daylight
            matrix calculation as needed. You must follow Radiance's standard syntax
            (e.g. -ps 1 -lw 0.01).
        smtxOptPar_: Use this input to set other Radiance parameters for sun
            matrix calculation as needed. You must follow Radiance's standard syntax
            (e.g. -ps 1 -lw 0.01).
    Returns:
        radPar: Radiance parameters.
        vmtxPar: Radiance parameters for view matrix calculation.
        dmtxPar: Radiance parameters for daylight matrix calculation.
        smtxPar: Radiance parameters for direct sun matrix calculation.
"""

ghenv.Component.Name = "HoneybeePlus_Radiance Parameters Image-based"
ghenv.Component.NickName = 'RADParImageBased'
ghenv.Component.Message = 'VER 0.0.04\nFEB_07_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '03 :: Daylight :: Recipe'
ghenv.Component.AdditionalHelpFromDocStrings = "5"

try:
    from honeybee.radiance.recipe import parameters as param
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))
    

_complexity_ = _complexity_ or 0
_recipeType_ = _recipeType_ or 0

radPar, vmtxPar, dmtxPar, smtxPar = \
    param.get_radiance_parameters_image_based(_complexity_, _recipeType_)
    
if radOptPar_ and radPar:
    radPar.import_parameter_values_from_string(radOptPar_)

if vmtxOptPar_ and vmtxPar:
    vmtxPar.import_parameter_values_from_string(vmtxOptPar_)

if dmtxOptPar_ and dmtxPar:
    dmtxPar.import_parameter_values_from_string(dmtxOptPar_)

if smtxOptPar_ and smtxPar:
    smtxPar.import_parameter_values_from_string(smtxOptPar_)    