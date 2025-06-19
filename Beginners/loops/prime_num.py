n = 13

if n == 1:
    print("This is neither Prime nor Composite")
else:
    flag = 0
    for i in range(2, n):
        if n % i == 0:
            flag += 1
        
        if flag != 0:
            print("Not Prime")
            exit()
    
    print("Prime")
    
    
            
        


