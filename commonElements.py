n1=int(input("Enter Size of an array 1:"))          #getting Size of an Array 1
a1=[]
for i in range(0,n1,1):                           #Loop for getting Array 1
    z1=int(input("Enter the element:"))
    a1.append(z1)
n2=int(input("Enter Size of an array 2:"))          #getting Size of an Array 2
a2=[]
for i in range(0,n2,1):                           #Loop for getting Array 2
    z2=int(input("Enter the element:"))
    a2.append(z2)
n3=int(input("Enter Size of an array 3:"))          #getting Size of an Array 3
a3=[]
for i in range(0,n3,1):                           #Loop for getting Array 3
    z3=int(input("Enter the element:"))
    a3.append(z3)
for i in range(0,n1,1):                           #Loop for Finding Common Elements ia all Three Array's
    if(a1[i] in a2 and a1[i] in a3):
        print(a1[i])

