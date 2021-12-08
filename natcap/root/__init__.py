import logging

import pkg_resources

LOGGER = logging.getLogger('natcap.root')
LOGGER.addHandler(logging.NullHandler())

try:
    # __version__ = pkg_resources.get_distribution(__name__).version
    __version__ = 's.0.1'
except pkg_resources.DistributionNotFound:
    # package is not installed.  Log the exception for debugging.
    LOGGER.exception('Could not load natcap.root version information')
