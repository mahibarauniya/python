################################################################################
# Author Name       : Mahendra Kumar Barauniya
# Reviewer Name     :
# Create Date       : 08/06/2022
# Last modifyDate   : 08/06/2022
# Usage             : Used to convert the xlxs file to any format dat, txt or csv and skip n number of records if applicable
#                   : we can also do separate fields using a single character delimiter
#                   : we can also enclosed the non-numeric fields with double quotes.
#Default Behaviour  : cntskipheader is 0 if not defined and outputformat is csv if not defined.
#                   : outputfilepath is not passed then file will get generated at same path where input file is available.
#Limitation         : "delimeter" must be a single character string.
#Input  file        : ./data/employee_list.xlsx
#Output file        : ./data/employee_list.dat,  ./data/employee_list.csv

#Call
#                   : cd <to the directory>
#
'''
python xlsxConverter.py \
--inputfilepath "D:\1.2-PYTHON\GIT-python\python\python_utilities\data"
--inputfilename="employee_list.xlsx"


python xlsxConverter.py \
--inputfilepath "D:\1.2-PYTHON\GIT-python\python\python_utilities\data"
--inputfilename="employee_list.xlsx"
--delimiter="|"

python xlsxConverter.py \
--inputfilepath "D:\1.2-PYTHON\GIT-python\python\python_utilities\data"
--inputfilename="employee_list.xlsx"
--delimiter="|"
--enclosedfields="Y"
--cntskipheader=1

python xlsxConverter.py \
--inputfilepath "D:\1.2-PYTHON\GIT-python\python\python_utilities\data"
--inputfilename="employee_list.xlsx"
--delimiter="~"
--enclosedfields="Y"
--cntskipheader=5
--outputformat="dat"
'''

################################################################################
import csv
import configparser
import argparse
import pandas as pd
import utils.customException as ce

# Always Append your project’s root directory to PYTHONPATH
# set PYTHONPATH=%PYTHONPATH%;D:\study\python\python_utilities\


import utils.loadLibrary as ll
import utils.logutils as lu

def main():
    try:
        parser =  argparse.ArgumentParser (description="utility for converting XLSX/XLX file to any format(csv, dat, txt) and by default is csv")
        parser.add_argument('--inputfilepath', dest='inputfilepath', required=True, help ='Directory for input file | REQUIRED')
        parser.add_argument('--inputfilename', dest='inputfilename', required=True, help ='File Name for input file | REQUIRED')
        parser.add_argument('--delimiter', dest='delimiter', default = ",", required=False, help ='any single character delimiter which will be used to seperated fields. By default is ,')
        parser.add_argument('--outputformat', dest='outputformat', default = "csv", required=False, choices=["txt", "dat", "csv"], help='Format of output files')
        parser.add_argument('--outputfilepath', dest='outputfilepath', required=False, help ='output file path where you want to generate the output files')
        parser.add_argument('--enclosedfields', dest='enclosedfields', default = 'N', type = str.upper, choices = ["Y", "N"], required=False, help ='pass: Y if you want non-numeric fields enclosed with double quotes')
        parser.add_argument('--cntskipheader', dest='cntskipheader', required=False, default = 0, help ='number of records to be skipped while converting the input file')

        args= parser.parse_args()

        ##config parser
        config = configparser.ConfigParser()
        config.read('./config/configDetails.conf')
        PASS_MSG = config.get("CONSTANT_VALUE", "PASS_MSG")
        RC_S     = config.get("CONSTANT_VALUE", "SCRIPT_FINAL_SUCCESS_RETURN_CODE")
        RC_F     = config.get("CONSTANT_VALUE", "SCRIPT_FINAL_FAIL_RETURN_CODE")

        file_with_path = args.inputfilepath + "/" + args.inputfilename

        ####### Basic Validation...
        lu.log_message("Validating Input Direcotry......", "INFO")
        ll.validate_directory(args.inputfilepath)
        ll.validate_file_available_at_directory(args.inputfilepath, args.inputfilename, PASS_MSG)
        lu.log_message("Input file: {} is going to convert to {} ......".format(file_with_path, args.outputformat), "INFO")


        ####### get file name from input file passed
        fileprefix = args.inputfilename.split(".")[0]

        outputfiledir = args.outputfilepath if args.outputfilepath else args.inputfilepath
        lu.log_message("Validating Output Directory......", "INFO")
        ll.validate_directory(outputfiledir)

        cntskipheader = args.cntskipheader if args.cntskipheader else 0
        cntskipheader = int(cntskipheader)



        outputfile = outputfiledir + "/" + fileprefix + "." + args.outputformat

        ##reading the excel file from input file path...
        df_inputfile = pd.read_excel (file_with_path, skiprows = cntskipheader)
        lu.log_message("delimiter {} is used while converting the input file ".format(args.delimiter), "INFO")

        print("outputfiledir is {} {} {}".format(outputfiledir, fileprefix, args.outputformat))

        if args.enclosedfields.upper() == "Y":
            df_inputfile.to_csv(outputfile, index = False, sep = args.delimiter, quoting = csv.QUOTE_NONNUMERIC)
        else:
            df_inputfile.to_csv(outputfile, index = False, sep = args.delimiter)

        print("Return code: {}".format(RC_S))

    except ce.DirectoryNotFound as e:
        lu.log_message(e.msg, "ERR")
        print("Return code: {}".format(RC_F))

    except ce.FileNotFound as e:
        lu.log_message(e.msg, "ERR")
        print("Return code: {}".format(RC_F))

    except Exception as e:
        lu.log_message("Unexpected eror.....{}".format(e), "ERR")
        print("Return code: {}".format(RC_F))

if __name__ == "__main__":
    main()