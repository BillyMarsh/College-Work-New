listt = []
listtt = []
listttt = []
listtttt = []

for i in range(1, 1001): 
    listt.append(i)
print(listt)


listtt = [i for i in range(1, 1001)]
print(listtt)


listttt = [i for i in range(1, 1001) if i%8==0]
print(listttt)

listtttt = [i for i in range(1, 1001) if "6" in list(str(i))]
print(listtttt)
