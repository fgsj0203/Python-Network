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

# ---------------------------------------------------------------------------------------------------
# Logic code for first file you value hash
# Defined algorithm used for hash file one
hash1 = hashlib.new("ripemd160")  # Ripemd160 is algorithm of 160 bits
# Method "update" is compare of hashes
# parameter "rb" is read in mode binary
hash1.update(open(fileOne, "rb").read())
# ---------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------
# Logical code for second file you value hash
hash2 = hashlib.new("ripemd160")  # Ripemd160 is algorithm of 160 bits
# Method "update" is compare of hashes
# parameter "rb" is read in mode binary
hash2.update(open(fileTwo, "rb").read())

# ---------------------------------------------------------------------------------------------------


# Structure conditional Checking values of hashes in files
# Function "digest" resume datas of method update returned of hash
if hash1.digest() != hash2.digest():
    print(f"The file: {fileOne} is different of file: {fileTwo}")
    # Method "hexdigest" return value in format hexadecimal
    # Printing values of hash two files
    print("The value hash of file one is: ", hash1.hexdigest())
    print("The value hash of file two is: ", hash2.hexdigest())
else:
    print(f"the file: {fileOne} is equal a the file: {fileTwo}")
    # Printing values of hash two files
    print("The value hash of file one is: ", hash1.hexdigest())
    print("The value hash of file two is: ", hash2.hexdigest())

# ---------------------------------------------------------------------------------------------------
