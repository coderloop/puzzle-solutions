#!/usr/bin/python
# write your solution to helloworld
import sys

try:
    if (len(sys.argv) > 1):
        fo = open(sys.argv[1], 'r')
        print 'Hello World!'
        fo.close()
except IOError:
    print 'Hello World!'