'''
def read():
    flag = True
    while flag:
        try:
            # change to read in sequence from file
            sequence = "5’ TCAATGTAACGCGCTACCCGGAGCTCTGGGCCCAAATTTCATCCACT 3’"
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
 '''

def read(fastafile):
    fastaseq = open(fastafile, 'r')
    originalseq = ""
    for line in fastaseq:
        if line[0] != '>':
            originalseq = originalseq + line.strip()


def complement(sequence):
    # Reverses the sequence
    backward = sequence[::-1]
    complementaryseq = []
    pair = {"A": "T", "C": "G", "T": "A", "G": "C"}
    for i in range(len(backward)):
        if backward[i] in pair.keys():
            complementaryseq.append(pair[backward[i]])

    complementaryseq = ''.join(complementaryseq)
    print(complementaryseq)
    return complementaryseq



def orf(seq, comp):
    frames = []
    # Reading frames for the original sequence and reverse complement
    # We assume that the length of the sequence and complement should be the same
    # 3 possible frames for sequence and 3 possible for the reverse complement
    for x in range(3):
        s_frame = []
        c_frame = []
        for i in range(x, len(seq), 3):
            if (i + 2) < len(seq):
                s_frame.append([seq[i:i + 3]])
                c_frame.append([comp[i:i + 3]])
        frames.append(s_frame)
        frames.append(c_frame)


    orfList = list()
    for frame in frames:
        orf = False
        gene = []
        for codon in frame:
            if codon == ["ATG"]:
                orf = True
                print("appending", codon)
                gene.append(codon)
            while orf:
                gene.append(codon)
                if codon in (["TAA"], ["TGA"], ["TAG"]):
                    print("appending at end", codon)
                    gene.append(codon)
                    orfList.append(gene)
                    gene.clear()
                    orf = False

    print(orfList)



def main():
    seq = read()
    comp = complement(seq)
    orf(comp, seq)


if __name__ == "__main__":
    main()
