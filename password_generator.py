import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = int(input("Enter your password length (numbers only): "))

password = ""
for i in range(length):
    password += random.choice(characters)

print(password) 