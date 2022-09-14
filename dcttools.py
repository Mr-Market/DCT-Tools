#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys 
import getopt
import shutil

VERSION = "1.0.1"

class colors:

    #BLUE = '\033[94m'
    RED = '\033[31m'
    #FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def logo():
    print(colors.RED + colors.BOLD)
    print("""

  _____   _____ _______ _              _     
 |  __ \ / ____|__   __| |            | |    
 | |  | | |       | |  | |_ ___   ___ | |___ 
 | |  | | |       | |  | __/ _ \ / _ \| / __|
 | |__| | |____   | |  | || (_) | (_) | \__ 
 |_____/ \_____|  |_|   \__\___/ \___/|_|___/

{V} - https://github.com/Mr-Market/DCT-Tools

    """.format(V=VERSION))
    print(colors.ENDC)

def usage():
    logo()
    print("""
    DCTtools usage:
    -i    --input       Open Input.txt
    -o    --output      Open Output.txt
    -a    --uaadd       Add Slashes To a List of UA's
    -r    --uarem       Remove Slashes From a List of UA's
    -h    --help        Show Help & Exit
    """)
    sys.exit()


def truncate(file):
    """
        Truncate a file so it's empty on the next script run.
    """
    f = open(file, 'w') 
    f.close()

def open_files():
    """
        Open needed files
    """
    inputfile = open('input.txt', 'r')
    output = open('output.txt', 'w')
    
def close_files():
    """
        Close opened files
    """
    inputfile.close()
    output.close()

def ua_list_add_slashes():
    """
        Description: Take a list of dct unit addresses and add slashes.
        Example: 0000439530485103 -> 000-04395-30485-103

        How To Use:
        1. Place your list of DCT Unit Addresses without hyphens into the input.txt file
        2. Run the script using "-a" or "--uaadd" option
        3. See on screen or in output.txt for the list of Unit addresses with the hyphens added
    """
    inputfile = open('input.txt', 'r')
    output = open('output.txt', 'w')

    #Process
    for ua in inputfile.read().splitlines(): #read records and remove newlines
        ua = ua[0: 3] + "-" + ua[3:8] + "-" + ua[8:13] + "-" + ua[13:16] # Add Hyphens
        print (ua) 
        output.write(ua+"\n") #Write results to output.txt

    #Close files
    inputfile.close()
    output.close()

    #Truncate input file
    truncate("input.txt")

def ua_list_remove_slashes():
    """
        Description: Take a list of dct unit addresses and remove all slashes
        Example: 000-04395-30485-103 -> 0000439530485103


        How To Use:
        1. Place your list of DCT Unit Addresses with hyhens into the input.txt file
        2. Run the script with "-r" or "--uarem" option
        3. See on screen or in output.txt for the list of Unit addresses with the hyphens removed
    """

    #Open Files
    inputfile = open('input.txt', 'r')
    output = open('output.txt', 'w')

    #Process
    for ua in inputfile.read().splitlines(): #read records and remove newlines
        ua_replaced = (ua.replace('-','')) #Remove the "-" from the UAs
        print (ua_replaced) #Print output to screen
        output.write(ua_replaced+"\n") #Write results to output.txt

    #Close Files
    inputfile.close()
    output.close()

    #Truncate input file
    truncate("input.txt")

def access_file(file):
    """
        Opens a file, in this case, input.txt or output.txt, to view file contents.
        Editor attemot order -> 1. Gedit, 2. Nano, 3. vi

        To Do: 1. Add notepad.exe option + mac.
    """
    #print(file) #Test

    if shutil.which('gedit') is not None:
        print("Gedit exists...Opening" + " " + file + " " + "with Gedit")
        os.system("gedit" + " " + file)
    elif shutil.which('nano') is not None:
        print("Nano exists...Opening" + " " + file + " " + "with Nano")
        os.system("nano" + " " + file)
    elif shutil.which('vi') is not None:
        print("Vi exists...Opening" + " " + file + " " + "with Vi")
        os.system("vi" + " " + file)
    #To Do: Add option for notepad.exe and mac text editor
    else:
        print("Gedit, Nano, or vi do not exist. Unable to open" + " " + file)
    
        

def main():
    if len(sys.argv) <= 1:
        usage()
    try:
        (opts, args) = getopt.getopt(sys.argv[1:], 'aroixhu', [
            'uaadd', 'input', 'output', 'uarem', 'help'])
    except (getopt.GetoptError):
        usage()
        sys.exit(2)
    for (o, a) in opts:
        if o in ('-h', '--help'):
            usage()
        elif o in ('-a', '--uaadd'):
            ua_list_add_slashes()
        elif o in ('-i', '--input'):
            file = "input.txt"
            access_file(file)
        elif o in ('-o', '--output'):
            file = "output.txt"
            access_file(file)
        elif o in ('-r', '--uarem'):
            ua_list_remove_slashes()
        #elif o in ('-u', '--update'):
            #usage()
        else:
            usage()


if __name__ == '__main__':
    main()

