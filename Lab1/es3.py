"""
### Assignment 3 ###
>python es3.py fasta1_file fasta2_file
"""
import sys

file_1 = sys.argv[1]
file_2 = sys.argv[2]
reads = ''

with open(file_1) as fp:
    seq = ''
    read_id = ''
    for line_index, line in enumerate(fp):
        if line_index == 0:
            read_id = line[1:-1]
        elif line.startswith(">"):
            # cerco
            with open(file_2) as fp2:
                seq2 = ''
                read_id2 = ''
                for line2_index, line2 in enumerate(fp2):
                    if line2_index == 0:
                        read_id2 = line2[1:-1]
                        continue
                    if line2.startswith(">"):
                        if seq == seq2:
                            reads += read_id+" - "+read_id2+'\n'
                            seq2 = ''
                            break
                        seq2 = ''
                        read_id2 = line2[1:-1]
                    else:
                        seq2 += line2[:-1]
            read_id = line[1:-1]
            seq = ''
        else:
             seq += line[:-1]
print(reads)