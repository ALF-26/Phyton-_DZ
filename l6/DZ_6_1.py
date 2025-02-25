#"a-c" -> abc
#"a-a" -> a
#"s-H" -> stuvwxyzABCDEFGH
#"a-A" -> abcdefghijklmnopqrstuvwxyzA

import string

string_letters = input()

letters = string.ascii_letters

first, second = string_letters.split('-')
first_index = letters.index(first)
second_index = letters.index(second)

print(letters[first_index:second_index + 1])
