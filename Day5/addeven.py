total = 0
for num in range(1, 101):  # end is not included
    if(num % 2 == 0):
        total += num
print(total)

total = 0
for num in range(2, 101, 2):
    total += num
print(total)
