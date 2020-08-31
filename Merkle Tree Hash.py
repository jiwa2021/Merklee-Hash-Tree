#Assignment 5 OpenSSL
#Farhaan Jiwa and Ashlyn Schultz
#Modern Cryptography
#Professor Zheng
#April 12, 2020

#This code was written independently by the team.
#We ___Farhaan Jiwa and Ashlyn schultz____________ declare that I/We have completed this computer code completely and
#entirely on my/our own, without any consultation with others.

#I/We have read the UAB Academic Honor Code and understand that any breach of the Honor Code may result in severe penalties.	
#Student signature(s)/initials: ____FJ and AS________	
#Date: _____04/12/2020_______


import sys
import hashlib

# BUF_SIZE is totally arbitrary, change for your app!
day0 = "Day0.txt"
BUF_SIZE = 65536  #Read the file in this size.

sha = hashlib.sha256()  # Creation of the hash object

with open(day0, 'rb') as f:     # Open the file in read bytes format
        sha.update(f.read(BUF_SIZE))            # Update the hash

shahash = sha.hexdigest()       # Get the hexadecimal digest of the hash

print ("DAY 0 SHA256: ", shahash)       #Print the Hash.   The remainder of the code follows the same format.
#----------------------------------------------------------------------
day1 = "Day1.txt"

sha1 = hashlib.sha256()

with open(day1, 'rb') as f:
        sha1.update(f.read(BUF_SIZE))

sha1hash= sha1.hexdigest()

print ("Day 1 SHA256: ", sha1hash)
#----------------------------------------------------------------------
day2 = "Day2.txt"

sha2 = hashlib.sha256()

with open(day2, 'rb') as f:
        sha2.update(f.read(BUF_SIZE))

sha2hash= sha2.hexdigest()

print ("Day 2 SHA256: ", sha2hash)

#----------------------------------------------------------------------
day3 = "Day3.txt"

sha3 = hashlib.sha256()

with open(day3, 'rb') as f:
        sha3.update(f.read(BUF_SIZE))

sha3hash= sha3.hexdigest()

print ("Day 3 SHA256: ", sha3hash)

#----------------------------------------------------------------------
day4 = "Day4.txt"

sha4 = hashlib.sha256()

with open(day4, 'rb') as f:
        sha4.update(f.read(BUF_SIZE))

sha4hash= sha4.hexdigest()

print ("Day 4 SHA256: ", sha4hash)

#----------------------------------------------------------------------
day5 = "Day5.txt"

sha5 = hashlib.sha256()

with open(day5, 'rb') as f:
        sha5.update(f.read(BUF_SIZE))

sha5hash= sha5.hexdigest()

print ("Day 5 SHA256: ", sha5hash)

#----------------------------------------------------------------------
sha0_1 = hashlib.sha256()

sha0_1.update(bytes(shahash, 'utf-8') + bytes(sha1hash, 'utf-8'))
sha0_1hash= sha0_1.hexdigest()

print ("Day 0_1 SHA256: ", sha0_1hash)

#----------------------------------------------------------------------
sha2_3 = hashlib.sha256()

sha2_3.update(bytes(sha2hash, 'utf-8') + bytes(sha3hash, 'utf-8'))
sha2_3hash= sha2_3.hexdigest()

print ("Day 2_3 SHA256: ", sha2_3hash)

#----------------------------------------------------------------------
sha4_5 = hashlib.sha256()

sha4_5.update(bytes(sha4hash, 'utf-8') + bytes(sha5hash, 'utf-8'))
sha4_5hash= sha4_5.hexdigest()

print ("Day 4_5 SHA256: ", sha4_5hash)

#----------------------------------------------------------------------
sha01_23 = hashlib.sha256()

sha01_23.update(bytes(sha0_1hash, 'utf-8') + bytes(sha2_3hash, 'utf-8'))
sha01_23hash= sha01_23.hexdigest()

print ("Day 01_23 SHA256: ", sha01_23hash)

#----------------------------------------------------------------------
sha45_45 = hashlib.sha256()

sha45_45.update(bytes(sha4_5hash, 'utf-8') + bytes(sha4_5hash, 'utf-8'))
sha45_45hash= sha45_45.hexdigest()

print ("Day 45_45 SHA256: ", sha45_45hash)

#----------------------------------------------------------------------
sha012345 = hashlib.sha256()

sha012345.update(bytes(sha01_23hash, 'utf-8') + bytes(sha45_45hash, 'utf-8'))
sha012345hash= sha012345.hexdigest()

print ("Root Hash: Days 012345 SHA256: ", sha012345hash)







