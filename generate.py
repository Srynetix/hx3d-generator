#!/usr/bin/env python3

#     Main generator program.
#     Using the Python library Colorama by Jonathan Hartley.
#
#     Copyright (C) 2015 Denis BOURGE
#
#     This library is free software; you can redistribute it and/or
#     modify it under the terms of the GNU Lesser General Public
#     License as published by the Free Software Foundation; either
#     version 2.1 of the License, or (at your option) any later version.
#
#     This library is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#     Lesser General Public License for more details.
#
#     You should have received a copy of the GNU Lesser General Public
#     License along with this library; if not, write to the Free Software
#     Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
#     USA

import argparse

import os
import re
import shutil

from config import config
from distutils.dir_util import copy_tree

from dependencies import colorama
from dependencies.colorama import Fore
from dependencies.colorama import Style

# UTILS ########################

def pprint(text, color=Fore.GREEN):
    print(Style.BRIGHT + color + text)

def execcommand(command):
    code = os.system(command)
    if code != 0:
        pprint("> Execute error.", Fore.RED)
        exit(code)

def explore_directory(directory):
    file_list = []
    folder_list = []

    for root, directories, files in os.walk(directory):
        for d in directories:
            filepath = os.path.join(root, d)
            folder_list.append(filepath)
        for filename in files:
            filepath = os.path.join(root, filename)
            file_list.append(filepath)

    return folder_list, file_list

def replace_content(content, conf):
    new_content = content
    for key, value in conf.items():
        occurences = re.findall(r"\<\#\[({})\]\#\>".format(key), new_content)
        if len(occurences) > 0:
            new_content = re.sub(r"\<\#\[({})\]\#\>".format(key), value, new_content)

    # Last check
    occurences = re.findall(r"\<\#\[(\w+)\]\#\>", new_content)
    if len(occurences) > 0:
        print()
        pprint("> /!\\ Error: variables remains.", Fore.RED)
        for oc in occurences:
            pprint("\t- Variable: {}".format(oc), Fore.RED)
        print()

    return new_content

# GENERATE PROJECT FROM TEMPLATE ###########################

def generate_template(conf):

    pprint("> Building new game `{}` in the folder `{}`.".format(conf["game_name"], conf["folder"]))

    # Template list
    folders, files = explore_directory("template/")
    new_folders = []
    new_files = []

    for f in files:
        new_file_name = replace_content(f, conf)
        new_files.append(re.sub(r"^template/", conf["folder"], new_file_name))

    for d in folders:
        new_dir_name = replace_content(d, config)
        new_folders.append(re.sub(r'^template/', conf["folder"], new_dir_name))

    # Folders copy
    print()
    pprint("> Creating folder structure")
    for i in range(len(new_folders)):
        old = folders[i]
        new = new_folders[i]

        if not os.path.exists(new):
            os.makedirs(new)

    # Files copy
    print()
    pprint("> Copying and templating files")
    for i in range(len(new_files)):
        old = files[i]
        new = new_files[i]

        # File replacement
        if not new.endswith(".png"):
            old_file = open(old, "r")
            old_file_content = old_file.read()

            with open(new, "w+") as new_file:
                print("{}".format(replace_content(old_file_content, config)), file=new_file)
        else:
            shutil.copy(old, new)

    pprint("> Done")

# GET THE ENGINE #########################

def create_project(conf):

    folder = conf["folder"]

    # Folder creation
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Framework check
    pprint("> Fetching the hx3d framework to `{}`.".format(folder))
    execcommand("git clone --depth=1 {} {}".format(conf["hx3d_repo"], folder))
    execcommand("cd {} && ./clone_dependencies.sh".format(folder))
    execcommand("rm -rf {}/.git".format(folder))

    # Generate template
    generate_template(conf)

# MAIN ###################################

def main():
    colorama.init(autoreset=True)
    print()

    parser = argparse.ArgumentParser(description='Generate a hx3d template')
    parser.add_argument('--new', nargs=3, metavar=("game", "destination", "package"), type=str, help='Generate a new game')
    args = parser.parse_args()

    if args.new:
        config["game_name"] = args.new[0]
        config["game_name_lower"] = args.new[0].lower()
        config["game_name_upper"] = args.new[0].upper()

        config["folder"] = args.new[1] + "/"
        config["android_package_name"] = args.new[2]

        create_project(config)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
