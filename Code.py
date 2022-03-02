def read():
    # Reads in text file name from user
    textfile = input("Enter text file name: ")
    textseq = open(textfile, 'r').readlines()
    originalseq = ""
    errorChar = dict()

    # Stores capitalized sequence in new string
    for line in textseq:
        originalseq = line.upper()

    # Checks to see if there are errors in the string
    for c in originalseq:
        if c not in "5'ACGT3' " or not c.isalpha():
            originalseq = originalseq.replace(c, '')
            for key in errorChar:
                errorChar[key] = originalseq.index(c)

    if errorChar:
        print("The following charaacters that didn't correspond to nucleotides were found:", errorChar)
    # Prints and returns the formatted sequence
    print("Original sequence: " + originalseq)
    return originalseq


def complement(originalseq):
    # Reverses the sequence
    backward = originalseq[::-1]
    complementaryseq = []
    pair = {"A": "T", "C": "G", "T": "A", "G": "C"}
    for i in range(len(backward)):
        if backward[i] in pair.keys():
            complementaryseq.append(pair[backward[i]])

    complementaryseq = ''.join(complementaryseq)
    print("Complementary sequence: " + complementaryseq)
    return complementaryseq


def orf(seq, comp):
    frames = []
    # Reading frames for the original sequence and reverse complement
    # We assume that the length of the sequence and complement should be the same
    # 3 possible frames for sequence and 3 possible for the reverse complement
    for x in range(3):
        s_frame = ""
        c_frame = ""
        for i in range(x, len(seq), 3):
            if (i + 2) < len(seq):
                s_frame += seq[i:i + 3]
                c_frame += comp[i:i + 3]
        frames.append(s_frame)
        frames.append(c_frame)

    # Returns the longest gene sequence
    orfList = list()
    for frame in frames:
        gene = []
        orf = False
        for i in range(0, len(frame), 3):
            codon = frame[i:i+3]
            if codon == "ATG" and not orf:
                gene.append(codon)
                orf = True
            elif codon in ("TAA", "TGA", "TAG") and orf:
                gene.append(codon)
                orf = False
            else:
                if orf:
                    gene.append(codon)
        if gene:
            if gene[0] == "ATG" and gene[-1] in ("TAA", "TGA", "TAG"):
                orfList.append(''.join(gene))
    # returns longest gene in orfList
    return max(orfList, key=len)


def transcribe(gene):
    # Transcribes gene into mRNA
    gene = str(gene)
    gene = gene.upper()
    listHolder = list(gene)
    for i in range(len(listHolder)):
        if listHolder[i] == 'T':
            listHolder[i] = 'U'
    mrnaSequence = "".join(listHolder)
    return mrnaSequence


def translate(mrnaSequence):
    # Translate mRNA into AA sequence
    aaSequence = []
    codonList = [mrnaSequence[i:i+3] for i in range(0,len(mrnaSequence),3)]
    for i in codonList:
        if i == "AUG":
            aaSequence.append("M")
        elif i == "UUU" or i == "UUC":
            aaSequence.append("F")
        elif i == "UUA" or i == "UUG" or i == "CUU" or i == "CUC" or i == "CUA" or i == "CUG":
            aaSequence.append("L")
        elif i == "GUU" or i == "GUC" or i == "GUA" or i == "GUG":
            aaSequence.append("V")
        elif i == "UCU" or i == "UCC" or i == "UCA" or i == "UCG" or i == "AGU" or i == "AGC":
            aaSequence.append("S")
        elif i == "CCU" or i == "CCC" or i == "CCA" or i == "CCG":
            aaSequence.append("P")
        elif i == "ACU" or i == "ACC" or i == "ACA" or i == "ACG":
            aaSequence.append("T")
        elif i == "GCU" or i == "GCC" or i == "GCA" or i == "GCG":
            aaSequence.append("A")
        elif i == "UAU" or i == "UAC":
            aaSequence.append("Y")
        elif i == "CAU" or i == "CAC":
            aaSequence.append("H")
        elif i == "CAA" or i == "CAG":
            aaSequence.append("Q")
        elif i == "AAU" or i == "AAC":
            aaSequence.append("N")
        elif i == "AAA" or i == "AAG":
            aaSequence.append("K")
        elif i == "GAU" or i == "GAC":
            aaSequence.append("D")
        elif i == "GAA" or i == "GAG":
            aaSequence.append("E")
        elif i == "UGU" or i == "UGC":
            aaSequence.append("C")
        elif i == "UGG":
            aaSequence.append("W")
        elif i == "CGU" or i == "CGC" or i == "CGA" or i == "CGG" or i == "AGA" or i == "AGG":
            aaSequence.append("R")
        elif i == "GGU" or i == "GGC" or i == "GGA" or i == "GGG":
            aaSequence.append("G")
        elif i == "AUU" or i == "AUC" or i == "AUA":
            aaSequence.append("I")
        else:
            break
    print("Amino acid sequence translated from mRNA: " + "".join(aaSequence))
    return("".join(aaSequence))


def main():
    seq = read()
    comp = complement(seq)
    openRF = orf(seq,comp)
    print("Longest ORF gene sequence: "+openRF)
    print("mRNA transcribed from gene: " + transcribe(openRF))
    translate(transcribe(openRF))


if __name__ == "__main__":
    main()
