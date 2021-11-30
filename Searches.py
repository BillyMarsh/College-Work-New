import time
import random

default_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def randomListSearch(lists, x):
  # Setting Loop To true so that it will start the while loop
    needToLoop = True
  # Getting our starting time so that we can work out how long it takes to complete
    start = time.time()

  # As we have started the loop it will repeat unil we get x
    while needToLoop == True:
  # Picking a random number so that we can compare it to the number we are looking for
      pickedNumber = random.choice(range(1, len(lists)-1))
  # Printing and stopping the loop if x has been found
      if pickedNumber == x:
        needToLoop = False
  # Setting the end time so that we can work out the end - start = time taken to find
    end = time.time()
  # Printing how long it took to find the number
    print("Took ", end - start, " to find ", x)


def linearListSearch(lists, x):
  # Setting Loop To true so that it will start the while loop
  start = time.time()

  # Looping all numbers which are in the list given in the function
  for num in lists:
  # Checking if the number of the list is the same as the number it is looking for
    if num == x:
  # If it is the number, it will break and end the loop
      break

  # Setting the end time so that we can work out the end - start = time taken to find
  end = time.time()
  # Printing how long it took to find the number
  print("Took ", end - start, " to find ", x)


def binaryListSearch(lists, x, min, max):
    if max >= min:
        mid = round((max + min) / 2)
        if mid == x:
            return(mid)
        elif mid > x:
            print(mid)
            return binaryListSearch(lists, x, min, mid - 1,)
        elif mid< x:
            print(mid)
            return binaryListSearch(lists, x, mid + 1, max)
    else:
        return -1

randomListSearch(default_list, 2)
linearListSearch(default_list, 7)
t = binaryListSearch(default_list, 4, 0, 15)
 
if t != -1:
    print("Found in List |", str(t))
else:
    print("Not found in list")
