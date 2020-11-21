"""
# Assignment 1
# Step 1: Convert SAM file obtained in LAB2 to BAM -> Done with CMD (my.bam)
# Step 2: Sort BAM file to make the following process faster. -> Done with CMD
# Step 3: Use bcftools to obtain a VCF file. -> Done with CMD (sorted.vcf)
# Step 4: Write a Python program to parse the VCF file and obtain only Single Nucleotides Polymorphism (SNP) for which
#         the information is complete.
"""
print("Step 4")
with open('sorted.vcf', 'r') as vcf:
    for line in vcf:
        if not line.startswith("#"):
            reference = line.split("\t")[3]
            sample = line.split("\t")[4]
            if "," in sample:
                if reference != sample.split(",")[0]:
                    print(line)
"""
# Step 5: Write a Python program to parse VCF file and obtain only Insertion or Deletions (INDEL) for which the
#         information is complete.
"""
print("Step 5")
with open('sorted.vcf', 'r') as vcf:
    for line in vcf:
        if not line.startswith("#"):
            reference = line.split("\t")[3]
            sample = line.split("\t")[4]
            if "INDEL" in line:
                print(line)
