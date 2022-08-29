"""
    Name: DCT-Tools/ua_list_add_slashes.py
    Date: Aug 29th, 2022
    Author: Mr-Market (sp)

    Description: Take a list of dct unit addresses and add slashes.
    Example: 0000439530485103 -> 000-04395-30485-103

    How To Use:
    1. Place your list of DCT Unit Addresses without hyhens into the input.txt file
    2. Run the script
    3. See on screen or in output.txt for the list of Unit addresses with the hyphens added
"""
from dcttools_functions import *

#Open Files
inputfile = open('input.txt', 'r')
output = open('output.txt', 'w')

#Process
for ua in inputfile.read().splitlines(): #read records and remove newlines
    ua = ua[0: 3] + "-" + ua[3:8] + "-" + ua[8:13] + "-" + ua[13:16] # Add Hyphens
    print (ua) 
    output.write(ua+"\n") #Write results to output.txt

#Truncate input file
truncate("input.txt")

#Close Files
inputfile.close()
output.close()