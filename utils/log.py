"""Logging module"""

import logging

from colorlog import ColoredFormatter

LOG_LEVEL = logging.DEBUG
LOGFORMAT = (
    "  %(log_color)s%(levelname)-8s%(reset)s |"
    " %(log_color)s%(message)s%(reset)s"
)
logging.root.setLevel(LOG_LEVEL)
logging.addLevelName(logging.INFO, "INFO")
formatter = ColoredFormatter(LOGFORMAT)
formatter.log_colors = {
    "DEBUG": "white",
    "INFO": "light_green",
    "WARNING": "light_yellow",
    "ERROR": "light_red",
    "CRITICAL": "bold_red",
}
stream = logging.StreamHandler()
stream.setLevel(LOG_LEVEL)
stream.setFormatter(formatter)
log = logging.getLogger("-THIS-")
log.setLevel(LOG_LEVEL)
log.addHandler(stream)
