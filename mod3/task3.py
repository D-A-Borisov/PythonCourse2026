domain_name = input()
result = domain_name.split(".")[::-1]
print(*result, sep="\n")
