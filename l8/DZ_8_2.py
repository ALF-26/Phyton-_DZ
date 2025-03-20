import string

def is_palindrome(text):
    text = ''.join(char.lower() for char in text if
                   char not in string.punctuation and char != ' ')
    return text == text[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') is True, 'Test1'
assert is_palindrome('0P') is False, 'Test2'
assert is_palindrome('a.') is True, 'Test3'
assert is_palindrome('aurora') is False, 'Test4'

print("ОК")