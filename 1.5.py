char = input("Enter a character: ")  
  
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  
  
if char in vowels:  
    print(f"The character '{char}' is a vowel!")  
else:  
    print(f"The character '{char}' is a consonant!")  