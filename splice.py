def splice(mrnaSequence):
    frames = []
    
    for x in range(2):
        frame = ""
        for i in range(x, len(mrnaSequence), 2):
            if (i + 1) < len(mrnaSequence):
                frame += mrnaSequence[i:i + 2]
        frames.append(frame)

    final_seq = ""
    splice_seq = ""
    pair = ""
    # Will iterate through twice, for each reading Frame that could contain a splice site
    for frame in frames:
        splice = False
        for i in range(0, len(frame), 2):
            pair = frame[i:i + 2]
            if pair == 'GU' and splice == False:
                 splice_seq += pair
                 splice = True
            elif pair == 'AG' and splice == True:
                 splice_seq += pair
                 splice = False
            else:
                if splice == True:
                    splice_seq += pair 
                    print("append", pair)
    print(splice_seq)
    final_seq = mrnaSequence.replace(splice_seq, '')
    print("mRNA sequence after splicing:", final_seq)
    return final_seq


splice("CCGUCCCCCCCCAGCC")
splice("CUGUCCCcCCCCAGCU")

