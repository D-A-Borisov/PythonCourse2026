def check_number():
    numbers = list(map(int, input().split()))
    unique_count = len(set(numbers))
    total_count = len(numbers)

    if unique_count == 1:
        print("Все числа равны")
    elif unique_count == total_count:
        print("Все числа разные")
    else:
        print("Есть равные и неравные числа")


if __name__ == "__main__":
    check_number()
