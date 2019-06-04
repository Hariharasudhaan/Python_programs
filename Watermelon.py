n=int(input("Enter weight of the watermelon:"))         #Getting Weight from the User
a=b=0                                                   #Inistialization
if(n>=1 and n<=100):
    if(n%2==0 and n!=2):
        z=n//2                                          #Splitting into Two Halves
        if(z%2!=0):                                     #If the value is odd,Convert the Splitted values into even value with Minimum difference
            a=z+1
            b=z-1
            print(a,b)
        else:
            a=b=z                                       #Assign Spiltted value to Both a and b
            print(a,b)
    else:
        print("Unable to Share")
else:
    print("Enter a weight b\w 1 to 100")
