"""
Author = Francisco Gomes
Date = 08/02/2022
Project = Create generator password strong with best practices of CyberSecurity
"""

# Importing libraries used in project
import random, string


# Variable of size password for best practices cybersecurity
sizePassword = 16

# Method ascii_letters using lower case and Upper Case
# String digits with numbers between 0 and 9
# Concatenated letters, numbers and character special
chars = string.ascii_letters + string.digits + "!@#$%&*()-=+,.;?][ç" # Receiving structure of password generate

passwordRandom = random.SystemRandom() # function SystemRandom using other library (OS) "urandom"

# Printing password generated with parameters
print("".join(passwordRandom.choice(chars) for i in range(sizePassword)))




