domain = input()

index = domain.find(".")
result = ""

while index != -1:
    level = domain[:index]
    if result:
        result = level + "\n" + result
    else:
        result = level

    domain = domain[index + 1:]
    index = domain.find(".")

if result:
    result = domain + "\n" + result
else:
    result = domain

print(result)
