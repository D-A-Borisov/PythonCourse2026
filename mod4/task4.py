def can_form_palindrome():
    word = input().strip()
    char_count = {}

    for char in word:
        char_count[char] = char_count.get(char, 0) + 1

    odd_chars = [char for char, count in char_count.items() if count % 2 != 0]

    if len(odd_chars) > 1:
        print("Нельзя составить палиндром")
        return

    palindrome = []
    middle_char = ""

    for char, count in char_count.items():
        if count % 2 != 0:
            middle_char = char
            count -= 1
        palindrome.extend([char] * (count // 2))

    first_half = ''.join(palindrome)
    result = first_half + middle_char + first_half[::-1]
    print(result)


if __name__ == "__main__":
    can_form_palindrome()
