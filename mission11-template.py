# CS1010A --- Programming Methodology
# Mission 11 Template

# Note that written answers are stored in """multi-line strings"""
# to allow us to run your code easily when grading your problem set.

import csv
from xml.sax.handler import property_encoding


def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows


##########
# Task 1 #
##########

def replicate(dna_strand):
    dna_base_pairings = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    new_dna_strand = ""
    for letter in dna_strand:
        new_dna_strand = dna_base_pairings.get(letter, "") + new_dna_strand
    return new_dna_strand

#print("## Q1 ##")
#print(replicate("AAATGC"))     # 'GCATTT'
#print(replicate("ATTGGGCCCC")) # 'GGGGCCCAAT'

with open("dna.txt") as f:
    dna = f.read()
#print(replicate(dna )[:10])    #'AATAGTTTCT'


##########
# Task 2 #
##########

def transcribe(dna_strand):
    dna_base_pairings = {
        "A": "U",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    new_dna_strand = ""
    for letter in dna_strand:
        new_dna_strand = dna_base_pairings.get(letter, "") + new_dna_strand
    return new_dna_strand


def reverse_transcribe(rna_strand):
    dna_base_pairings = {
        "U": "A",
        "A": "T",
        "G": "C",
        "C": "G"
    }
    new_rna_strand = ""
    for letter in rna_strand:
        new_rna_strand = dna_base_pairings.get(letter, "") + new_rna_strand
    return new_rna_strand

print("## Q2 ##")
#print(transcribe("AAATGC"))     # 'GCAUUU'
#print(transcribe("ATTGGGCCCC")) # 'GGGGCCCAAU'

#print(reverse_transcribe(transcribe("AAATGC"))) # 'AAATGC'
#print(reverse_transcribe("GGGGCCCAAU"))         # 'ATTGGGCCCC'

rna = transcribe(dna)
#print(rna[-10:])                # 'GAAUAUGUGA'


##########
# Task 3 #
##########

def get_mapping(csvfilename):
    dic = {}
    with open(csvfilename) as csvfile:
        for row in csv.reader(csvfile):
            dic[row[0]] = row[-1]
    return dic

print("## Q3 ##")
codon2amino = get_mapping("codon_mapping.csv")

#print(codon2amino["ACA"]) # 'T'
#print(codon2amino["AUU"]) # 'I'
#print(codon2amino["CUC"]) # 'L'
#print(codon2amino["ACU"]) # 'T'
#print(codon2amino["UAG"]) # '_'
#print(codon2amino["UGA"]) # '_'


##########
# Task 4 #
##########

def translate(rna_strand):
    codon2amino = get_mapping("codon_mapping.csv")
    protein = ""
    i = 0
    while i < len(rna_strand):
        if rna_strand[i:i+3] == "AUG":
            break
        i += 1
    if i >= len(rna_strand):
        return None
    while i < len(rna_strand):
        codon = rna_strand[i:i + 3]
        if codon in ["UAA", "UAG", "UGA"]:
            protein += codon2amino[codon]
            break
        protein += codon2amino[codon]
        i += 3
        if i >= len(rna_strand):
            return None
    return protein

print("## Q4 ##")
print(translate("AUGUAA"))           # 'M_'
print(translate("AGAGAUGCCCUGAGGG")) # 'MP_'

protein = translate(rna)
print(protein) # 'MANLTNFHLKIYIHTYIQLKHLSSGAFSLFSAHNSRSINYNYYFSFRDLNITYNHTHLTTY_'
print(protein == 'MANLTNFHLKIYIHTYIQLKHLSSGAFSLFSAHNSRSINYNYYFSFRDLNITYNHTHLTTY_') # True


##########
# Task 5 #
##########

'''
=== Space Complexity Analysis ===
to create get_mapping (dict): O(n)
to create get_mapping (list): O(n)

=== Time Complexity Analysis ===
codon lookup using codon2amino (dict): O(1)
codon lookup using codon2amino (list): O(n)

=== Conclusion ===
State and justify which is the better implementation.
The dictionary version is far more efficient for codon lookups, with constant time complexity of O(1). The list version
requires a linear search with time complexity O(n), which means that as the number of codons grows, the lookup time increases 
linearly. This makes the list version much less efficient for codon lookups.
'''
