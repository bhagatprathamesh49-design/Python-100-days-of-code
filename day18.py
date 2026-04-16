sentence = input("Enter a Sentence: ")
vowels = 0
consonants = 0

for letter in sentence:
    if letter in "aeiouAEIOU":
        vowels = vowels + 1
    elif letter.isalpha():
        consonants = consonants + 1

print("Number of Vowels:", vowels)
print("Number of Consonants:", consonants)
