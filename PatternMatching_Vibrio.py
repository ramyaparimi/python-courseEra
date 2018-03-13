# Copy your PatternMatching function below this line.
def PatternMatching(Pattern,Genome):
    Positions=[]
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            Positions.append(i)
    return Positions
# # The following lines will automatically read in the Vibrio cholerae genome for you and store it in a variable named v_cholerae
# import sys                              # needed to read the genome
# input = sys.stdin.read().splitlines()   #
# v_cholerae = input[1]                   # store the genome as 'v_cholerae'

v_cholerae=open("Vibrio_cholerae.txt","r").encode("UTF-8")
v_cholerae.read()
# Call PatternMatching with Pattern equal to "CTTGATCAT" and Genome equal to v_cholerae,
# and store the output as a variable called positions
positions=PatternMatching("CTTGATCAT",v_cholerae)

# print the positions variable
print(positions)