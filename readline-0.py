#!/usr/bin/env python3

inFile = open("wordlist.10000.txt", "r")
line = inFile.readline()
while line:
    if (len(line) < 4):
        print(line)
    line = inFile.readline()

inFile.close()

'''
https://www.mit.edu/~ecprice/wordlist.10000
'''
