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

def nukedir(target_dir, rmdir=False):
    """Delete all the files inside target_dir.

    This function has been copied from ladybug.futil.
    """
    d = os.path.normpath(target_dir)
    if not os.path.isdir(d):
        return

    files = os.listdir(d)
    for f in files:
        if f == '.' or f == '..':
            continue
        path = os.path.join(d, f)
        if os.path.isdir(path):
            nukedir(path)
        else:
            try:
                os.remove(path)
            except Exception:
                print("Failed to remove %s" % path)

    if rmdir:
        try:
            os.rmdir(d)
        except Exception:
            try:
                dir_util.remove_tree(d)
            except Exception:
                print("Failed to remove %s" % d)


def copy_file_tree(source_folder, dest_folder, overwrite=True):
    """Copy an entire file tree from a source_folder to a dest_folder.

    Args:
        source_folder: The source folder containing the files and folders to
            be copied.
        dest_folder: The destination folder into which all the files and folders
            of the source_folder will be copied.
        overwrite: Boolean to note whether an existing folder with the same
            name as the source_folder in the dest_folder directory should be
            overwritten. Default: True.
    """
    # make the dest_folder if it does not exist
    if not os.path.isdir(dest_folder):
        os.mkdir(dest_folder)

    # recursively copy each sub-folder and file
    for f in os.listdir(source_folder):
        # get the source and destination file paths
        src_file_path = os.path.join(source_folder, f)
        dst_file_path = os.path.join(dest_folder, f)

        # if overwrite is True, delete any existing files
        if overwrite:
            if os.path.isfile(dst_file_path):
                try:
                    os.remove(dst_file_path)
                except Exception:
                    raise IOError("Failed to remove %s" % f)
            elif os.path.isdir(dst_file_path):
                nukedir(dst_file_path, True)

        # copy the files and folders to their correct location
        if os.path.isfile(src_file_path):
            shutil.copyfile(src_file_path, dst_file_path)
        elif os.path.isdir(src_file_path):
            if not os.path.isdir(dst_file_path):
                os.mkdir(dst_file_path)
            copy_file_tree(src_file_path, dst_file_path, overwrite)

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
        uo_folds = ('honeybee',)
    else:
        repos = lb_repos + hb_repos
        uo_folds = ('ladybug', 'honeybee')
    
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
            sourceFolder = os.path.join(targetDirectory, r"{}-master".format(f), 'honeybee_plus')
            libFolder = os.path.join(targetDirectory, 'honeybee_plus')
        else:
            sourceFolder = os.path.join(targetDirectory, r"{}-master".format(f), f.replace('-', '_')) \
                if f != 'honeybee' else os.path.join(targetDirectory, r"{}-master".format(f), 'honeybee_plus')
            libFolder = os.path.join(targetDirectory, f.replace('-', '_')) \
                if f != 'honeybee' else os.path.join(targetDirectory, 'honeybee_plus')
        if not os.path.isdir(libFolder):
            os.mkdir(libFolder)
        print 'Copying {} source code to {}'.format(f, libFolder)
        copy_file_tree(sourceFolder, libFolder)
    
    # copy user-objects
    uofolder = UserObjectFolders[0]

    for pl in uo_folds:
        if pl == 'ladybug':
            userObjectsFolder = os.path.join(
                targetDirectory,
                r"{}-grasshopper-master/ladybug_grasshopper/user_objects".format(pl))
        else:
            userObjectsFolder = os.path.join(
                targetDirectory,
                r"{}-grasshopper-master/plugin/grasshopper/userObjects".format(pl))
        
        if pl == 'ladybug':
            plus_uofolder = os.path.join(uofolder, 'ladybug_grasshopper', 'user_objects')
        else:
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