"""
Author = Francisco Gomes
Date = 09/02/2022
Project = Create comparator of values Hashes
version = 1.0
"""

# Importing libraries
import hashlib


# Variables with values of file created
fileOne = "file1.txt"
fileTwo = "file2.txt"

# Defined algorithm used for hash file one
hash1 = hashlib.new("ripemd160") # Ripemd160 is algorithm of 160 bits

# Method "update" is comparate of hashes
# parameter "rb" is read in mode binary
hash1.update(open(fileOne, "rb").read())

hash2 = hashlib.new("ripemd160")

hash2.update(open(fileTwo, "rb").read())

#Checking values of hashes in files
#Function digest resume datas of method update
if hash1.digest() != hash2.digest():
    print(f"The file: {fileOne} is different of file: {fileTwo}")
else:
    print(f"the file: {fileOne} is equal a the file: {fileTwo}")
