import inspect
import os
import subprocess

import utils.logutils as lu
from utils.loadLibrary import validate_directory, validate_file, createFolder

fileName = __file__  # or by using inspect module we can get file name #fileName = inspect.getfile(inspect.currentframe())


def gitDiffGenerator(objectGit, debugMode):

    lu.log_message_debug(debugMode, "Inside: {} and Function: {} - ...................".format( fileName,  inspect.currentframe().f_code.co_name ))

    validate_directory(debugMode, objectGit.tmpLocation)

    validate_file(debugMode, os.path.abspath(objectGit.yaml) )

    lu.log_message("Creating source and target folder at tmpLocation", "INFO")
    createFolder ( debugMode, objectGit.tmpLocation,  objectGit.source_repo_name + "_" + objectGit.source_branch_name )
    createFolder ( debugMode, objectGit.tmpLocation,  objectGit.target_repo_name + "_" + objectGit.target_branch_name )

    lu.log_message_debug("Cloning source and target repo in source and target folders", "INFO")

    gitClone( debugMode, objectGit.source_repo_url, objectGit.tmpLocation,  objectGit.source_repo_name + "_" + objectGit.source_branch_name , objectGit.source_branch_name)
    gitClone( debugMode, objectGit.target_repo_url, objectGit.tmpLocation,  objectGit.target_repo_name + "_" + objectGit.target_branch_name , objectGit.target_branch_name)




def gitClone(debugMode, source_repo_url, tmpLocation, foldername, gitBranchName):
    lu.log_message_debug(debugMode, "Inside: {} and Function: {} -  ...................".format(fileName, inspect.currentframe().f_code.co_name))
    try:
        p = subprocess.Popen(['git', 'clone', '--branch', gitBranchName, source_repo_url, tmpLocation + '\\' +  foldername ] , stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True )

    except Exception as e:
        raise Exception("error in git clone {}".format(e))



