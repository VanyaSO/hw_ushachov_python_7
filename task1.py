# Користувач вводить із клавіатури ціле шестизначне число. 
# Написати програму, яка визначає, чи є введене число щасливим 
# (щасливим вважається шестизначне число, в якого сума перших 3 цифр дорівнює сумі других трьох цифр).
# Наприклад, 123321 — щасливе число, тому що 1+2+3 = 3+2+1.
# 3 іншого боку 378423 — нещасливе число, оскільки 3+7+8 != 4+2+3.
# Якщо користувач ввів не шестизначне число, потрібно вивести повідомлення про
# помилку.


number = int(input("Enter six-digit number: "))

# Сheck for six digit number
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

# Сheck for lucky number
if digit_1 + digit_2 + digit_3 == digit_4 + digit_5 + digit_6 :
    print("Your number is lucky")
else: 
    print("Your number is not lucky")