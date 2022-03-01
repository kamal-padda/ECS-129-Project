def read():
    flag = True
    while flag:
        try:
            # change to read in sequence from file
            sequence = "5’TATAAAGAGCCATGCATGAACTGGATAAAAGGCTCTGAGAATTTATCTCTAG’"
            # Raises all the nucleotides to upper case to get rid of user input case error
            sequence = sequence.upper()
            for c in sequence:
                if c not in "5’ACGT3' ":
                    raise ValueError
                else:
                    flag = False
        except ValueError:
            print("There was an error in the protein sequence, please try again. \n")

    for char in sequence:
        if not char.isalpha():
            sequence = sequence.replace(char, '')
    return sequence

"""
def read(fastafile):
    fastaseq = open(fastafile, 'r')
    originalseq = ""
    for line in fastaseq:
        if line[0] != '>':
            originalseq = originalseq + line.strip()
    orignalseq = ''.join(originalseq)
    print(originalseq)
    return originalseq
"""


def complement(originalseq):
    # Reverses the sequence
    backward = originalseq[::-1]
    complementaryseq = []
    pair = {"A": "T", "C": "G", "T": "A", "G": "C"}
    for i in range(len(backward)):
        if backward[i] in pair.keys():
            complementaryseq.append(pair[backward[i]])

    complementaryseq = ''.join(complementaryseq)
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
            


def main():
    seq = read()
    comp = complement(seq)
    gene = orf(seq, comp)
    print(gene)


if __name__ == "__main__":
    main()
