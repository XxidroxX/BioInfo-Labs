"""
### Assignment 1 ###
Global Alignment
"""
import sys
import numpy as np
sys.setrecursionlimit(3500)

seq1 = sys.argv[1]
seq2 = sys.argv[2]
# match, mismatch, gap costs
costs = [int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])]

matrix = np.zeros((len(seq1)+1, len(seq2)+1))
a = len(seq2)
# Operazioni preliminari: setup della prima riga e prima colonna
matrix[0, :] = np.arange(start=0, stop=costs[2]*(len(seq2)+1), step=costs[2])
matrix[:, 0] = np.arange(start=0, stop=costs[2]*(len(seq1)+1), step=costs[2])

for row_index in range(1, len(seq1)+1):
    row = matrix[row_index, :]
    for col_index in range(1, len(seq2)+1):
        # per ogni cella ho potenzialmente 3 possibili movimenti: ori, vert, diag
        element = row[col_index]
        if seq1[row_index-1] == seq2[col_index-1]:
            # match
            next_value = np.amax([costs[0]+matrix[row_index-1, col_index-1],
                                 matrix[row_index-1, col_index]+costs[2],
                                 matrix[row_index, col_index-1]+costs[2]])
        else:
            # missmatch
            next_value = np.amax([costs[1] + matrix[row_index - 1, col_index - 1],
                                 matrix[row_index - 1, col_index] + costs[2],
                                 matrix[row_index, col_index - 1] + costs[2]])
        matrix[row_index, col_index] = next_value

print("Global alignment score: "+str(matrix[-1,-1]))
print(matrix)
print("Final alignment: ")

# Start from the bottom right cell in matrix
r = len(seq1)
c = len(seq2)
align1 = ""
align2 = ""


# A function for determining the score between any two bases in alignment
def match_score(alpha, beta):
    if alpha == beta:
        return costs[0]
    elif alpha == '-' or beta == '-':
        return costs[2]
    else:
        return costs[1]

def tree(row, col, align1, align2):
    score_current = matrix[row, col]
    score_diagonal = matrix[row - 1, col - 1]
    score_up = matrix[row - 1, col]
    score_left = matrix[row, col - 1]

    if row == 0 and col == 0:
        # Since we traversed the score matrix from the bottom right, our two sequences will be reversed.
        # These two lines reverse the order of the characters in each sequence.
        align1 = align1[::-1]
        align2 = align2[::-1]
        center_string = ""
        for i, j in zip(align1, align2):
            if i == j:
                center_string += "*"
            else:
                center_string += " "

        print(align1)
        print(center_string)
        print(align2+"\n")
        return
    # Check to figure out which cell the current score was calculated from,
    # then update i and j to correspond to that cell.
    if score_current == score_diagonal + match_score(seq2[col - 1], seq1[row - 1]):
        tree(row-1, col-1, align1+seq1[row-1], align2+seq2[col-1])

    if score_current == score_up + costs[2]:  # gap_penalty
        tree(row-1, col, align1+seq1[row-1], align2+'-')

    if score_current == score_left + costs[2]:  # gap_penalty
        tree(row, col-1, align1+'-', align2+seq2[col-1])

tree(r, c, align1, align2)
