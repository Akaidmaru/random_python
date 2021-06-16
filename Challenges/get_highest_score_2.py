students = [
{"Name": "Reddmar", "Score": 93},
{"Name": "Francisco", "Score": 95},
{"Name": "Ricardo", "Score": 97}
]
name, score, highest_score, counter_1, counter_2 = [] , [], 0, 0, 0

for student in students:
    for j, k in student.items():
        if j == 'Name':
            name.append(k)
        elif j == 'Score':
            score.append(k)

for i in score:
    if i >= highest_score:
        highest_score  = i
        counter_1 += 1

for i in range(0, counter_1 + 1):
    counter_2 += 1
    if counter_2 == counter_1:
        print(name[counter_2-1])