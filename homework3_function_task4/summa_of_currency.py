def get_summa():
    summa = int(input("Enter value of summa "))
    if summa < 0:
        print("Введите положительное число.")
        while True:
            summa = input("Enter value of summa ").strip()
            if summa.isdigit():
                summa = int(summa)
                break
            else:
                if not summa:
                    print("Вы ввели пустое поле. Введите  число.")
                else:
                    print("Вы ввели не число. Введите число.")
    return summa