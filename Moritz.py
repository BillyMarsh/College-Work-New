from prettytable import PrettyTable 
  

myTable = PrettyTable([" ", "List", "Array", "Tuple"]) 
  

myTable.add_row(["Is it mutable?", " ", " ", " "]) 
myTable.add_row(["Can we change the size after creation?", " ", " ", " "]) 
myTable.add_row(["Can items in the list be changed?", " ", " ", " "]) 
myTable.add_row(["How many different types of data can be stored", " ", " ", " "]) 

  
print(myTable)
