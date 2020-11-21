"""
### Assignment 2 ###
Write a python program for extracting statistics from fasta/fastq files. The program must take as a
first argument from the command line the name of the input fasta file to be analyzed and write to
an output text file (whose name is passed as a second argument from the command line) a
summary of the computed statistics.
The following are the expected output statistics:
- Statistics of single bases across all the reads: Number of A,T,C,G
- Number of reads having at least one low complexity sequence: AAAAAA, TTTTTT, CCCCCC or
GGGGGG.
- Number of reads having the number of GC couples (so called GC content) higher than a threshold
GC_THRESHOLD passed as third argument from the command line
- For each read having a GC content higher than GC_THRESHOLD, report the read_id and the
number of GC couples

>python es2.py input_file threshold
(ho rimosso il file di output perchè stampo semplicemente a video)
"""
import sys

f = open(sys.argv[1], "r")
reads_complex, gc_reads = 0, 0
gc_ts = int(sys.argv[2])
reads_details = ""
bases = ['G', 'C', 'T', 'A']
count = [0, 0, 0, 0]

for line_number, line in enumerate(f):
    if (sys.argv[1][-1] == 'a' and line.startswith(">")) or (sys.argv[1][-1] == 'q' and line_number % 4 != 1):
        continue

    if "A"*6 in line or "T"*6 in line or "C"*6 in line or "G"*6 in line:
        reads_complex += 1

    for index, base in enumerate(bases):
        count[index] += line.count(base)

    gc_bases = line.count("GC")
    if gc_bases >= gc_ts:
        gc_reads += 1
        reads_details += "Read #"+str(line_number)+" with GC couples: "+str(gc_bases)+"\n"

for index, base in enumerate(bases):
    print("Number of "+base+": "+str(count[index]))

print("Number of complex reads: " + str(reads_complex))
print("Number of GC reads: " + str(gc_reads) + "\n")
print(reads_details)
