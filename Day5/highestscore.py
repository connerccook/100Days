student_scores = input("Input a lost of student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = student_scores[0]

for score in student_scores:
    if(score > highest_score):
        highest_score = score
print(highest_score)
