import csv

def write(test):
    with open('data.txt', 'w') as file:
        file.write(test + '\n')
        file.close()

    
def append(test):
    with open('data.txt', 'a') as file:
        file.write(test + '\n')
        file.close()

list1 = ["test", "test2", "test3"]

for i in list1:
    append(i)

write("Test Data 1")
append("Test Data 2")


import csv

with open("gamerscore.csv") as f:
    file = csv.reader(f)
    for row in file:
        print(" ".join(row))
