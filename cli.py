# standard imports
import argparse


def cli():
    """ Defines and parses the command line arguments.

    Parameters:
        None

    Returns:
        args (obj): parsed arguments.
    """

    # create parser
    parser = argparse.ArgumentParser(
        description="Monitor service port migration."
    )

    # define arguments
    parser.add_argument("old",
                        action="store",
                        help="old service port number")
    parser.add_argument("new",
                        action="store",
                        help="new service port number")
    parser.add_argument("hosts",
                        action="store",
                        help="path to hosts file")
    parser.add_argument("-v", "--version",
                        action="version",
                        version="0.0.1",
                        help="display the version")

    # parse arguments
    args = parser.parse_args()

    return args
