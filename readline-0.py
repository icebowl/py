#!/usr/bin/env python3

inFile = open("words.txt", "r")
line = inFile.readline()
while line:
    print(line)
    line = inFile.readline()

inFile.close()

'''
https://www.mit.edu/~ecprice/wordlist.10000
'''
