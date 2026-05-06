digits = [65,69,79,73,85]

char = input("Enter a single character : ")

ascii=ord(char)

if ascii in digits:
    print("Vowel")
else:
    print("Consonent")