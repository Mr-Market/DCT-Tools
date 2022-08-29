"""
    Name: dcttools/ua_list_remove_slashes.py
    Date: Aug 29th, 2022
    Author: Mr-Market (sp)

    Description: Take a list of dct unit addresses and remove all slashes
    Example: 000-04395-30485-103 -> 0000439530485103

    How To Use:
    1. Place your list of DCT Unit Addresses with hyhens into the input.txt file
    2. Run the script
    3. See on screen or in output.txt for the list of Unit addresses with the hyphens removed

"""
from dcttools_functions import *

#Open Files
inputfile = open('input.txt', 'r')
output = open('output.txt', 'w')

#Process
for ua in inputfile.read().splitlines(): #read records and remove newlines
    ua_replaced = (ua.replace('-','')) #Remove the "-" from the UAs
    print (ua_replaced) #Print output to screen
    output.write(ua_replaced+"\n") #Write results to output.txt

#Truncate input file
truncate("input.txt")

#Close Files
inputfile.close()
output.close()

