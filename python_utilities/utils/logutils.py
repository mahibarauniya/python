################################################################################
# Author Name    : Mahendra Kumar Barauniya
# Create Date    : 08/06/2022
# Last modifyDate: 08/06/2022
# Usage          : Logging utility for python script in any project..

################################################################################
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(filename)s - %(levelname)s -%(message)s',
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger  = logging.getLogger(__name__)
console = logging.StreamHandler()
console.setLevel(logging.ERROR)

def log_message(msg, type = "INFO"):
    if type == "INFO":
        logger.info(msg)
    elif type == "WARN":
        logger.warning(msg)
    elif type == "ERR":
        logger.error(msg)
    elif type == "CRIT":
        logger.critical(msg)
    else:
        logger.info(msg)