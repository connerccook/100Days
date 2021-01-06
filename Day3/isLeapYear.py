isLeap = False

year = int((input("Which year do you want to check: ")))

if(year % 4 == 0):
    isLeap = True
    if(year % 100 == 0):
        isLeap = False
        if(year % 400 == 0):
            isLeap = True

if(isLeap):
    print(f"Year {year} is a leap year")
else:
    print(f"Year {year} is not a leap year")
