#!/usr/bin/env python

import argparse
import helloworld


def parse_command_line():
    " parses args for the helloworld.py funtions"

    # init parser and add arguments
    parser = argparse.ArgumentParser()

    # add short args
    parser.add_argument(
        "-n", "--name",
        help="optional name to say hello to",
        type=str)

    parser.add_argument(
        "--popcorn",
        help="prints movie if popcorn is true",
        action="store_true")

    parser.add_argument(
        "--countdown",
        help="prints showtime, otherwise prints get popcorn",
        type=int)

    # parse args
    args = parser.parse_args()
    return args


def main():
    " run helloworld on parsed args"
    args = parse_command_line()
    helloworld.helloworld(
        popcorn=args.popcorn,
        countdown=args.countdown)
