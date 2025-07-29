# calculate sum of even nums till a given number n 

n = int(input("Enter the value of n: "))

# n = 6

sum = 0

for num in range(1, n+1):
    if not num % 2:
        sum += num

print(f"The Sum of all the even numbers till {n} is {sum}")
        

