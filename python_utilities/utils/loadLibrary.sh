SCRIPT_NAME=`basename $0`

logMsg(){

    RED='\033[0;31m'
    YELLOW='\033[0;33m'
    GREEN='\033[0;37m'

    script=$1
    case $2 in

        e) type=ERR
           COLOR=${RED};;
        w) type=WARN
           COLOR=${YELLOW};;
        i) type=INFO
           COLOR=${GREEN};;
        \?) type=OTHER;;
    esac

    msg=$3

    echo -e "${COLOR}[${script}][$(date '+%Y-%m-%d %H:%M:%S')]:: ${msg}"
}
