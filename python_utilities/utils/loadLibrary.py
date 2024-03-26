import os
import configparser
import inspect
import subprocess


import utils.logutils as lu
import utils.customException as cm


fileName = __file__  # or by using inspect module we can get file name #fileName = inspect.getfile(inspect.currentframe())

config = configparser.ConfigParser()
path_current_directory = os.path.dirname(__file__)

path_parent_directory=os.path.abspath(os.path.join(path_current_directory, '..'))

#config.read(os.path.join(path_current_directory, 'conf', 'config.cfg')
configPath= os.path.join(path_parent_directory, 'config', 'configDetails.conf')

config.read(configPath)


MSG_PASS = config.get("CONSTANT_VALUE","PASS_MSG")
MSG_FAIL = config.get("CONSTANT_VALUE","FAIL_MSG")

def validate_directory(debugMode, dirpath):
    try:
        isDir = os.path.isdir(dirpath)
        if not isDir:
            raise cm.DirectoryNotFound
        else:
            lu.log_message_debug(debugMode, "{} Directory exists: {} ".format(MSG_PASS, dirpath))
    except Exception as e:
        raise cm.DirectoryNotFound("{}: Directory {} doesn't exist".format(MSG_FAIL, dirpath))




def validate_file(debugMode, filepath):
    try:
        isFileAvailable = os.path.exists(filepath)
        if not isFileAvailable:
            raise cm.FileNotFound
        else:
            lu.log_message_debug(debugMode, "{} File exists: {} ".format(MSG_PASS, filepath))
    except Exception as e:
        raise cm.FileNotFound("{}: File {} doesn't exist and error is {}".format(MSG_FAIL, filepath, e))



def validate_file_available_at_directory(dirpath, filename, msg):
    try:
        filewithpath = dirpath + "/" + filename
        isFile = os.path.isfile(filewithpath)

        if not isFile:
            raise cm.FileNotFound
        else:
            lu.log_message("{} File exists: {} ".format(MSG_PASS, filewithpath), "INFO")
    except Exception as e:
        raise cm.FileNotFound("{}: File {} doesn't exist".format(MSG_FAIL, filewithpath))




def createFolder(debugMode, folderpath, newfoldername):
    lu.log_message_debug(debugMode, "Inside: {} and Function: {} - ...................".format(fileName,
                                                                                                   inspect.currentframe().f_code.co_name))

    lu.log_message_debug( debugMode, "Checking if folder already exist or not. and if Exists then delete it first" )

    try:
        folder_with_path = folderpath + "\\" + newfoldername
        cmd = 'mkdir ' + folder_with_path

        delete_folder_if_exists( debugMode, folder_with_path )

        p = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True)
        stdout, stderr = p.communicate()
        returncode = p.returncode

        if returncode != 0:
            raise cm.DeleteFolderException

    #except cm.DeleteFolderException as e:
    #raise cm.DeleteFolderException("Error while deleting a folder and  storerr is {} and error is {}".format(stderr, e))

    except Exception as e:
        raise cm.CreateFolderException("Error while deleting/creating a folder and error is {}".format(  e ))



def delete_folder_if_exists(debugMode, folder):
    try:
        lu.log_message_debug(debugMode, "Inside: {} and Function: {} - ...................".format(fileName,
                                                                                                   inspect.currentframe().f_code.co_name))

        if os.path.isdir(folder):
            cmd2 =  'rmdir ' +  folder

            p = subprocess.Popen(['cmd', '/c', 'rmdir', '/s', '/q', folder], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            stdout, stderr = p.communicate()
            returncode = p.returncode

            if returncode != 0:
                raise cm.DeleteFolderException("Error Occurred... while deleting this folder {} ".format(folder))


    except Exception as e:
        raise cm.DeleteFolderException("Error while deleting a folder and  err is {}".format(e))