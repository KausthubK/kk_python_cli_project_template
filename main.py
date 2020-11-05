#!/usr/bin/env python3
__version__ = 'v0.0.0'
__author__ = 'Kausthub Krishnamurthy'

""" System Imports """
from os.path import join, expanduser, splitext, basename
import sys
from datetime import datetime as dt

""" Common Library Imports """
import argparse


""" Local Imports """


########################################################################################################################

#  ##     ##       ###       ####    ##    ##
#  ###   ###      ## ##       ##     ###   ##
#  #### ####     ##   ##      ##     ####  ##
#  ## ### ##    ##     ##     ##     ## ## ##
#  ##     ##    #########     ##     ##  ####
#  ##     ##    ##     ##     ##     ##   ###
#  ##     ##    ##     ##    ####    ##    ##

########################################################################################################################

def main(arguments):
    args = parse_args(arguments)
    print("Input: " + str(args.input))
    print("Output: " + str(args.output))
    return 0

########################################################################################################################

#  ##          ####    ########
#  ##           ##     ##     ##
#  ##           ##     ##     ##
#  ##           ##     ########
#  ##           ##     ##     ##
#  ##           ##     ##     ##
#  ########    ####    ########

########################################################################################################################


def helper_function() -> None:
    return


def _private_helper_function() -> None:
    return

########################################################################################################################

#   ######     ##          ####
#  ##    ##    ##           ##
#  ##          ##           ##
#  ##          ##           ##
#  ##          ##           ##
#  ##    ##    ##           ##
#   ######     ########    ####

########################################################################################################################

def parse_args(argv) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", help="debug output", action='store_true', default=False)
    parser.add_argument("-i", "--input", help="input", required=True)
    parser.add_argument("-o", "--output", help="path to output directory",
                        default=join(expanduser("~"), 'out', 'python_project_template',
                                     format(int(dt.timestamp(dt.now()) * 1000))))
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version " + __version__ + ") by " + __author__)
    args = parser.parse_args(argv[1:])
    return args


""" main trigger """
if __name__ == '__main__':
    main(sys.argv)
