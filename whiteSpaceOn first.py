count=0
s=input("Enter the string:")            #Getting String from the User
l=s.split(' ')                          #Converting string into List
for i in s:
    if(i==" "):
        count=count+1                   #Loop for Counting Number of Words
x="".join(l)
z=x.split(',')
for i in range(0,count,1):              #Loop for Inserting White Spaces
    z.append(" ")
z.reverse()                             #Reversing the string
a="".join(z)                            #converting back from String to List
print(s)
print(a)
