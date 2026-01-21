n = int(input())
result = f"{bin(n)[2:]}, {oct(n)[2:]}, {hex(n)[2:]}" if n >= 0 else "Неверный ввод"
print(result)
