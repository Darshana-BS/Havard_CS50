#appraoch1
students = ['a', 'b', 'c']
print(students[0])
print(students[1])
print(students[1])
print('1======================')

#approach2
for student in students:
    print(student)
print('2======================')

#approach3
for i in range(len(students)):
    print(students[i])
    #approach3(a)
    print(i+1, students[i])
print('3======================')

#approach4
students2 = ['Hermione', 'Harry', 'Rom', 'Draco']
houses = ["Gryfffindor", "Griffindor", "Grinffindor", "Slytherin"]

#apprach4(a)
students2 = {"Hermione:Gryfffindor", "Harry:Gryffindor","Rom:Grinffindor", "Draco:Slytherin" }
students2 = {
    "Hermione":"Gryfffindor",
    "Harry":"Gryffindor",
    "Rom":"Grinffindor",
    "Draco":"Slytherin" 
}

print(students2["Hermione"])
print(students2["Harry"])
print(students2["Rom"])
print(students2["Draco"])

#approach4(b) iterate over the keys
for new_student in students2:
    print(new_student, students2[new_student], sep=', ')

print('4======================')

#approach5
students4 = [
    {"name":"Hermione","house":"Gryfffindor","patronus":"Otter"},
    {"name":"Harry", "house":"Gryfffindor", "patronus":"Stag"},
    {"name":"Ron", "house":"Gryfffindor", "patronus":"Jacl Russell terrier"},
    {"name":"Draco", "house":"Slytherin", "patronus":None}
]

for students44 in students4:
    print(students44["name"], students44["house"], students44["patronus"])