list1 = ["Billy", "is", "a", "Cool", "Cat"]
list2 = [10, 20, 30, 40, 50]

list1.reverse()

listmerge = list1 + list2

print(list1)
print(listmerge)


for i in range(len(list2)): 
    list2[i]=list2[i]**2 
print(list2) 


list3 = zip(list1, list2)
list3 = list(list3)
print(list3)
