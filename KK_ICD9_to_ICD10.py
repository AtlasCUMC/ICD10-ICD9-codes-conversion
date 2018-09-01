# Atlas Khan
#12/08/2017

# Version 0.1
# This script converts ICD-9 to ICD-10 codes with optional verbose

import csv, sys, argparse
import os
from itertools import product
from time import sleep,ctime
import time
prog_name = "KK_ICD10_to_ICD9.py"

def main():
    ap = argparse.ArgumentParser(description='The database for converting ICD-10 to ICD-9 codes', prog = prog_name)
    ap.add_argument('-v','--verbose',help="Verbose output",action="store_true")
    ap.add_argument('-ICD9', '--ICD9' ,required = True, metavar = 'The list of ICD10 codes is need to be converted ICD9 codes', type = str, help ='The list ICD10 codes')
    ap.add_argument('-ICD10', '--ICD10', required = True, metavar = 'The output ICD9 codes file', type = str, help ='The list of ICD9 codes')

    time_total=time.time()
    ops=ap.parse_args()
    if ops.ICD9 is None:
        ap.print_help(),ctime()
    else:
        args = ap.parse_args()
        #ICD10=os.path.abspath(args.ICD10)
        ICD9=os.path.abspath(args.ICD9)
        ICD10=args.ICD10



########### The database ###########

    try:
	    dict = open('ICD_9_10_d_v07.csv')
    except FileNotFoundError:
	    print("Unable to find file, since the database file should be in the current directory!!!!!!!!!!!!!."),ctime()
	    sys.exit(1)


    csv_dict = csv.reader(dict, delimiter='|')

    dict_lines={}

    if args.verbose is True:
	    for row in csv_dict:
	 	    if row[0] == args.code:
			    print("ICD-10: ", row[1])
			    print("Description: ", row[2])
    elif args.verbose is False:
        for p1 in dict.readlines():
            p2=p1.strip()
            dict_lines[p2.split("|")[1]] = p2
        f3=open(ICD9, 'r')
        print ctime(),("\n" "NOTICE:Converting ICD9 codes to ICD10 codes!")
        with open(ICD10 + "_ICD10.txt",'w') as output2:
            for val in f3.readlines():
                val1=val.strip()
                val2=val1.split("\t")[0]
                p2 = dict_lines.get(val2, None)
                if p2==None:
                    p3=val1.split()[0] + "\t"+ val1.split()[0]  +"\t" + "ICD10"

	            output2.write('%s\n' % p3)
                else:
                    p4= p2.split("|")[0] + "\t" +  p2.split("|")[1] + "\t" +  p2.split("|")[2]
                    output2.write('%s\n' % p4)
        output2.close()
    

    header = "ICD10" + "\t" + "ICD9" + "\t" + "I9Name" "\n"
    def WriteHeader(ICD10, header):
        file = open(ICD10 + "_ICD10.txt", 'r')
        lines = [line for line in file]
        file.close()
        if lines and lines[0] == header:
            return True
        else:
            file = open(ICD10 + "_ICD10.txt", 'w')
            file.write(header + ''.join([line for line in lines if not line == header]))
            file.close()
            return True
    WriteHeader(ICD10, header)


    print ctime(),("\n" "NOTICE: Please see the ICD10 and ICD9 codes in: " "\n" + ICD10 + "_ICD10.txt")
    time_end_total=time.time()
    elapsed_total=time_end_total-time_total
    print "Time taken: ", elapsed_total, "seconds."
if __name__ == '__main__':
    main()
