def splice(mrnaSequence):
    final_seq = ""
    splice_seq = ""
    pair = ""
    # Will iterate through twice, for each reading Frame that could contain a splice site
    for x in range(2):
        splice = False
        for i in range(x, len(mrnaSequence), 2):
            pair = mrnaSequence[i:i + 2]
            if pair == 'GU' and splice == False:
                 splice_seq += pair
                 splice = True
            elif pair == 'AG' and splice == True:
                 splice_seq += pair
                 splice = False
            else:
                if splice == True:
                    splice_seq += pair
    final_seq = mrnaSequence.replace(splice_seq, '')
    print("mRNA sequence after splicing:", final_seq)
    return final_seq


splice("CCGUCCCCCCCCAGCC")
splice("CGUCCCCCCCCAGC")

