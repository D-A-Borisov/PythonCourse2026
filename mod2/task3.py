input_string = input()

index_first_space = input_string.find(" ")
index_second_space = input_string.find(" ", index_first_space + 1)

a = int(input_string[:index_first_space])
b = int(input_string[index_first_space+1:index_second_space])
c = int(input_string[index_second_space+1:])

if (a <= b <= c) or (c <= b <= a):
    result = b
elif (b <= a <= c) or (c <= a <= b):
    result = a
else:
    result = c

print(result)
