# bgc-analysis
#### Secondary metabolism exploration
Some handy scripts to work with antiSMASH and BiG-SCAPE results.

* **Script** to format .gbk file headers to use them as input in antiSMASH: [`gbk_file_formater.py`](/gbk_file_formater.py) \
Utility: Output files from Prokka annotation can have some incompatibilities with the required antiSMASH input.

* **Script** adds a prefix (subdirectory name) to all .gbk files inside the subdirectories. [`gbk_renamer.sh`](/gbk_renamer.sh) \
Utility: Usefull to format antiSMASH v5.0 results for other analysis so they are trackable.

* **Script** to summarize results from antiSMASH v5.0 into a csv file per genome and summary table with BGC type counts per genome: [`antismash_html_tocsv.py`](/antismash_html_tocsv.py) 

* **Script** to clean .fasta files that have unwanted lines starting with '-': [`fasta_cleanner.py`](/fasta_cleanner.py) \
Utility: While running BiG-SCAPE, the workflow may stop due to lines starting with '-' in some .fasta files.
