""" Regex  -> Searching , Sending """

import os
import re
import shutil
import sys
from time import sleep

FOUND_FILES = []
FOUND_PATHS = []

# == Searching files (extension based) with os.walk()


def waiting():
    """ waiting message """
    sys.stdout.write("\r")
    sys.stdout.write(" \t\t --> Processing is on the way <-- ")
    sys.stdout.flush()


def shutil_send(source):
    """ shutil copy function """
    try:
        shutil.copy(source, os.path.join(os.getcwd(), "FOUND_FILES"))
    except PermissionError:
        pass


def searching_files():
    """ Search files using os.walk() """
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
                FOUND_FILES.append(check.group())
                FOUND_PATHS.append(os.path.join(i, check.group()))
            continue
    sys.stdout.write("\r \t\t --> Hurray! Searching Completed  <--\n")
    sleep(1)
    if FOUND_FILES:
        ret = 1
    return ret


def sending_files(send_choice):
    """ Directory creation and send files """
    if not os.path.exists(os.path.abspath("./FOUND_FILES")):
        print("\n Creating Directory -> FOUND_FILES")
        os.mkdir("FOUND_FILES")
    #pass

    if send_choice == "yes":
        result_file = open(os.path.abspath("./FOUND_FILES/CHECK_PATHS.txt"), "w")
        for every_path in FOUND_PATHS:
            try:
                result_file.write(every_path + "\n")
                shutil_send(every_path)
                waiting()
            except shutil.SameFileError:
                print("\n\n \t\t --> Same File Occur <--\n")
                break
        sys.stdout.write("\r \t\t--> Hurray! Sending Complete <--\n")
    else:
        print(" --- Sending Cancelled ---")


def show_terminal(choice):
    """ print message on the terminal """
    if choice == "names":
        for every_file in FOUND_FILES:
            print(f" {FOUND_FILES.index(every_file)} -> {every_file} ")
    elif choice == "paths":
        for every_path in FOUND_PATHS:
            print(f" {FOUND_PATHS.index(every_path)} \
    -> {every_path} -> {os.path.getsize(every_path)}")
    else:
        print(" I'm not a stupid like you ")
