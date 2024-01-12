from textwrap import wrap

convert = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UGU": "Cysteine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
}


def proteins(strand):
    codons = wrap(strand, width=3)
    aa = []
    for codon in codons:
        if codon == "UAA" or codon == "UAG" or codon == "UGA":
            break
        aa.append(convert.get(codon))
    return aa
