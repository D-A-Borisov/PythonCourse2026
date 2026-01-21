string = input()

result = ""
last_char = ""

for char in string:
    if char == ' ':
        if last_char:
            result += last_char
            last_char = ""
    else:
        last_char = char

if last_char:
    result += last_char

print(result)
