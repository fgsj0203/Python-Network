import random, string

sizePassword = 16  # Best practice for size password

#Method ascii_letters using lower case and Upper Case
#String digits with numbers between 0 and 9
chars = string.ascii_letters + string.digits + "!@#$%&*()-=+,.;?][ç" # Receiving structure of password generate

passwordRandom = random.SystemRandom() # function SystemRandom using other library (OS) urandom

print("".join(passwordRandom.choice(chars) for i in range(sizePassword)))




