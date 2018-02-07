# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Convert hdr files to tiff files.

-

    Args:
        _hdrs: A list of hdr files.
        _convert: Set to True to start the converting process.
    Returns:
        tiff: List of full path to output tiff images.
"""

ghenv.Component.Name = "HoneybeePlus_HDR to Tiff"
ghenv.Component.NickName = 'hdr2tiff'
ghenv.Component.Message = 'VER 0.0.04\nFEB_07_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '04 :: Daylight :: Daylight'
ghenv.Component.AdditionalHelpFromDocStrings = "5"

try:
    from honeybee.radiance.command.raTiff import RaTiff
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))

if _convert:
    tiff = []
    for fp in _hdrs:
        output = fp[:-4] + '.tiff'
        RaTiff(fp, output).execute()
        tiff.append(output)