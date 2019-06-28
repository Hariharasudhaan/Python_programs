n=int(input("Enter the Number:"))     #Getting the Element
count=0
for i in range(0,n+1,1):
    temp=i                            #Assigning Each value in Temp
    while(temp!=0):
        if(temp%2==1):
            count=count+1
        temp=temp/2
print(count)                          #print the Count
