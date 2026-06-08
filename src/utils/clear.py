from os import *
from sys import *
def clear():
    if name== 'nt':
        _=system('cls')
    else:
        _=system('clear')
def printline():
    print("########################################################################################")

def printfilename(s):
    print("######################",s,"###################################")    