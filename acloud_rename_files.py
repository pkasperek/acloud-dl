#!/usr/bin/python3
# -*- coding: utf-8 -*-
# pylint: disable=E,C,W,R
import argparse
import os
import sys


def find_files(path, old_extension, new_extension):
    if path is None or old_extension is None or new_extension is None:
        ret_val = {"status": "False", "msg": "One of required parameters is None"}
        return ret_val

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".{}".format(old_extension)):
                file_path = os.path.join(root, file)
                print("Renaming file: {}".format(file_path))
                file_name, ext = os.path.splitext(file_path)
                os.rename(file_path, "{0}.{1}".format(file_name, new_extension))
                print("Renamed file: {0}.{1}".format(file_name, new_extension))

    ret_val = {"status": "True", "msg": "Finish renaming files extensions"}
    return ret_val


def main():
    description = 'A cross-platform python based utility to rename video extensions from .VIDEO_AUDIO to custom extension.'
    parser = argparse.ArgumentParser(description=description, conflict_handler="resolve")
    general = parser.add_argument_group("General")
    general.add_argument(
        '-h', '--help',
        action='help',
        help="Shows the help.")

    advance = parser.add_argument_group("Advance")
    advance.add_argument(
        '-f', '--folder',
        dest='folder',
        type=str,
        help="Select parent folder of VIDEO/AUDIO files.", metavar='')
    advance.add_argument(
        '-o', '--old-extension',
        dest='old_extension',
        type=str,
        help="Rename course lecture video/audio files extension to defined by user.")
    advance.add_argument(
        '-n', '--new-extension',
        dest='new_extension',
        type=str,
        help="Rename course lecture video/audio files extension to defined by user.")

    options = parser.parse_args()

    ret_val = None
    try:
        ret_val = find_files(options.folder, options.old_extension, options.new_extension)
    except Exception as e:
        ret_val = {"status": "False", "msg": "Exception : %s" % e}

    if ret_val is not None:
        print(f"Result of function is {ret_val.values['status']}, with message {ret_val.values['msg']}")

    sys.exit(0)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
