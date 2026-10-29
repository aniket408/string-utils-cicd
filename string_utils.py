def reverse_string(text):
    return text[::-1]

def to_uppercase(text):
    return text.upper()

def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]