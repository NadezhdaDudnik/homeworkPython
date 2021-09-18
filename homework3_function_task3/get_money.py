def get_money():
    input_data = int(input("Enter value of currency RUB "))
    if input_data < 0:
        print("Введите положительное число.")
        while True:
            input_data = input("Enter value of currency RUB ").strip()
            if input_data.isdigit():
                input_data = int(input_data)
                break
            else:
                if not input_data:
                    print("Вы ввели пустое поле. Введите  число.")
                else:
                    print("Вы ввели не число. Введите число.")
    return input_data
