import sys
import string
def transform(ch, m):
	mx = 26 - (m % 26)
	if ch in string.uppercase:
		r = ( ( ( ord(ch) - ord('A') ) + mx ) % 26 ) + ord('A')
	elif ch in string.lowercase:	
		r = ( ( ( ord(ch) - ord('a') ) + mx ) % 26 ) + ord('a')
	else:
		r = ord(ch)
	return chr(r)
	
test_cases = open(sys.argv[1], 'r')
n = -1
for test in test_cases:
	if( len(test) > 0 ):
		if n == -1:
			n = int(test)
			ttab = [ transform(chr(i), n) for i in range(256) ] #tabella di trasformazione
			tstr = "".join(ttab)
		else:	
			test = string.rstrip(test, '\n\r')
			#l = len(test)
			#dec = [ ttab[ ord(test[i]) ] for i in range(l) ]
			#sdec = "".join(dec)
			sdec = string.translate(test, tstr)
			print sdec
test_cases.close()