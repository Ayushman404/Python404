#Keep asking for input from user until they give number b/w 1 to 10

while True:
    
    try:
        n = int(input("Enter the Number: "))
    except ValueError:
        print("Please Enter an Integer")
    else:
        if 1 <= n <= 10:
            print("Input Validated!")
            break
        else:
            print("Enter Number b/w 1 to 10")  

    
    
    