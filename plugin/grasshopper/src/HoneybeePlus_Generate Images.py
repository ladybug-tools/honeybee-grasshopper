# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Hourly results for a sensor for several hours during the year.

-

    Args:
        _img_collection: An imgage collection from the results of an image-based
            study.
        hoys_: An optional list of hours for hours of the year if you don't want
            the analysis to be calculated for all the hours.
        blind_states_: A list of blind states for light sources as tuples for
            hours of the year. You can use Dynamic Blinds Schedule component
            to generate this schedule. If left empty the first state of each
            window group will be used.
        _mode_: An integer between 0-3.
            0 returns the combined image of the sources with total - direct + sun values
            1 returns the combined image of the sources with total values
            2 returns the combined image of the sources with direct values
            3 returns the combined image of the sources with sun values
    Returns:
        report: Reports, errors, warnings, etc.
        values: List of values for hours of the year.
"""

ghenv.Component.Name = "HoneybeePlus_Generate Images"
ghenv.Component.NickName = 'genImages'
ghenv.Component.Message = 'VER 0.0.06\nJUL_07_2020'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '04 :: Daylight :: Daylight'
ghenv.Component.AdditionalHelpFromDocStrings = "4"

if _img_collection:
    _modes = ('combined', 'total', 'direct', 'diffuse')
    _mode_ = _mode_ or 0
    hoys_ = hoys_ or _img_collection.hoys

    assert _mode_ < 4, \
        '_mode_ can only be 0: combined, 1: total, 2: direct or 3: sky.'

    states = _img_collection.parse_blind_states(blind_states_)
    
    print(_img_collection.details)
    print('Loading {} values for several hours.'.format(_modes[_mode_]))
    
    images = _img_collection.generate_combined_images_by_id(hoys_, states, _mode_) 