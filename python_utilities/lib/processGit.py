import inspect
import os, stat
import subprocess
import shutil
import filecmp

import utils.logutils as lu
from utils.loadLibrary import validate_directory, validate_file, createFolder

fileName = __file__  # or by using inspect module we can get file name #fileName = inspect.getfile(inspect.currentframe())


def gitProcess(objectGit, debugMode):

    lu.log_message_debug(debugMode, "Inside: {} and Function: {} - ...................".format( fileName,  inspect.currentframe().f_code.co_name ))

    validate_directory(debugMode, objectGit.tmpLocation)
    validate_file(debugMode, os.path.abspath(objectGit.yaml) )

    lu.log_message("Creating source and target folder at tmpLocation", "INFO")
    source_folder_name = objectGit.source_repo_name + "_" + objectGit.source_branch_name
    createFolder(debugMode, objectGit.tmpLocation, source_folder_name)
    lu.log_message("Cloning source git repo and deleting folders and files from mentioned yaml files", "INFO")
    gitClone(debugMode, objectGit.source_repo_url, objectGit.tmpLocation, source_folder_name, objectGit.source_branch_name)
    delete_folders_from_repo(debugMode, objectGit.tmpLocation, objectGit.source_folder_to_include, source_folder_name)
    delete_files_from_repo(debugMode, objectGit.tmpLocation, objectGit.source_files_to_exclude, source_folder_name)

    lu.log_message("Cloning target git repo and deleting folders and files from mentioned yaml files", "INFO")
    target_folder_name = objectGit.target_repo_name + "_" + objectGit.target_branch_name
    createFolder ( debugMode, objectGit.tmpLocation,  target_folder_name )
    gitClone(debugMode, objectGit.target_repo_url, objectGit.tmpLocation, target_folder_name, objectGit.target_branch_name)
    delete_folders_from_repo(debugMode, objectGit.tmpLocation, objectGit.target_folder_to_include, target_folder_name)
    delete_files_from_repo(debugMode, objectGit.tmpLocation, objectGit.target_files_to_exclude, target_folder_name)


def gitClone(debugMode, source_repo_url, tmpLocation, foldername, gitBranchName):
    try:
        p = subprocess.Popen(['git', 'clone', '--branch', gitBranchName,  source_repo_url, tmpLocation + '\\' +  foldername ] , stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True )
        stdout, stderr = p.communicate()
        returncode = p.returncode

        # if returncode != 0:
        #     raise Exception("Error Occurred in gitClone...")

    except Exception as e:
        raise Exception("error in git clone {}".format(e))


def delete_folders_from_repo(debugMode, tmpLocation, source_folder_to_include, source_folder_name):
    lu.log_message_debug(debugMode, "Inside: {} and Function: {} - ...................".format( fileName,  inspect.currentframe().f_code.co_name ))

    root_directory = tmpLocation + '\\' + source_folder_name
    #print(root_directory)
    #print(source_folder_to_include)
    try:
        for root, dirs, files in os.walk(root_directory):
            for dirname in dirs:
                dir_full_path = os.path.join(root, dirname)
                dir_path = dir_full_path.replace(root_directory, "").strip()
                dir_path = dir_path[1:] if dir_path.strip().startswith("\\") else dir_path  ## removing \ from the path if that \ has it's first character
                dir_path = dir_path[0:-1] if dir_path.strip().endswith("\\") else dir_path  ## removing \ from the path if that \ has it's last  character
                if dir_path not in source_folder_to_include:
                    delete_path =  os.path.join(root_directory, dirname)
                    shutil.rmtree(delete_path, ignore_errors=False, onerror=remove_readonly)  ## if shutil.rmtree is giving error because of read only file then we change the stat of the file on error
                    lu.log_message_debug(debugMode, "Folder {} deleted successfully.".format(delete_path))
    except Exception as e:
        raise Exception("error occured in non_delete_folders_from_repo {}".format(e))

def remove_readonly(func, path, _):
    os.chmod(path, stat.S_IWRITE)
    func(path)


def delete_files_from_repo(debugMode, tmpLocation, source_files_to_exclude, source_folder_name):
    lu.log_message_debug(debugMode, "Inside: {} and Function: {} - ...................".format(fileName,
                                                                                               inspect.currentframe().f_code.co_name))
    root_directory = tmpLocation + '\\' + source_folder_name
    try:
        for i in range(len(source_files_to_exclude)):
            os.remove(os.path.join(root_directory, source_files_to_exclude[i]))
            lu.log_message_debug(debugMode, "File {} deleted successfully.".format(source_files_to_exclude[i]))

    except Exception as e:
        raise Exception("error occured in delete_files_from_repo and error is: {}".format(e))


def runCompare( debugMode, tmpLocation, reposource, repotarget, objectGit ):
    lu.log_message_debug(debugMode, "Inside: {} and Function: {} - ...................".format(fileName, inspect.currentframe().f_code.co_name))


    depth_of_source_path = get_max_depth_of_directory(reposource)
    depth_of_target_path = get_max_depth_of_directory(repotarget)

    lu.log_message_debug(debugMode, "reposource is {} and depth is {} ".format(reposource, depth_of_source_path))
    lu.log_message_debug(debugMode, "repotarget is {} and depth is {} ".format(repotarget, depth_of_target_path))

    max_depth = max(depth_of_source_path, depth_of_target_path)
    gitDiffFile = tmpLocation + "\gitDiffFile.dat"
    lu.log_message("gitDiffFile is {} and available at {}".format(gitDiffFile, tmpLocation), "INFO")

    f = open (gitDiffFile, "w")
    compare_report_recusively(debugMode, objectGit,  max_depth, reposource, repotarget, f)
    f.close()
    return gitDiffFile


def get_max_depth_of_directory( directory ):
    max_cnt = 0
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                full_file_path = os.path.join(root, file)
                lu.log_message("full_file_path is {}".format(full_file_path), "INFO")
                cnt = full_file_path.count("\\")
                max_cnt  = max(cnt, max_cnt )
        return max_cnt
    except Exception as e:
        raise Exception("error occured in get_max_depth_of_directory and error is: {}".format(e))


def compare_report_recusively(debugMode, objectGit, max_depth, reposource, repotarget, file, i=0):
    lu.log_message_debug(debugMode, "Inside: {} and Function: {} - ...................".format(fileName,
                                                                                               inspect.currentframe().f_code.co_name))


    try:
        dircmp = filecmp.dircmp(reposource, repotarget)

        for name in dircmp.diff_files:
            file.write("Mismatch| " + name + "|" + dircmp.left + "|" + dircmp.right + "\n" )

        for name in dircmp.left_only:
            file.write("Exist only in " + objectGit.source_repo_name +"_"+ objectGit.source_branch_name + "|" + name + "|" + dircmp.left + "|\n")

        for name in dircmp.right_only:
            file.write("Exist only in " + objectGit.target_repo_name +"_"+ objectGit.target_branch_name + "|" + name + "|" + "" + "|" + dircmp.right + "\n")

        for sub_dcmp in dircmp.subdirs.values():
            if i <= max_depth:
                i = i + 1
            else:
                break

            compare_report_recusively(debugMode, objectGit, max_depth, os.path.join(reposource, sub_dcmp.left), os.path.join(repotarget, sub_dcmp.right), file)


    except Exception as e:
        raise Exception("error occured in compare_report_recusively and error is: {}".format(e))