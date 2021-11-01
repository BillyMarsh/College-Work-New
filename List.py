# Original Lists

list1 = ["Billy", "is", "a", "Cool", "Cat"]
list2 = [10, 20, 30, 40, 50]

# Reversing Lists

list1.reverse()

# Merging Two Lists

listmerge = list1 + list2

# Squaring All Numbers In List

for i in range(len(list2)): 
    list2[i]=list2[i]**2

# Merging Two Lists With Zip

list3 = zip(list1, list2)
list3 = list(list3)

# Print Statements

print(list3)
print(list1)
print(listmerge)



