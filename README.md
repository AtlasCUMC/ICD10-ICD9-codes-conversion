# ICD10 and ICD9 codes conversion

# Introduction
We created a database for conversion of the ICD10 to ICD9 codes, since most PheWAS algorithms uses the ICD9 codes. We downloaded the ICD9 and ICD10 codes from https://www.cms.gov/Medicare/Coding/ICD10/2018-ICD-10-CM-and-GEMs.html. We developed a python script to directly convert the ICD10 codes to ICD9 and vice versa.

# Useful database
https://www.cdc.gov/nchs/icd/icd10cm_pcs_background.htm

https://www.findacode.com/icd-9/icd-9-cm-diagnosis-codes.html

## Usage

### ICD10 to ICD9

First downlaod the code and the database:

git clone https://github.com/Atlas9266/ICD10-ICD9-codes-conversion.git

Then cd
cd ICD10-ICD9-codes-conversion

python KK_ICD10_to_ICD9.py --help

The database for converting ICD-10 to ICD-9 codes

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Verbose output
  -ICD10 The list of ICD10 codes is need to be converted ICD9 codes, --ICD10 The list of ICD10 codes is need to be converted ICD9 codes
                        The list ICD10 codes
  -ICD9 The output ICD9 codes file, --ICD9 The output ICD9 codes file
                        The list of ICD9 codes

python KK_ICD10_to_ICD9.py -ICD10 your_list_of_icd10_codes -ICD9 OUT_PUT_ICD9

EXAMPLE

python KK_ICD10_to_ICD9.py -ICD10 your_list_of_icd10_codes -ICD9 OUT_PUT_ICD9

### ICD9 to ICD10

python KK_ICD9_to_ICD10.py -ICD9 your_list_of_icd9_codes -ICD10 OUT_PUT_ICD10

### ICD9 to ICD10

python KK_icd10to9_v1.1.py  --help 

Eaxmaple
python KK_icd10to9_v1.1.py A00.0 
After running this code, it will print the out in terminal: 
ICD9 = 001.0


# Author

Atlas Khan, Department of Medicine (Division Nephrology), Columbia University Medical Centre, New York, USA.


