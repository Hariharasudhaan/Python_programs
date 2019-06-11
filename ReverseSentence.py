s=input("Enter a String:")      #Getting String from the User
l=s.split(' ')                  #Split the String into List
z=l[-1::-1]                     #Reverse thr List
z=' '.join(z)                   #Join the Reversed String
print(z)
