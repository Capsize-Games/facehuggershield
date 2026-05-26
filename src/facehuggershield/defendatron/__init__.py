import logging
from typing import Optional

import facehuggershield.shadowlogger
import facehuggershield.darklock
import facehuggershield.nullscream
from facehuggershield.defendatron.nullscream_tracker import (
    NullscreamTracker,
)


nullscream_tracker = NullscreamTracker()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def activate(
    # Nullscream properties
    nullscream_blacklist: Optional[list[str]] = None,
    nullscream_whitelist: Optional[list[str]] = None,
    nullscream_function_blacklist: Optional[list[str]] = None,
    # darklock properties
    darklock_os_whitelisted_operations: Optional[list[str]] = None,
    darklock_os_whitelisted_filenames: Optional[list[str]] = None,
    darklock_os_whitelisted_modules: Optional[list[str]] = None,
    darklock_os_whitelisted_directories: Optional[list[str]] = None,
    darklock_os_allow_network: bool = False,
    darklock_allowed_network_port: Optional[int] = None,
    activate_shadowlogger: bool = False,
    activate_darklock: bool = False,
    activate_nullscream: bool = False,
    # Shadowlogger properties
    show_stdout: bool = True,
):
    logger.info("Activating defendatron")
    if activate_shadowlogger:
        logger.info("Activating shadowlogger")
        facehuggershield.shadowlogger.manager.activate(
            show_stdout=show_stdout,
            trackers=[nullscream_tracker],
        )

    if activate_darklock:
        logger.info("Activating darklock")
        facehuggershield.darklock.activate(
            whitelisted_modules=darklock_os_whitelisted_modules,
            allow_network=darklock_os_allow_network,
            whitelisted_directories=darklock_os_whitelisted_directories,
            allowed_network_port=darklock_allowed_network_port,
        )

    if activate_nullscream:
        logger.info("Activating nullscream")
        facehuggershield.nullscream.activate(
            blacklist=nullscream_blacklist,
            whitelist=nullscream_whitelist,
            function_blacklist=nullscream_function_blacklist,
        )


def deactivate(
    # Nullscream properties
    nullscream_blacklist: Optional[list[str]] = None,
):
    facehuggershield.shadowlogger.manager.deactivate()
    facehuggershield.darklock.manager.deactivate()
    facehuggershield.nullscream.manager.deactivate(
        blacklist=nullscream_blacklist,
    )
