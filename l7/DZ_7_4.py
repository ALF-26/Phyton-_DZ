#assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

def common_elements():
    set_3 = {i for i in range(100) if i % 3 == 0}
    set_5 = {i for i in range(100) if i % 5 == 0}
    intersection = set_3 & set_5
    return intersection

result = common_elements()

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")

print(result)