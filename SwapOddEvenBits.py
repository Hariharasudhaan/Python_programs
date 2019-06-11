n=int(input("Enter the Number:"))   #Getting a Number from the User 
l=[]
sum=0
while(n!=0):                        #loop for Finding Binary Number
    temp=n%2
    n=n//2
    l.append(temp)
l=l[-1::-1]                         #Reversing the Array
n1=len(l)
for i in range(0,n1-1,2):           #Loop for Swapping
    temp=l[i]
    l[i]=l[i+1]
    l[i+1]=temp
l=l[-1::-1]                         #Reversing the Array
for i in range(0,n1,1):
    sum=sum+(l[i]*(2**i))           #Coverting Binary to Eqivalent value
print(sum)
