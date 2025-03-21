import string


def first_word(text: str) -> string:
    for elem in text:
        if elem in string.punctuation and elem != "'":
            text = text.replace(elem, ' ')

    string_list = text.split()

    if string_list:
        return string_list[0]


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
assert first_word("...?, ") == None, 'Test7'

print('OK')