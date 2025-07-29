year = 4000

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"Year: {year}, Is a Leap Year")
else:
    print(f"Year: {year}, is NOT a Leap Year")