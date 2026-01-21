phone = input()
result = ''.join(symbol for symbol in phone if symbol in '+0123456789')
print(result)
