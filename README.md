# DCT-Tools
Command line scripts for working with DCT settop IDs.

## Build and install from source
`git clone https://github.com/Mr-Market/DCT-Tools`

`cd dcttools`

`chmod +x build.sh`

`./build.sh`

## How to use:
1. Place UA list into input.txt
2. Run the script with desired option
    e.g.
    python3 dcttools.py -h
    dcttools -h 
3. See screen output or output.txt

## Add Slashes To a List Of UA's
This script will take a list of DCT unit addresses and ADD hyphens.

e.g. 00045643445678103 -> 000-45643-45678-103 

## Remove Slashes From a List of UA's
This script will take a list of DCT unit addresses and REMOVE all the hyphens in the UA's.

e.g. 000-45643-45678-103 -> 00045643445678103


