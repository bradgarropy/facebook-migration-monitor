# standard imports
import logging
import sys


def configure(level=logging.INFO):
    """ Configures logging for this module.

    Parameters:
        level (int): log level.

    Returns:
        None
    """

    # establish logger
    logger = logging.getLogger()

    # disable propagation
    logger.propagate = False

    # set log level
    logger.setLevel(level)

    # remove any existing handlers
    logger.handlers = []

    # create handlers
    stdout, stderr = handlers()

    # add handlers
    logger.addHandler(stdout)
    logger.addHandler(stderr)

    return


def handlers():
    """ Configures logging handlers for this module.

    Parameters:
        None

    Returns:
        stdout (obj): standard out handler.
        stderr (obj): standard error handler.
    """

    # stdout
    stdout = logging.StreamHandler(stream=sys.stdout)
    stdout.setFormatter(logging.Formatter('%(message)s'))
    stdout.addFilter(LTEFilter(logging.WARNING))

    # stderr
    stderr = logging.StreamHandler(stream=sys.stderr)
    stderr.setFormatter(logging.Formatter('%(message)s'))
    stderr.addFilter(GTEFilter(logging.ERROR))

    return stdout, stderr


class LTEFilter(logging.Filter):

    def __init__(self, level):
        super(LTEFilter, self).__init__()
        self.level = level

    def filter(self, record):
        """ Logs records which are less than or equal to level.
        Parameters:
            record (obj): log message.
        Returns:
            log (bool): True if message should be logged, False otherwise.
        """

        return record.levelno <= self.level


class GTEFilter(logging.Filter):

    def __init__(self, level):
        super(GTEFilter, self).__init__()
        self.level = level

    def filter(self, record):
        """ Logs records which are greater than or equal to level.
        Parameters:
            record (obj): log message.
        Returns:
            log (bool): True if message should be logged, False otherwise.
        """

        return record.levelno >= self.level
