# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
This component downloads honeybee libraries from github to:
C:\Users\%USERNAME%\AppData\Roaming\McNeel\Rhinoceros\5.0\scripts
OR
C:\Users\%USERNAME%\AppData\Roaming\McNeel\Rhinoceros\6.0\scripts

-

    Args:
        _update!: Set to True to install honeybee[+] (and ladybug) on your machine.
    Returns:
        Vviiiiiiiiiizzz!: !!!
"""

ghenv.Component.Name = "HoneybeePlus Installer"
ghenv.Component.NickName = "HBInstaller"
ghenv.Component.Message = 'VER 0.0.06\nJUL_07_2020'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = "05 :: Developers"
ghenv.Component.AdditionalHelpFromDocStrings = "1"

import os
import System
import sys
import zipfile
import shutil
import distutils
from distutils import dir_util
from Grasshopper.Folders import UserObjectFolders
System.Net.ServicePointManager.SecurityProtocol = System.Net.SecurityProtocolType.Tls12

def copy_tree_full(sourceFolder, libFolder):
    for file in os.listdir(sourceFolder):
        src_file_path = os.path.join(sourceFolder, file)
        dst_file_path = os.path.join(libFolder, file)
        if os.path.isfile(src_file_path):
            shutil.copyfile(src_file_path, dst_file_path)
        elif os.path.isdir(src_file_path):
            if not os.path.isdir(dst_file_path):
                os.mkdir(dst_file_path)
            copy_tree_full(src_file_path, dst_file_path)

def updateHoneybee():
    
    """
    This code will download honeybee and honeybee[+] library from github and
    update the current installation.
    """
    lb_repos = ['ladybug', 'ladybug-geometry', 'ladybug-rhino',
                'ladybug-comfort', 'ladybug-grasshopper']
    hb_repos = ['honeybee', 'honeybee-grasshopper']
    home_folder = os.getenv('HOME') or os.path.expanduser('~')
    lb_install = os.path.join(home_folder, 'ladybug_tools', 'python', 'Lib', 'site-packages')
    if lb_install in sys.path:
        repos = hb_repos
    else:
        repos = lb_repos + hb_repos
    
    try:
        targetDirectory = [p for p in sys.path if p.find('scripts')!= -1][0]
    except IndexError:  # there is no scripts in path try to find plugins folder
        try:
            targetDirectory = [p for p in sys.path if p.find(r'settings\lib')!= -1][0]
        except IndexError:
            try:  # we might be on a Mac
                targetDirectory = [p for p in sys.path if p.find(r'Lib')!= -1][0]
            except IndexError:
                raise IOError(
                    'Failed to find a shared path in sys.path to install honeybee.\n' \
                     'Make sure Grasshopper is installed correctly!')
    
    # delete current folders 
    for f in repos:
        libFolder = os.path.join(targetDirectory, f.replace('-', '_')) \
            if f != 'honeybee' else os.path.join(targetDirectory, 'honeybee_plus')
        if os.path.isdir(libFolder):
            try:
                print 'removing {}'.format(libFolder)
                dir_util.remove_tree(libFolder)
            except:
                print 'Failed to remove {}.'.format(libFolder)

    # download files
    for repo in repos:
        url = "https://github.com/ladybug-tools/%s/archive/master.zip" % repo
        # download the zip file
        print "Downloading {} the github repository to {}".format(repo, targetDirectory)
        zipFile = os.path.join(targetDirectory, '%s.zip' % repo)
        
        try:
            client = System.Net.WebClient()
            client.DownloadFile(url, zipFile)
        except Exception, e:
            msg = `e` + "\nDownload failed! Try to download and unzip the file manually form:\n" + url
            raise Exception(msg)
        
        #unzip the file
        with zipfile.ZipFile(zipFile) as zf:
            for f in zf.namelist():
                if f.endswith('/'):
                    try:
                        os.makedirs(f)
                    except:
                        pass
                else:
                    zf.extract(f, targetDirectory)
        zf.close()
        try:
            os.remove(zipFile)
        except:
            print 'Failed to remove downloaded zip file.'
    
    # copy files to folder.
    for f in repos:
        if f.endswith('honeybee-grasshopper'):
            sourceFolder = os.path.join(targetDirectory, r"{}-master".format(f), f.split('-')[0])
            libFolder = os.path.join(targetDirectory, 'honeybee_plus')
        else:
            sourceFolder = os.path.join(targetDirectory, r"{}-master".format(f), f.replace('-', '_'))
            libFolder = os.path.join(targetDirectory, f.replace('-', '_')) \
                if f != 'honeybee' else os.path.join(targetDirectory, 'honeybee_plus')
        if not os.path.isdir(libFolder):
            os.mkdir(libFolder)
        print 'Copying {} source code to {}'.format(f, libFolder)
        copy_tree_full(sourceFolder, libFolder)
    
    # copy user-objects
    uofolder = UserObjectFolders[0]

    for pl in ('ladybug', 'honeybee'):
        if pl == 'ladybug':
            userObjectsFolder = os.path.join(
                targetDirectory,
                r"{}-grasshopper-master/ladybug_grasshopper/user_objects".format(pl))
        else:
            userObjectsFolder = os.path.join(
                targetDirectory,
                r"{}-grasshopper-master/plugin/grasshopper/userObjects".format(pl))
    
        plus_uofolder = os.path.join(uofolder, '{}Plus'.format(pl.capitalize()))
        if not os.path.isdir(plus_uofolder):
            os.mkdir(plus_uofolder)
    
        print 'Removing {}[+] userobjects.'.format(pl, uofolder)
    
        # remove older userobjects
        for f in os.listdir(uofolder):
            if os.path.isdir(os.path.join(uofolder, f)):
                continue
            if f.startswith('{}Plus'.format(pl.capitalize())):
                try:
                    os.remove(os.path.join(uofolder, f))
                except:
                    print('Failed to remove {}'.format(os.path.join(uofolder, f)))
        for f in os.listdir(plus_uofolder):
            if f.startswith('{}Plus'.format(pl.capitalize())):
                try:
                    os.remove(os.path.join(plus_uofolder, f))
                except:
                    print('Failed to remove {}'.format(os.path.join(plus_uofolder, f)))
                    
        print 'Copying {}[+] userobjects to {}.'.format(pl, uofolder)
    
        for f in os.listdir(userObjectsFolder):
            shutil.copyfile(os.path.join(userObjectsFolder, f),
                            os.path.join(plus_uofolder, f))

    # try to clean up
    for r in repos:
        try:
            shutil.rmtree(os.path.join(targetDirectory, '{}-master'.format(r)))
        except:
            print 'Failed to delete donloaded libraries.'

if _update:
    try:
        updateHoneybee()
    except ImportError as e:
        raise Exception("Failed to update honeybee[+]:\n{}".format(e))
    else:
        try:
            import honeybee_plus
        except ImportError as e:
            raise ImportError('Failed to import honeybee[+]:\n{}'.format(e))
        else:
            print "\n\nImported honeybee[+] from {}\nVviiiizzzz...".format(honeybee_plus.__file__)
            print "Restart Grasshopper and Rhino to load the new library."
else:
    print 'Set update to True to update ladybug[+] and honeybee[+]!'