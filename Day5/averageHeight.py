student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total = 0
# for i in range(len(student_heights)):
#    total += student_heights[i]
for height in student_heights:
    total += height
print(round(total/len(student_heights)))
