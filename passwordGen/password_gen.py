import random

# Created the Character list
characters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
    '8', '9', '!', '#', '$', '%', '&', '(', ')', '*', '+'
]

# User input
n_characters = int(input("How many characters do you want in your password? "))

password_list = []

for i in range(n_characters):
  char = random.choice(characters)
  password_list += char

# the suffle function for more randomness
random.shuffle(password_list)

password = ""
for i in password_list:
  password += i
print(password)


