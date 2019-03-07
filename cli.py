# standard imports
import argparse
import logging
import logger

# custom imports
import fmm


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


def main():
    """ Main method.

    Parameters:
        None

    Returns:
        None
    """

    # configure logging
    logger.configure()

    # cli arguments
    args = cli()

    # run migration monitor
    fmm.monitor(args.old, args.new, args.hosts)

    return


if __name__ == "__main__":

    main()
