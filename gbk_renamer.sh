
#!/bin/bash

# Description: This scripts adds a prefix (subdirectory name) to all .gbk files inside the subdirectories
# Utility: Usefull to format antiSMASH results for other analysis.

for i in $(ls); do                        # runs through the 'items' in this dir                               
  if [ -d $i ]; then                      # if this is a dir
     fname=${i##*/}    # pick up the dir name which will be used as prefix
     fname2="$( echo "$fname" | sed s/_out//g )"  # remove _out from folder name (if present)               
     echo $fname2                           
     cd $i                                    # move into the dir       
     for z in *.gbk; do               # loop over .gbk files
       mv $z ${fname2}_${z}         # put the prefix to the file.               
     done                                        
     cd ..                                         
  fi                                              
done

# Author: Sandra Godinho Silva
# Email: sandragodinhosilva@gmail.com
# Version: 0.1
# Date: 27/05/2020
