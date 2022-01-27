# №3 task
def main():
    try:
        input_money = get_money()
        usd_money = exchange_usd(input_money)
        eur_money = exchange_eur(input_money)
        chf_money = exchange_chf(input_money)
        gbp_money = exchange_gbp(input_money)
        cny_money = exchange_cny(input_money)
        print("Converted amount of USD-money = ", usd_money, "USD")
        print("Converted amount of EUR-money = ", eur_money, "EUR")
        print("Converted amount of CHF-money = ", chf_money, "CHF")
        print("Converted amount of GBP-money = ", gbp_money, "GBP")
        print("Converted amount of CNY-money = ", cny_money, "CNY")
    except ValueError as errorvalue:
        print(errorvalue)


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


def exchange_usd(money):
    int_money_usd = int(money) / 72.88
    return int_money_usd


def exchange_eur(money):
    int_money_eur = int(money) / 86.11
    return int_money_eur


def exchange_chf(money):
    int_money_chf = int(money) / 79.35
    return int_money_chf


def exchange_gbp(money):
    int_money_gbp = int(money) / 100.71
    return int_money_gbp


def exchange_cny(money):
    int_money_cny = int(money) / 11.32
    return int_money_cny


main()
