#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys 
import getopt

VERSION = "1.0.0"

class colors:

    BLUE = '\033[94m'
    #GREEN = '\033[92m'
    #RED = '\033[31m'
    #YELLOW = '\033[93m'
    #FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    #BGRED = '\033[41m'
    #WHITE = '\033[37m'

def logo():
    print(colors.BLUE + colors.BOLD)
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
    -a    --uaadd       Add Slashes To a List of UA's
    -r    --uarem       Remove Slashes From a List of UA's
    -h    --help        print(this help and exit)
    -     --future      Future Use
    -     --future      Future Use
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
        Future Use. So we don't manually open the files each time.
    """
    #inputfile = open('input.txt', 'r')
    #output = open('output.txt', 'w')
    
def close_files():
    """
        Future Use. So we don't manually close files each time.
    """
    #inputfile.close()
    #output.close()

def ua_list_add_slashes():
    """
        Description: Take a list of dct unit addresses and add slashes.
        Example: 0000439530485103 -> 000-04395-30485-103

        How To Use:
        1. Place your list of DCT Unit Addresses without hyhens into the input.txt file
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


def main():
    #check_root()
    if len(sys.argv) <= 1:
        #check_update()
        usage()
    try:
        (opts, args) = getopt.getopt(sys.argv[1:], 'arxhu', [
            'uaadd', 'stop', 'uarem', 'help', 'update'])
    except (getopt.GetoptError):
        usage()
        sys.exit(2)
    for (o, a) in opts:
        if o in ('-h', '--help'):
            usage()
        elif o in ('-a', '--uaadd'):
            ua_list_add_slashes()
        #elif o in ('-x', '--stop'):
            #usage()
        elif o in ('-r', '--uarem'):
            ua_list_remove_slashes()
        #elif o in ('-u', '--update'):
            #usage()
        else:
            usage()


if __name__ == '__main__':
    main()

