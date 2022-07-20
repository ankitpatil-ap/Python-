"""python has builtin function open() a file
this function returns a file
return objectwe can specify the mode while opening a file  In mode , we specify whether we
    want to read 'r' write 'w' or append 'a' to file

with open('filename.txt', 'w') as fileObject:
"""

f= open('data.txt', 'r' ) #this is not recommended as it does not close the file by itself so we use with open
#by deafualt its in read mode

"""print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
"""
for line in f:
    print(line)

f.close()

#*****************************************************************

with open('data.txt') as f: #it auto close the file
    for line in f:
        print(line)
    #print(f.read())  #it reads complete file.
    print(f.read(4))  #it reads 3 charecter.
students = ["ankit", "patil", "Raghav", "A"]
with open('data1.txt','w') as f:  #it create new file and if file exists already then it delte its complete data and write this
    f.write("Ankit")
    f.writelines((students))

with open('data2.txt', 'a') as f: #it created new file or file exists then apped data at the end of file
    f.write("Ankit")
    f.writelines((students))
    f.write("Ap")
