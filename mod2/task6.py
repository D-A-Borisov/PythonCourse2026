string = input()

count_0 = 0
count_1 = 0

for char in string:
    if char == '0':
        count_0 += 1
    elif char == '1':
        count_1 += 1

if count_0 == count_1:
    print('yes')
else:
    print('no')
