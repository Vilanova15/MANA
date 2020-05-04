import os
import time
import platform

def printbychar(files):
    bannerStr = ''
    for filename in files:
        bannerStr += "\n"
        banner = open(filename, 'r')
        for line in banner:
            for character in line:
                time.sleep(0.003)
                clear()
                bannerStr += character
                print(bannerStr)

def printbyline(filename):
    bannerStr = ''
    bannerStr += "\n"
    banner = open(filename, 'r')
    for line in banner:
        time.sleep(0.1)
        clear()
        bannerStr += line
        print(bannerStr)       


def clear():
    system_os = platform.system()
    if system_os == "Linux":
        os.system("clear")
    elif system_os == "Windows":
        os.system("cls")
    else:
        print("ARE YOU USING MAC????")
        raise UnsupportedOsException

class UnsupportedOsException(Exception):
    pass