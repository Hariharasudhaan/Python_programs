n=int(input("Enter the no of houses:"))         #Enter Number of Houses
amt=int(input("Enter the amount:"))             #Enter the Amount
total=0
for i in range(1,n+1,2):                        #Loop for finding the Max Amount
    total=total+amt
print(total)
