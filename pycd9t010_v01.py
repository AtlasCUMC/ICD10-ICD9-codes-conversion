# PyCD
# Version 0.1
# This script converts ICD-9 to ICD-10 codes with optional verbose
# output.
# usage: pycd.py [-h] [-v] code

# positional arguments:
#  code           ICD-9 code

# optional arguments:
#  -h, --help     show this help message and exit
#  -v, --verbose  Verbose output

import csv, sys, argparse

ap = argparse.ArgumentParser()
ap.add_argument('-v','--verbose',help="Verbose output",action="store_true")
ap.add_argument("code",help = "ICD-9 code", type=str)
args = ap.parse_args()

#Import CSV file
try:
	dict = open('ICD10_Formatted.csv')
except FileNotFoundError:
	print("Unable to find file.")
	sys.exit(1)

csv_dict = csv.reader(dict, delimiter='|')

#Search for matching ICD-9, return ICD-10 and description
if args.verbose is True:
	for row in csv_dict:
		if row[0] == args.code:
			print("ICD-10: ", row[1])
			print("Description: ", row[2])			
elif args.verbose is False:
	for row in csv_dict:
		if row[1] == args.code:
			print(row[0])

