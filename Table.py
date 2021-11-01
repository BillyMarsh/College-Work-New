from prettytable import PrettyTable 
  

myTable = PrettyTable([" ", "List", "Array", "Tuple"]) 
  

myTable.add_row(["Is it mutable?", "Yes", "Yes", "No"]) 
myTable.add_row(["Can we change the size after creation?", "Yes", "No", "No"]) 
myTable.add_row(["Can items in the list be changed?", "Yes", "Yes", "No"]) 
myTable.add_row(["How many different types of data can be stored", "All", "1", "All"]) 

  
print(myTable)
