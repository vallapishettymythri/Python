#Character Type Classification
#Write a Python code to check whether a character is an alphabet, digit or
#special character.
word=input("enter anything:")
if ('A'<=word <='Z') or ('a'<=word<='z'):
    print("Alphabet")
elif ('0' <= word <='9'):
    print("Digit")
else:
    print("Special character")