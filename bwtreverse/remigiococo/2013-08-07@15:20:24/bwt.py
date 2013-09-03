import sys
import string


def bwt_decode(buf_in, buf_out, size, primary_index):

	F = [0 for i in range(size)]
	buckets = [0 for i in range(256)]
	indices =[0 for i in range(size)]

	for i in range(256):
		buckets[i] = 0
	for i in range(size):
		buckets[ord(buf_in[i])] = buckets[ord(buf_in[i])]+1
	k = 0
	for i in range(256):
		for j in range( buckets[i] ):
			F[k] = i
			k = k+1
	j=0		
	for i in range(256):
		while ( (j<size) and (i>F[j]) ):
			j = j+1
		buckets[i] = j; # it will get fake values if there is no i in F, but
												# that won't bring us any problems
	for i in range(size):
		indices[ buckets[ ord(buf_in[i]) ] ] = i;
		buckets[ ord( buf_in[i] ) ] = buckets[ ord( buf_in[i] ) ] + 1
	buf_out = ""
	j = indices[primary_index]
	for i in range(size):
		buf_out += buf_in[j]
		j=indices[j];
	print buf_out

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	if( len(test) > 0 ):
		test = string.rstrip(test, '\n\r')
		s = test.split(' ')
		if len(s) == 2:
			n = int(s[0]) # riga dove appare la stringa originale
			lc = s[1] # ultima colonna della BWT
			le = len(lc)
			r = ""
			bwt_decode(lc, r, le, n)
			#print r
			# ------
			#tab = [ lc[i] for i in range(le) ]
			#tab.sort()
			#for i in range(le-1):
			#	tab = [ lc[i]+tab[i] for i in range(le) ]
			#	tab.sort()
			#print tab[n]
test_cases.close()
