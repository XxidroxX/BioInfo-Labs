"""
### Assignment 4 ###
"""
import collections
import csv
import numpy as np

file1 = open("alignments.txt", "w")
file1.writelines("read_0\tCAGCCATGACACTAAGCACG\t15\n")
file1.writelines("read_1\tTTTAAAAAATCCGTGGACAC\t40\n")
file1.writelines("read_2\tGCATTTAAAAAATCCTTGGA\t37\n")
file1.writelines("read_3\tATTTCGGCGGCGACACCCCG\t0\n")
file1.writelines("read_4\tTTCGGCGGCGACACACCGAT\t2\n")
file1.writelines("read_5\tATATTTGGACACAAATGCAT\t48\n")
file1.close()  # to change file access modes

matrix = np.zeros((6, 69), dtype=np.str)
with open('alignments.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row_index, row in enumerate(csv_reader):
        for i in range(int(row[2]), int(row[2])+len(row[1])):
            matrix[row_index, i] = row[1][i-int(row[2])]

result = []
region = []
def unique_list(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]

for c in matrix.T:
    counts = collections.Counter(c)
    new_list = sorted(c, key=counts.get, reverse=True)
    unique = unique_list(new_list)

    if len(unique) > 1:
        if unique[0] == "":
            region.append(unique[1])
        else:
            region.append(unique[0])
    else:
        result.append(region)
        region = []

for i in result:
    print(i)