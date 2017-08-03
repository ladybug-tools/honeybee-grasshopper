# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Radiance BSDF Material

-

    Args:
        _xmlfile: Path to an xml file. Data will not be cached in memory.
        _upOrientation_: (x, y ,z) vector that sets the hemisphere that the
            BSDF material faces.  For materials that are symmetrical about
            the HBSrf plane (like non-angled venitian blinds), this can be
            any vector that is not perfectly normal to the HBSrf. For
            asymmetrical materials like angled veneitan blinds, this variable
            should be coordinated with the direction the HBSrfs are facing.
            The default is set to (0.01, 0.01, 1.00), which should hopefully
            not be perpendicular to any typical HBSrf.
        _upVector_: Optional number to set the thickness of the BSDF material.
            (default: 0)
    Returns:
        readMe!: Reports, errors, warnings, etc.
        material: Radiance BSDF material
"""

ghenv.Component.Name = "HoneybeePlus_Radiance BSDF Material"
ghenv.Component.NickName = 'BSDFMaterial'
ghenv.Component.Message = 'VER 0.0.03\nAUG_04_2017'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '01 :: Daylight :: Materials'
ghenv.Component.AdditionalHelpFromDocStrings = "2"

try:
    from honeybee.radiance.material.bsdf import BSDFMaterial
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))

if _xmlfile:
    material = BSDFMaterial(_xmlfile, _upVector_, thickness_)
