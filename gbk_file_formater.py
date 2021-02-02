#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###############################################################################
#### Goal: Script to format gbk file headers to use them as input in antiSMASH             
#### Usage: python gbk_file_formater.py /path/to/directory_wt_all_files/ 
#### Note: provide full path!                                          
###############################################################################


import os
import glob
import argparse
import sys

parser=argparse.ArgumentParser(
    description='''Goal: remove "-" from begining of lines in FASTA files.''')

__file__ = "orf_annotation.py"
__author__ = 'Sandra Godinho Silva (sandragodinhosilva@gmail.com)'
__version__ = '0.2'
__date__ = '05-12-2020'

parser.add_argument('inputDirectory', 
		help='Specify the directory containing *.fa files')

# Execute parse_args()
args = parser.parse_args()

inputDirectory = sys.argv[1]
###############################################################################
curdir = inputDirectory
os.chdir(curdir)

gbkfiles = []
for file in glob.glob("*.gbk"):
    gbkfiles.append(file)

for filename in gbkfiles:
    d ={}
    z=0
    filenam = filename.split(".")
    out = str(filenam[0]) + "_out.gbk"
    with open(filename, "r+") as f, open(out, "a") as output:
        lines = f.readlines()
        i=0
        x=0
        for line in lines:
            x+=1
            if line.strip().startswith("LOCUS"):
                title = x
                a = line.split("       ")
                b = a[1]
                c = b.split("_")
                line2 = a[0] + "       " + c[2] + "       " + a[2]
            elif line.startswith("     source"):
                source = line.split("          ")
                numbers = source[1].split("..")
                size = numbers[1]
                sizes=int(size)
                t = line2.replace(str(sizes), "")
                t = t.replace("bp", (str(sizes) + " bp"))
                d[title]=t
                i+=1
        for line in lines:
            z+=1
            if z in d.keys():
                output.write(d[z])
            else:
                output.write(line)
        f.close()
        output.close()
 
__date__ = '26 May 2020'        
