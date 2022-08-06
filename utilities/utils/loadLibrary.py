import os
import configparser

import logutils as lu
import customException as cm

config = configparser.ConfigParser()
config.read('./../config/configDetails.conf')


MSG_PASS = config.get("CONSTANT_VALUE","PASS_MSG")
MSG_FAIL = config.get("CONSTANT_VALUE","FAIL_MSG")

def validate_directory(dirpath):
    isDir = os.path.isdir(dirpath)
    if not isDir:
        raise cm.DirectoryNotFound("{}: Directory {} doesn't exist".format(MSG_FAIL, dirpath))
    else:
        lu.log_message("{} Directory exists: {} ".format(MSG_PASS, dirpath), "INFO")


def validate_file_available_at_directory(dirpath, filename, msg):
    filewithpath = dirpath + "/" + filename
    isFile = os.path.isfile(filewithpath)

    if not isFile:
        raise cm.FileNotFound("{}: File {} doesn't exist".format(MSG_FAIL, filewithpath))
    else:
        lu.log_message("{} File exists: {} ".format(MSG_PASS, filewithpath), "INFO")
