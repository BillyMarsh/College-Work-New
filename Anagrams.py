def anagrams(string1, string2):
    if sorted(string1.lower()) == sorted(string2.lower()):
        print("Anagrams")
    else:
        print("Not")

anagrams("Test dd", "seTt dd")
