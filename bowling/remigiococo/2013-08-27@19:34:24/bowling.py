import sys
import string
import time

def rawscore(c):
	if c == 'X':
		return 10
	elif c == '/':
		return 10
	elif c in string.digits:
		return int(c)
	else:
		return 0
		
raw = { '0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'X':10, '/':0 }		

#t1 = time.clock()
ooo=''
test_cases=open(sys.argv[1], 'r')
for test in test_cases:
	#if len(test) > 0:
	test = string.rstrip(test)
	s = string.split(test, ' ')
	score = 0
	st = 0
	frame = 0
	ls = len(s)
	#for i in xrange( ls ):
	#	s[i] = string.rstrip(s[i])
	#r = [raw[s[i]] for i in xrange(ls)]
	for i in xrange( ls ):
		cs = s[i]
		if cs == 'X':
			if frame < 10:
				score += 10
				if i < (ls-2):
					if s[i+2] != '/':
						score += raw[s[i+1]] + raw[s[i+2]]
					else:
						score += 10
				st = 0
				frame += 1
		elif cs == '/':
			if frame < 10:
				score += 10 - prev
				if i < (ls-1):
					score += raw[s[i+1]]
				st = 0
				frame += 1
		else:
			cur = int(cs)
			if frame < 10:
				score += cur
				prev = cur
				st += 1
				if st == 2:
					st = 0
					frame += 1
		#print '---', i, s[i], score
	#print score
	ooo += str(score) + '\n'
print ooo,	
test_cases.close()
#print 'elapsed: ', time.clock()-t1		