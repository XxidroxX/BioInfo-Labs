"""
### Assignment 1 ###
Write a python program that generates both fasta and fastq files containing reads with the following
characteristics:
- Read id contains a progressive number starting from 0.
- Sequences have length 50 bp
- Bases are randomly generated using a A,T,C,G alphabet, but probability of each base for each read
should be given from the command line as a set of numbers (probA, probT, probC, probG)
- The number of reads should be passed as an argument from the command line
- The name of the fasta/fastq file should be passed as an argument from the command line
- For fastq files only: the quality of each base is randomly selected.

Example:
python read_generator.fq simulatedfasta.fa 100 30 30 30 10
"""
import sys
from random import choices
import random
import numpy as np

num_args = len(sys.argv)
args = sys.argv
fastq = args[1]
fasta = args[2]
reads = int(args[3])
prob_a = int(args[4])
prob_t = int(args[5])
prob_c = int(args[6])
prob_g = int(args[7])
print('Number of arguments:', num_args, 'arguments.')
print('Argument List:', args)

file1 = open(fasta, "w")
file2 = open(fastq, "w")

for i in range(reads):
    base = choices(['A', 'T', 'C', 'G'], weights=[prob_a, prob_t, prob_c, prob_g], k=50)
    file1.writelines(">read_"+str(i)+"\n"+str(''.join(str(x) for x in base))+"\n")
    file2.writelines("@"+str(i)+"\n")
    file2.writelines(str(''.join(str(x) for x in base))+"\n")
    file2.writelines(str(i)+'\n')
    for _ in range(50):
        file2.writelines(chr(random.choice(np.arange(33, 127)))) #Sanger format
    file2.writelines("\n")
file1.close()
file2.close()
