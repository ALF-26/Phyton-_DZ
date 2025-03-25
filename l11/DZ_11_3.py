def is_even(digit: int) -> bool:
    return int(str(digit)[-1]) in range(0, 9, 2)

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
assert is_even(0) == True, 'Test4'

print('OK')