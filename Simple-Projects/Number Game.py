import random
import time
number = random.randint(1,10)
while True:
    user = int(input("guess the number: "))
    if user != number:
    	print("Your guess is incorrect try again")
    if user == number:
        print("Hurray!!")
        print(f"you guessed the number right it's {number}")
        time.sleep(2)
        break