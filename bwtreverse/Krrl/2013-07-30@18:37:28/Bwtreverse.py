import sys

def ibwt(r, *args):
        first = "".join(sorted(r))
        count = [0]*256
        byteS = [-1]*256
        output = [""] * len(r)
        sCut = [None]*len(r)
        
        for i in range(len(r)):
                sCutIndex = ord(r[i])
                sCut[i] = count[sCutIndex]
                count[sCutIndex] += 1
                sCutIndex = ord(first[i])
                if byteS[sCutIndex] == -1:
                        byteS[sCutIndex] = i
 
        localI = (r.index("\x00") if not args else args[0])
        for i in range(len(r)):
                nextB = r[localI]
                output [len(r)-i-1] = nextB
                sCutIndex = ord(nextB)
                localI = byteS[sCutIndex] + sCut[localI]
        return "".join(output).rstrip("\x00")

f = open(sys.argv[1])

text = f.read()

text = text.split('\n')

for item in text:
    current = item.split(" ")
    print (ibwt(current[1], int(current[0])))