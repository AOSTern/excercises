def to_rna(dna_strand):
    rna_strand = ""
    for i in dna_strand:
        if i == "A":
            rna_strand = rna_strand + ("U")
        if i == "T":
            rna_strand = rna_strand + ("A")
        if i == "G":
            rna_strand = rna_strand + ("C")
        if i == "C":
            rna_strand = rna_strand + ("G")
    return rna_strand
