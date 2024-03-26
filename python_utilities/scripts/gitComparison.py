########################################################################################################################
#Author Name: Mahendra Barauniya
#Date: 03/15/2024
#Usage: Used to compare two git repositories
#Call-
# --product="RETAIL" --yaml .\..\config\gitrepo.yaml  --tmpLocation D:\gitrepository\tmp\ --debug
# --product="RETAIL" --yaml .\..\config\gitrepo.yaml  --tmpLocation D:\gitrepository\tmp
########################################################################################################################


import sys


#set the project root as what we set export PYTHONPATH in Unix....
sys.path.append('D:\gitrepository\python\python_utilities')
sys.path.remove('D:\gitrepository\datatransformation')
#print(sys.path)

import utils.logutils as lu
import argparse
from lib.GitConfig import GitConfig
import lib.processGit as pg
import utils.customException as cm


def main():
    try:
        parser = argparse.ArgumentParser( description="Utility to compare branches of two git repositories" )
        #group = parser.add_mutually_exclusive_group()

        parser.add_argument('--product'      , required= True, choices = ["RETAIL", "MORTGAGE"], help="product from yaml file which has git repositories details")
        parser.add_argument('--yaml'         , required= False, dest =  'yaml',                                       help="yaml file which has all the details for git repositories")
        parser.add_argument('--tmpLocation'  , required= False, dest =  'tmpLocation',                                help="tmpLocation  for git repositories")
        parser.add_argument('--debug', action='store_true',  help='--debug mode pass it if you want to debug the code')

        args = parser.parse_args()
        lu.log_message("****************** Start: gitComparison:: program starts from here ****************** ", "INFO")

        obj_gitConfig = GitConfig( args.product, args.yaml, args.tmpLocation, args.debug )

        obj_gitConfig.initialize_variable()

        pg.gitProcess ( obj_gitConfig, args.debug )

        reposource = args.tmpLocation + "\\" + obj_gitConfig.source_repo_name + "_" + obj_gitConfig.source_branch_name
        repotarget = args.tmpLocation + "\\" + obj_gitConfig.target_repo_name + "_" + obj_gitConfig.target_branch_name

        diffFile = pg.runCompare ( args.debug, args.tmpLocation, reposource,  repotarget, obj_gitConfig )

    except Exception as e:
        lu.log_message("Error processing Git Comparison Utility !! {}".format(e))
        sys.exit(1)


if __name__ == "__main__":
    main()
