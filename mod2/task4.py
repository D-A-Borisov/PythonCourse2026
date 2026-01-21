number = int(input())

if number < 0:
    print("Неверный ввод")
    exit(1)

r2 = ""
temp = number
while temp > 0:
    r2 += str(temp % 2)
    temp = temp // 2

r8 = ""
temp = number
while temp > 0:
    r8 += str(temp % 8)
    temp = temp // 8

r16 = ""
temp = number
while temp > 0:
    digit = temp % 16
    if digit == 10:
        r16 += "A"
    elif digit == 11:
        r16 += "B"
    elif digit == 12:
        r16 += "C"
    elif digit == 13:
        r16 += "D"
    elif digit == 14:
        r16 += "E"
    elif digit == 15:
        r16 += "F"
    else:
        r16 += str(digit)
    temp = temp // 16

print(f"{r2[::-1]}, {r8[::-1]}, {r16[::-1]}")
