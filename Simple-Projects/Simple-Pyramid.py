def pypart(n):
    for i in range (0,n):
        for j in range (0,i+1):
            print("*",end=" ")
        print("\r")

print("Enter the size of pyramid:\n")
n = int(input("Enter the value for size of pyramid:\n"))
pypart(n)