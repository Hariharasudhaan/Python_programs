l=[]
a=[0]
c=0
n=int(input("Enter the number:"))
temp=n
while(temp!=0):
    z=temp%2
    l.append(z)
    temp=temp//2
l.reverse()
print(l)
for i in range(0,len(l)):
    c=0
    if(l[i]==1):
        for i in range(i+1,len(l)):
            if(l[i]==0):
                c=c+1
                continue
            if(l[i]==1):
                a.append(c)
                break    

print(max(a))
    
