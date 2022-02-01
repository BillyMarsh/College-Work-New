import pymongo
from random import randint
import time
# Connecting to the Mongo Database via the mongo string
myclient = pymongo.MongoClient("mongodb://82.24.77.18:25569/")

# Setting which Database we want to work with and what collection to work in
mydb = myclient["College"]
mycol = mydb["Duncan"]


def addProduct(productID, name, department, location, quantity, incvat, exvat):
  t = {"productID": productID, "name": name, "department": department, "location": location, "quantity": quantity, "IncVat": incvat, "ExVat": exvat}
  mycol.insert_one(t)
  print("Inserted Information into Database")

start= time.time()
#for i in range(1, 7500):
#  t = randint(134, 1235235)
#  t2 = randint(134, 123325)
#  t3 = randint(134, 1233)
#  addProduct(i, "Test19"+str(i), "New Department", "UK", t3, t, t2)
#end = time.time()
#print(str(end-start)+" Seconds")

for x in mycol.find({"productID": 1303}):
  remove = "{", "}", "'"
  for i in remove:
    x = str(x).replace(i, "")
  x = str(x).split(",")
  ID = str(x[0]).split(":")
  productID = str(x[1]).split(":")
  name = str(x[2]).split(":")
  department = str(x[3]).split(":")
  location = str(x[4]).split(":")
  quantity = str(x[5]).split(":")
  incvat = str(x[6]).split(":")
  exvat = str(x[7]).split(":")

  print("Information About Product: (ID:", ID[1],")")
  print(" - ID:", ID[1])
  print(" - Product ID:", productID[1])
  print(" - Name:", name[1])
  print(" - Department", department[1])
  print(" - Location:", location[1])
  print(" - Quantity:", quantity[1])
  print(" - Price (inc Vat):", incvat[1])
  print(" - Price (ex Vat", exvat[1])
  print("")

def findDocAmount():
  num = 0
  for x in mycol.find():
    num = num + 1
  return num

print(findDocAmount())
