import pymongo

# Add Your Own Mongo String

myclient = pymongo.MongoClient("mongodb://mongoip:port/")

mydb = myclient["Test"]
mycol = mydb["Menu"]

# Creating User

def addUserPass(info, user, password):
  num = 0
  for x in mycol.find():
    num = num + 1
  num = num + 1
  t = { "id": num, "information": info, "username": user, "pin": password, "balance": 0,"overdraft": 1000}
  mycol.insert_one(t)

# Find Username and Password via information mongo value

def searchByInfo(info):
  myquery = { "information": info }
  mydoc = mycol.find(myquery)
  for x in mydoc:
    print(x)

# Delete entire database of passwords

def deleteEntiredatabase():
  x = mycol.delete_many({})
  print(x.deleted_count, " documents deleted.")

# Get Username and Password from mongo string to display (From Mongo ID)

def getNameandDetailsByPin(mongoid):
  myquery = { "pin": mongoid }
  mydoc = mycol.find(myquery)
  for x in mydoc:
    return x

def getUsersName(mongoid):
  t = getNameandDetailsByPin(mongoid)
  remove = "{", ":"
  t2 = str(t).replace("'", "")
  for i in remove:
    t2 = str(t).replace(i, "")
  t2 = str(t).split(",")
  name = str(t2[3]).split(":")
  return name[1].replace("'", "")

def getUsersPassword(mongoid):
  t = getNameandDetailsByPin(mongoid)
  remove = "{", ":"
  t2 = str(t).replace("'", "")
  for i in remove:
    t2 = str(t).replace(i, "")
  t2 = str(t).split(",")
  passw = str(t2[4]).split(":")
  return passw[1]

def getUsersBalance(mongoid):
  t = getNameandDetailsByPin(mongoid)
  remove = "{", ":"
  t2 = str(t).replace("'", "")
  for i in remove:
    t2 = str(t).replace(i, "")
  t2 = str(t).split(",")
  balance = str(t2[5]).split(":")
  return balance[1]

  


def withdrawMoney(mongoid, amount):
  current_balance = getUsersBalance(mongoid)
  if int(current_balance) >= int(amount):
    new_balance = int(current_balance) - int(amount)
    myquery = { "balance": int(current_balance)}
    newvalues = { "$set": { "balance": int(new_balance) } }
    mycol.update_one(myquery, newvalues)
    print("Current Balance - £", current_balance)
    print("Removed - £", amount)
    print("New Money Available  - £", new_balance)
  else:
    print("Not Enough Money")

def depositMoney(mongoid, amount):
  current_balance = getUsersBalance(mongoid)
  new_balance = int(current_balance) + int(amount)
  myquery = { "balance": int(current_balance)}
  newvalues = { "$set": { "balance": int(new_balance) } }
  mycol.update_one(myquery, newvalues)
  print("Current Balance - £", current_balance)
  print("Deposited - £", amount)
  print("New Money Available - £", new_balance)



def passpin():
  count = 0
  while count <= 3:
    pin = int(input("Please Enter Your Pin: "))
    if pin == 1324:
      global pins
      pins = "1324"
      print("Access Given")
      break
    else:
      count = count + 1
      continue
  

passpin()

while True:

    print("-- ATM --")
    print("")
    print("Welcome To Your Bank", getUsersName(pins))
    print("")
    print("1) Deposit")
    print("2) Withdraw")
    print("3) Display Balance")
    print("4) Quit")
    print("")
    choice = int(input("Please Enter Number Choice: "))

    if choice == 1:
      print("-- ATM Deposit --")
      print("")
      amount = int(input("Enter The Amount To Deposit: "))
      depositMoney(pins, amount)
    
    elif choice == 2:
      print("-- ATM Withdraw --")
      print("")
      amount = int(input("Enter The Amount To Withdraw: "))
      withdrawMoney(pins, amount)

    elif choice == 3:
      print("-- ATM Display Balance --")
      print("")
      print(getUsersName(pins), "Has - £", getUsersBalance(pins))
    
    elif choice == 4:
      quit()

    else:
      continue
 


# Generate a new account:

#addUserPass("VISA Debit", "Billy Marsh", "1324")
