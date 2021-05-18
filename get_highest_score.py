students = [{"Name": "Reddmar", "Score": 200},{"Name": "Francisco", "Score": 30},{"Name": "Ricardo", "Score": 50}]
highest_score, counter , names, scores = 0, 0, [], []


max(students, key=students.get)
"""for student in students:
    for k, v in student.items():
        if k == 'Score':
            scores.append(v)
            highest_score = max(scores)
        elif k == 'Name':
            names.append(v)

for i in scores:
    if i ==  highest_score:
        counter +=1

print(names[counter])"""