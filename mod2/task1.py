input_string = input()  # 123, 12

index = input_string.find(", ")
first_number = int(input_string[:index])
second_number = int(input_string[index+2:])
remains = first_number % second_number

print(remains)
