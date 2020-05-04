import os
import time

def printbychar(files):
    bannerStr = ''
    for filename in files:
        bannerStr += "\n"
        banner = open(filename, 'r')
        for line in banner:
            for character in line:
                time.sleep(0.003)
                os.system("clear")
                bannerStr += character
                print(bannerStr)

def printbyline(filename):
    bannerStr = ''
    bannerStr += "\n"
    banner = open(filename, 'r')
    for line in banner:
        time.sleep(0.1)
        os.system("clear")
        bannerStr += line
        print(bannerStr)       


