keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dictionary = dict(zip(keys,values))

print(dictionary)


sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
  
}
keysToRemove = ["name", "salary"]


for i in keysToRemove:
    sampleDict.pop(i)
print(sampleDict)


sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}




sampleDict["location"] = sampleDict.pop("city")

print(sampleDict)
