#while
i = 2
while i <= 10:
    print(i * "*")
    i = i + 1

i = 5
while i >= 0:
    print(i * "*")
    i = i - 1

# for loops

for item in range(20):
    print(item)
#  list

marks = [95, 50, 30]
print(marks[-0])


marks = [95, 50, 30]
print(marks[1:3])


#append
marks = [95, 50, 30]

marks.append(993)

print(marks)


#insert

marks = [95, 50, 30]

marks.append(993)

print(marks)


#

marks = [95, 50, 30]

marks.append(993)

print( 95 in marks)

#length

marks = [95, 50, 30]

marks.append(993)

print(len(marks))

#break and continue

students = ["sameer","tofik","sahil","aarif","majid"]

for students in students:
    if students == "majid":
        break;
    print(students)


# continue

students = ["sameer","tofik","sahil","aarif","majid"]

for students in students:
    if students == "majid":
        continue;
    print(students)

#tuple (not changable)

marks = [95, 50, 30]
print(marks.index(30))


# list[],
#tuple()
#set {} unique value stor only


#dictionary
marks ={"english": 95, "chemistry" : 98}

print(marks["chemistry"])
marks["physics"] = 40;
print(marks)

marks["physics"] = 99;
print(marks)

#functions
# in built functions
# module funcitons
# user-defined fuctions

import math
print(dir(math))

#square

from math import sqrt
print(sqrt(16))

#user defined function
# def function_name(parameters):
 #//do something

def print_sum(first, second):
    print(first + second)

print_sum(5, 9)


def print_sum(first, second=5):
    print(first + second)

print_sum(5)