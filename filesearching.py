# Regex  -> Searching , Sending

import os
import re
import shutil
import sys
from time import sleep
from pprint import pprint

found_files = []
found_paths = []
# == Searching files (extension based) with os.walk()


def waiting():
    sys.stdout.write("\r")
    sys.stdout.write(" \t\t --> Processing is on the way <-- ")
    sys.stdout.flush()


def shutil_send(source):
    try:
        shutil.copy(source, os.path.join(os.getcwd(), "found_files"))
    except PermissionError:
        pass


def searching_files():
    ret = 0
    ignore_list = [
        "/home/hi-man/python/pyproject",
        "/home/hi-man/logs",
        "/home/hi-man/Templates",
        "/home/hi-man/Desktop",
    ]
    regex_pattern = re.compile(f"(.*?)[.]*{sys.argv[1]}$", re.I)
    path = input("\n Tell me the path ('/home/user-name/path) : ")
    print("\n")
    if os.path.exists(path) is not True:
        raise Exception(" Sorry Wrong Path ")
    for i, j, k in os.walk(path):
        if i in ignore_list:
            j[:] = []
            k[:] = []
        for every_k in k:
            check = re.search(regex_pattern, every_k)
            waiting()
            if check is not None:
                found_files.append(check.group())
                found_paths.append(os.path.join(i, check.group()))
            continue
    sys.stdout.write("\r \t\t --> Hurray! Searching Completed  <--\n")
    sleep(1)
    if found_files:
        ret = 1
    return ret


def sending_files(send_choice):
    if not (os.path.exists(os.path.abspath("./found_files"))):
        print("\n Create a Directory -> found_files")
        os.mkdir("found_files")
    pass

    if send_choice == "yes":
        result_file = open(os.path.abspath("./found_files/CHECK_PATHS.txt"), "w")
        for every_path in found_paths:
            try:
                result_file.write(every_path + "\n")
                shutil_send(every_path)
                waiting()
            except shutil.SameFileError:
                print(" Actually there was same files ")
                break
        sys.stdout.write("\r \t\t--> Hurray! Sending Complete <--\n")
    else:
        print(" --- Sending Cancelled ---")

    # == Show the files at terminal


def show_terminal(choice):
    if choice == "names":
        for every_file in found_files:
            pprint(f" {found_files.index(every_file)} -> {every_file}")
    elif choice == "paths":
        for every_path in found_paths:
            pprint(f" {found_paths.index(every_path)} -> {every_path}")
    else:
        print(" I'm not a stupid like you ")
