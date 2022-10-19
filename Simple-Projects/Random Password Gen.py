import random
# Max lenght of paasword is 75
passlen = int(input("enter the length of password:"))
s ="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p =  "".join(random.sample(s,passlen ))
print ("Your Password is :\n")
print (p)