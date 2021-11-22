str1 = "Practice Problems to Drill List Comprehension in Your Head."

def numberOfSpace(str1):
  list_spaces = [i for i in str1 if i == " "]
  list_spaces_num = len(list_spaces)
  return list_spaces_num


def removeVowel(text):
  return "".join([text for text in text if text not in "aeiouAEIOU"])

def lessThanFive(str1):
    list_five = str1.split(" ")
    list_under = [i for i in list_five if len(i) < 5]
    return list_under


print(removeVowel(str1))
print(numberOfSpace(str1))
print(lessThanFive(str1))
