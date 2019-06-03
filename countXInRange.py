X=int(input("Enter the value of X:"))
L=int(input("Enter the Lower limit:"))
U=int(input("Enter the Upper limit:"))
count=0
if (0 >= X or X <= 9):
    for i in range(L+1,U,1):
        a=i
        while(a>0):
            z=a%10
            if(z==X):
                count=count+1
            a=a//10
    print(count)
else:
    print("Enter b/w 0 to 9")
