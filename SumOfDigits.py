n=int(input("Enter a number:"))
temp=n
sum=0
while(temp>0):
      z=temp%10
      sum=sum+z
      temp=temp//10
print(sum)
