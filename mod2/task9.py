phone = input()
result = ""

for char in phone:
    if char not in ['-', ' ', '(', ')']:
        result += char

print(result)
