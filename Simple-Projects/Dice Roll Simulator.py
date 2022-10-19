import random # First import the "random" func

# Create a infinte loop
while True:
     # Inputs for user     
     print(''' 1. roll the dice             2. exit     ''')

     # Actual interger input 
     user = int(input("what you want to do\n"))  
     
     # Using if-else to generate random numbers
     if user==1:
        # Random Number Generator Code         
        number = random.randint(1,6)        
        print(number) 

     # to Exit the Infinite Loop
     else:         
        break 