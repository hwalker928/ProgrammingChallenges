import random
import sys
import string

length = input("Length: ")
length = int(length)
if length > 1000:
    print("\nAre you mad?")
    sys.exit()
password_characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(password_characters) for i in range(length))
print(f"\nYour password is:\n{password}")
