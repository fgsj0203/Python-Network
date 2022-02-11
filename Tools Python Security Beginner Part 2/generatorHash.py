#importing libraries
import hashlib
string = input("Enter a text this is generate hash: ")

menuHash = int(input("""### Menu - Select type of hash
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
                Input a number of type hash selected: """))


if menuHash == 1:
    result = hashlib.md5(string.encode("utf-8"))
    print("The hash MD5 of string is: ", string, " is ", result.hexdigest())

elif menuHash == 2:
    result = hashlib.sha1(string.encode("utf-8"))
    print("The hash SHA1 of string is: ", string, " is ", result.hexdigest())

elif menuHash == 3:
    result = hashlib.sha256(string.encode("utf-8"))
    print("The hash SHA256 of string is: ", string, " is ", result.hexdigest())

elif menuHash == 4:
    result = hashlib.sha512(string.encode("utf-8"))
    print("The hash SHA512 of string is: ", string, " is ", result.hexdigest())

else:
    print("Error, try again")