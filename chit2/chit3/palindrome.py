def is_palindrome(text):
    reversed_text = text[::-1]
    if text == reversed_text:
        return True
    else:
        return False

# Main program
word = input("Enter a string: ")

result = is_palindrome(word)

if result:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
