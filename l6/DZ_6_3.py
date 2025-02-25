#999 -> 2
#1000 -> 0
#423 -> 8
#33 -> 9
#25 -> 0
#1 -> 1
num = int(input())
while num > 9:
    result = 1
    for i in str(num):
        result = result*int(i)
    num = result
print(num)
