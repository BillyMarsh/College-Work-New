import pymongo

# Connecting to the Mongo Database via the mongo string
myclient = pymongo.MongoClient("mongodb://mongoip:mongoport/")

# Setting which Database we want to work with and what collection to work in
mydb = myclient["College"]
mycol = mydb["Cher"]

# Checking if the database is there, otherwise quitting
dblist = myclient.list_database_names()
if "College" in dblist:
  print("The database exists.")
else:
  quit()

# Adds the default project which will have extra information added to with each project
def addProject(name, deadline, client, price):
  num = 0
  for x in mycol.find():
    num = num + 1
  num = num + 1
  t = { "_id": num, "project_name": name, "deadline": deadline, "client_name": client, "price": price}
  mycol.insert_one(t)
  print("Inserted Information into Database (ID: " + str(num) + ")")
  return num



# Function which when called adds a website project to the database
def addWebsite(name, deadline, client, price, server, pages):
  
 # Get webID from addProject returning the ID of the mongo document
  webID = addProject(name, deadline, client, price)

 # Find document by looking up ID returned from addProject()
  myquery = { "_id": webID}
  mydoc = mycol.find(myquery)

  # Looping through documents to get the correct one from the query
  for x in mydoc:
  
    # Setting our new value to add and then updating our document (One at a time)
    newvalues = { "$set": { "server": server } }
    mycol.update_one(x, newvalues)

    newvalues = { "$set": { "pages": pages } }
    mycol.update_one(x, newvalues)

    newvalues = { "$set": { "Project": "WEB" } }
    mycol.update_one(x, newvalues)

    print("Updated Info (" + str(webID) + ")")


# Function which when called adds a game project to the database
def addGame(name, deadline, client, price, platform, genre):
  
 # Get webID from addProject returning the ID of the mongo document
  webID = addProject(name, deadline, client, price)

 # Find document by looking up ID returned from addProject()
  myquery = { "_id": webID}
  mydoc = mycol.find(myquery)

  # Looping through documents to get the correct one from the query
  for x in mydoc:
  
    # Setting our new value to add and then updating our document (One at a time)
    newvalues = { "$set": { "platform": platform } }
    mycol.update_one(x, newvalues)

    newvalues = { "$set": { "genre": genre } }
    mycol.update_one(x, newvalues)

    newvalues = { "$set": { "Project": "GAME" } }
    mycol.update_one(x, newvalues)

    print("Updated Info (" + str(webID) + ")")


# Function which when called adds a mobile game project to the database
def addApp(name, deadline, client, price, type):
  
 # Get webID from addProject returning the ID of the mongo document
  webID = addProject(name, deadline, client, price)

 # Find document by looking up ID returned from addProject()
  myquery = { "_id": webID}
  mydoc = mycol.find(myquery)

  # Looping through documents to get the correct one from the query
  for x in mydoc:
  
    # Setting our new value to add and then updating our document
    newvalues = { "$set": { "type": type } }
    mycol.update_one(x, newvalues)
    newvalues = { "$set": { "Project": "APP" } }
    mycol.update_one(x, newvalues)
    print("Updated Info (" + str(webID) + ")")


# Debug tools (Test creating each option)

#addWebsite("Cool Website", "1 Week", "Billy Marsh", 1000, "Server 1", 5)
#addGame("Cool Game", "1 Week", "Billy Marsh", 1000, "Xbox", "FPS")
#addApp("Cool Mobile Game", "1 Week", "Billy Marsh", 1000, "IOS")

# Defining menu for taking inputs for a Website Project
def websiteMenu():
  print("")
  print(" - Website Menu - ")
  print("")
  print("Answer Questions Below To Add:")
  name = input("  - What is the name of the website: ")
  timeframe = input("  - Enter a timeframe for this website: ")
  clientname = input("  - Enter clients name: ")
  price = int(input("  - Enter price of project (e.g: 1000): "))
  serverloc = input("  - Enter server location: ")
  pagenum = int(input("  - Enter number of pages: "))
  addWebsite(name, timeframe, clientname, price, serverloc, pagenum)

# Defining menu for taking inputs for a Game Project
def gameMenu():
  print("")
  print(" - Game Menu - ")
  print("")
  print("Answer Questions Below To Add:")
  name = input("  - What is the name of the game: ")
  timeframe = input("  - Enter a timeframe for this game: ")
  clientname = input("  - Enter clients name: ")
  price = int(input("  - Enter price of project (e.g: 1000): "))
  platform = input("  - Enter platform for project: ")
  genre = input("  - Enter genre of the project: ")
  addGame(name, timeframe, clientname, price, platform, genre)

# Defining menu for taking inputs for a Mobile App Project
def appMenu():
  print("")
  print(" - Mobile App Menu - ")
  print("")
  print("Answer Questions Below To Add:")
  name = input(" What is the name of the mobile game: ")
  timeframe = input("  - Enter a timeframe for this mobile game: ")
  clientname = input("  - Enter clients name: ")
  price = int(input("  - Enter price of project (e.g: 1000): "))
  type = input("  - Enter type of mobile (e.g IOS / Android): ")
  addApp(name, timeframe, clientname, price, type)

# Get all website projects from the database
def listallWebsiteProjects():
  myquery = { "Project": "WEB"}
  mydoc = mycol.find(myquery)

  # Looping through all documents of web projects
  count = 0
  print("")
  for x in mydoc:
    count = count + 1
    remove = "{", "}", "'"
    for i in remove:
      x = str(x).replace(i, "")
    x = str(x).split(",")
    webID = str(x[0]).split(":")
    project_name = str(x[1]).split(":")
    deadline = str(x[2]).split(":")
    client_name = str(x[3]).split(":")
    price = str(x[4]).split(":")
    server = str(x[5]).split(":")
    pages = str(x[6]).split(":")
    print(str(count) + ")" + " ID:" + str(webID[1]) + " | Project Name:" + project_name[1] + " | Deadline:" + deadline[1] + " | Client Name" + client_name[1] + " | Price: £" + str(price[1]) + " | Server" + server[1] + " | Number of Pages" + pages[1])
    
    

def projectMenu():
  print("")
  print(" - Project Menu - ")
  print("")
  print("1) Website Projects")
  print("2) Game Projects")
  print("3) Mobile App Projects")
  num = int(input("Enter the number of your option:  "))
  if num == 1:
    listallWebsiteProjects()
  if num == 2:
    gameMenu()
  if num == 3:
    appMenu()

# Defining main menu to decide what project to add
def mainMenu():
  print("")
  print(" - Main Menu - ")
  print("")
  print("1) Add Website Project")
  print("2) Add Game Project")
  print("3) Add Mobile Game Project")
  print("4) See Project Menu")
  num = int(input("Enter the number of your option:  "))
  if num == 1:
    websiteMenu()
  if num == 2:
    gameMenu()
  if num == 3:
    appMenu()
  if num == 4:
    projectMenu()


while True:
  mainMenu()
