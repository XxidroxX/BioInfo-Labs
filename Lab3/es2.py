"""
Assignment 2
"""
# Step 1: Write a Python program that parses the gtf file and extract the information about chr10 and 18. Select only
#         rows for which the feature is equal to "gene" and gene_biotype equal to "protein_coding".
print("Assignment 2")

# key=gene, value=count occurrences in SAM file
gene_count = dict()
with open('./Homo_sapiens.GRCh38.95.gtf', 'r') as vcf:
    for line in vcf:
        if not line.startswith("#"):
            feature = line.split("\t")[2]
            chromosome = line.split("\t")[0]
            gene_name = line.split("\t")[8].split(";")[2].split(" ")[2].replace("\"", "")

            if feature == 'gene' and "gene_biotype \"protein_coding\"" in line and (chromosome == "18" or chromosome == "10"):
                start = line.split("\t")[3]
                end   = line.split("\t")[4]
                # cerco nel file SAM
                with open("./results.sam", "r") as sam:
                    for l in sam:
                        if not l.startswith("@"):
                            index = l.split("\t")[3]
                            if start <= index <= end and chromosome == l.split("\t")[2]:
                                if gene_name in gene_count:
                                    gene_count[gene_name] = gene_count.get(gene_name) + 1
                                else:
                                    gene_count[gene_name] = 1

print(gene_count)
