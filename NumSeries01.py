def PrintNumber(N, Original, K, flag): 
    #print the number 
    print(N, end = " ") 
      
    # change flag if number 
    # become negative 
      
    if (N <= 0): 
        if(flag==0): 
            flag = 1
        else: 
            flag = 0
          
    # base condition for 
    # second_case (Adding K) 
      
    if (N == Original and (not(flag))): 
        return
      
    # if flag is true 
    # we subtract value until 
    # number is greater then zero 
      
    if (flag == True): 
        PrintNumber(N - K, Original, K, flag) 
        return
      
    # second case (Addition ) 
    if (not(flag)): 
        PrintNumber(N + K, Original, K, flag); 
        return
      
N = int(input("Enter the element:"))
K = 5
PrintNumber(N, N, K, True) 
