def splice(mrnaSequence):
    final_seq = ""
    
    start = "GU"
    stop = "AG"

    splice_start = mrnaSequence.index(start)
    splice_stop = mrnaSequence.index(stop)

    final_seq += mrnaSequence[: splice_start] + mrnaSequence[splice_stop + 2 :]
    print("mRNA sequence after splicing:", final_seq)
    return final_seq


splice("CCGUCCCCCCCCAGCC")
splice("CUGUCCCCvCCCsAGCU")

