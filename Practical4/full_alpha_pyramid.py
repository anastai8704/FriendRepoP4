import string
letters = string.ascii_uppercase

for i in range(1, 6):
    print(" ".join(letters[:i]))
