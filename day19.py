word = input("Enter a word: ")
cleaned = word.replace(" ", "").lower()
reversed_word = cleaned[:: -1]

if cleaned == reversed_word:
    print(f"Wow! {word} it's a Palindrome!")
else:
    print(f"{word} is NOT a Palindrome!")
    
