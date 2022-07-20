marks = [100,97,69,88,"science"]
print(marks)
#[100, 97, 69, 88, 'science']
print(marks[4])
#science
print(marks[-2])
#88
print(marks[0:3])
#[100, 97, 69]
markss = [100,97,69,88]
for score in markss:
    print(score)

markss.append(99)
print(markss)
#[100, 97, 69, 88, 99]
marks.insert(2, 10000)
print(marks)
#[100, 97, 10000, 69, 88, 'science']
print(88 in marks)
#True
print(len(marks))
#6


i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1

marks.clear()
print(marks)
#[]


students = ["ankit", "patil", "Raghav", "A"]
for stud in students:
    if stud == "patil":
        break;
    print(stud)
#ankit
for stud in students:
    if stud == "patil":
        continue;
    print(stud)

"""""ankit
Raghav
A"""""

#we can modify append delete and many operatin can be perform on list