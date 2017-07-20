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
Read more about the parameters at: http://daysim.ning.com/
Here is my favorite presentation by John Mardaljevic: http://radiance-online.org/community/workshops/2011-berkeley-ca/presentations/day1/JM_AmbientCalculation.pdf

-

    Args:
        _quality_: 0 > low, 1 > Medium, 2 > High (default: 0).
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

ghenv.Component.Name = "Honeybee_Radiance Parameters Grid-based"
ghenv.Component.NickName = 'RADParGridBased'
ghenv.Component.Message = 'VER 0.0.02\nJUL_20_2017'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '03 :: Daylight :: Recipe'
ghenv.Component.AdditionalHelpFromDocStrings = "5"

try:
    import honeybee.radiance.recipe.parameters as param
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))
    

_quality_ = _quality_ or 0
_recipeType_ = _recipeType_ or 0

radPar, vmtxPar, dmtxPar, smtxPar = \
    param.getRadianceParametersGridBased(_quality_, _recipeType_)
    
if radOptPar_ and radPar:
    radPar.importParameterValuesFromString(radOptPar_)

if vmtxOptPar_ and vmtxPar:
    vmtxPar.importParameterValuesFromString(vmtxOptPar_)

if dmtxOptPar_ and dmtxPar:
    dmtxPar.importParameterValuesFromString(dmtxOptPar_)

if smtxOptPar_ and smtxPar:
    smtxPar.importParameterValuesFromString(smtxOptPar_)