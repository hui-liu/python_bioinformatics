########
# A02
########
import sys
import matplotlib.pyplot as plt

# (1)
def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()
            seq = fh.readline().rstrip()
            fh.readline()
            qual = fh.readline().rstrip()
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities

# run
			
seqs, quals = readFastq(sys.argv[1])

# (2)
def phred33ToQ(qual):
    return ord(qual) - 33

def creatHist(qualities):
    hist = [0] * 50
	for qual in qualities:
        for phred in qual:
            q= phred33ToQ(phred)
            hist[q] += 1
	return hist

h = creatHist(quals)
print h

# (3)
plt.bar(range(len(h)), h)
plt.show()
