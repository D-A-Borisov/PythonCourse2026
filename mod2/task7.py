string = input()
s = string[:string.find(",")]
i = string[string.find(",") + 1]

count = 0
index = 0
while s[index] == i:
    count += 1
    index += 1

print(count)
