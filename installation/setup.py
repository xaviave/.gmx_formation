#!/usr/bin/env python3
import os
import sys


def add_right():
    try:
        file = os.path.join("~", ".gmx_formation", "gmx_correct_me", "correct_me.py")
        os.system(f"chmod +x {file}")
    except FileNotFoundError as e:
        print("Error while changing right, execute 'sudo python3 setup.py'")
        sys.exit(-1)


def add_alias():
    alias = 'alias gmx_correct_me="python3 ~/.gmx_formation/gmx_correct_me/correct_me.py"\n'
    try:
        file = os.path.abspath("../.zshrc")
        with open(file, "r+") as f:
            data = f.readlines()
            if not (alias is data):
                f.write(alias)
    except FileNotFoundError as e:
        print(
            "'.zshrc' is not found, maybe zsh is not install, run 'sudo apt install zsh', oh-my-zsh is adviced too"
        )


def create_workspace():
    os.system("cd ~/ && mkdir -p gmx_formation/part1 && mkdir -p gmx_formation/part2")
    os.system("cp .gmx_formation/sources/Part_1.md gmx_formation/part1")
    os.system("cp .gmx_formation/sources/Part_2.md gmx_formation/part2")


def setup():
    add_right()
    add_alias()
    create_workspace()


if "__main__" == __name__:
    setup()