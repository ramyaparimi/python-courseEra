def Complement(Pattern):
    x=""
    for i in Pattern:
        if i=="A":
            x=x+"T"
        elif i=="T":
            x=x+"A"
        elif i=="G":
            x=x+"C"
        else:
            x=x+"G"
    return x


print(Complement("ATGCTGAT"))