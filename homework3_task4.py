# task4
def main():
    #input_money = get_money()
    print_currency_list()
    input_currency_value()
    input_summa()

def print_currency_list():
    currency_list = ['USD','EUR','CHF','GBP','CNY']
    print("Выберите валюту из ", currency_list)

def input_currency_value():
    input_currency = input("Enter value of currency from currency list ['USD','EUR','CHF','GBP','CNY'] : ")
    return input_currency

def input_summa():
    summa_value = int(input("Введите сумму "))
    return summa_value



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

main()