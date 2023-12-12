# Користувач вводить шестизначне число. Необхідно поміняти в цьому числі першу та
# шосту цифри, а також другу та п'яту цифри.
# Наприклад, 723895 має перетворитися на 593827
# Якщо користувач ввів не шестизначне число, потрібно вивести повідомлення про помилку.

number = int(input("Enter six-digit number: "))

# Check for six digit number
if number < 100000 or number >= 1000000:
    print("You enter not six-digit number")
    exit()

# We get the number from first to sixth
digit_1 = number // 100000
digit_2 = (number // 10000) % 10
digit_3 = (number // 1000) % 10
digit_4 = (number // 100) % 10
digit_5 = (number // 10) % 10
digit_6 = number % 10

# Swap places 1-6 and 2-5
print(digit_6 * 100000 + digit_5 * 10000 + digit_3 * 1000 + digit_4 * 100 + digit_2 * 10 + digit_1 * 1 )