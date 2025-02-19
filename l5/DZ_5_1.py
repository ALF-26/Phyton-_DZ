import string
import keyword

var_name = input()

if (var_name[0].isdigit() or
    any (i.isupper()for i in var_name) or
    any(char in string.punctuation for char in var_name) and '_' not in var_name or
    var_name in keyword.kwlist or
    ' ' in var_name or
    var_name.count("_") > 1):
    print(False)
else:
    print(True)