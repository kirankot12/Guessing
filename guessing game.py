import random 
try:
    the_number = random.randint(1, 11)
    guess = int(input("guess a number between 1 and 11 "))
    while guess != the_number:
        if guess >the_number:
            print (guess, f"was way too high, the answer was {the_number}")
        if guess < the_number:
            print (f"the guess was too low, the answer was {the_number}")
        
        guess = int(input("try again"))
    print (guess, "was correct")
except:
    guess = (str) or ValueError or NameError
    print("these gueses are invalid, please try again")
