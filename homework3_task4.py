# task4
def main():
    while True:
        try:
            print_currency_list()
            input_currency = input_currency_value()
            input_summa = get_summa()
            if input_currency == 'USD':
                usd_money = exchange_usd(input_summa)
                print("You enter summa ", input_summa, " and ", "currency ", input_currency, ", Converted amount of "
                                                                                             "USD-money = ",
                      usd_money, "USD")
            elif input_currency == 'EUR':
                eur_money = exchange_eur(input_summa)
                print("You enter summa ", input_summa, " and ", "currency ", input_currency, ", Converted amount of "
                                                                                             "EUR-money = ",
                      eur_money, "EUR")
            elif input_currency == 'CHF':
                chf_money = exchange_chf(input_summa)
                print("You enter summa ", input_summa, " and ", "currency ", input_currency,
                      ", Converted amount of EUR-money = ", chf_money, "CHF")
            elif input_currency == 'GBP':
                gbp_money = exchange_gbp(input_summa)
                print("You enter summa ", input_summa, " and ", "currency ", input_currency,
                      ", Converted amount of EUR-money = ", gbp_money, "GBP")
            elif input_currency == 'CNY':
                cny_money = exchange_cny(input_summa)
                print("You enter summa ", input_summa, " and ", "currency ", input_currency,
                      ", Converted amount of EUR-money = ", cny_money, "CNY")
            else:
                print("conversion is not possible \n")
        # When you are finished interacting with the interpreter, you can exit a REPL session in several ways: macOS,
        # type Command + D
        except ValueError as errorvalue:
            print(errorvalue)
        except EOFError as error:
            print(error)
            break


# Скрипт сначала выводит "Выберите валюту из ['USD','EUR','CHF','GBP','CNY']"
def print_currency_list():
    currency_list = ['USD', 'EUR', 'CHF', 'GBP', 'CNY']
    for currency in currency_list:
        print("Select currency ", currency)


# Пользователь вводит один из 5 вариантов ['USD','EUR','CHF','GBP','CNY']
def input_currency_value():
    input_currency = input("Enter value of currency from currency list ['USD','EUR','CHF','GBP','CNY'] : ")
    return input_currency


# Скрипт выводит "Введите сумму", и Пользователь вводит сумму int
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


# обмен валюты
def exchange_usd(money):
    int_money_usd = round(int(money) / 72.88)
    return int_money_usd


def exchange_eur(money):
    int_money_eur = round(int(money) / 86.11)
    return int_money_eur


def exchange_chf(money):
    int_money_chf = round(int(money) / 100.71)
    return int_money_chf


def exchange_gbp(money):
    int_money_gbp = round(int(money) / 11.32)
    return int_money_gbp


def exchange_cny(money):
    int_money_cny = round(int(money) / 72.88)
    return int_money_cny


main()
