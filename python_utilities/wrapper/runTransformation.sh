#!/bin/bash
##############################################################################################################################################################
### Author : Mahendra Barauniya
### Date   : 2023-11-29
### Details: This is wrapper file for running the transformation logic for multiple products
### Operating System: Windows
### Prerequisite: install python and WSL Windows subsystem for Linux(ubuntu) in windows machine and run the command from ubuntu command prompt
### command to run
#            clear; bash runTransformation.sh -e dev
##############################################################################################################################################################

### first loading the unix library functions
. ./../utils/loadLibrary.sh

SCRIPT_NAME=`basename $0`
DETAIL="SCRIPT is being used as wrapper and we need to pass mandatory fields  -e{env}  -d{date}  -n{modelname}"

while getopts ":e:d:n:" opt
do
  case "$opt" in
    e) env="$OPTARG";;
    d) date="$OPTARG";;
    n) modelname="$OPTARG";;
   \?) logMsg ${SCRIPT_NAME} e "${DETAIL}"
        return 1;;
  esac
done


if ! [[ ${env} =~ ^("dev"|"qa"|"prod")$ ]]
then
  logMsg ${SCRIPT_NAME} e "env should be dev|qa|prod"
  exit
else
  logMsg ${SCRIPT_NAME} i "Input paramter env is ${env}"
fi

if [[ -z ${modelname} ]]
then
  logMsg ${SCRIPT_NAME} e "-n parameter can't be blank. Please pass modelname with -n"
  exit
else
  logMsg ${SCRIPT_NAME} i "Input paramter modelname is ${modelname}"
fi

if [[ -z ${date} ]]
then
  date=$(date '+%Y%m%d')
fi
logMsg ${SCRIPT_NAME} i "date parameter set to ${date}"




#set the PYTHONPATH and mention the location from where you're running the project /d/python/python_utilities/
# In below case project is running from window machine after ubuntu installation and from d drive python folder
export PYTHONPATH=$PATH:/mnt/d/python/python_utilities/
python3 /mnt/d/python/python_utilities/scripts/runTransformation.py ${modelname} ${cob} ${mode}
