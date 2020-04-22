#!/usr/bin/env python3
# read chr  - cwcoleman

with open("wordlist.10000.txt") as fileobj:
    for line in fileobj:
       for ch in line:
           print (ch)

fileobj.close()

'''
https://www.mit.edu/~ecprice/wordlist.10000

with open("filename") as fileobj:
    for line in fileobj:
       for ch in line:
           print ch
'''
