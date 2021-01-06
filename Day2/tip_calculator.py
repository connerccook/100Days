print("Welcome to the tip calculator")
bill = input("What was the total bill? ")
percentage = input(
    "What percentage tip would you like to give? 10, 12, or 15? ")
num_split = input("How many people to split the bill? ")

pay = (float(bill)/float(num_split)) * (1 + (int(percentage)/100))
pay = round(pay, 2)

print(f"Each person will pay: {pay}")
