
# №1 and №2 tasks
def main():
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

def get_money():
    input_data = int(input("Enter value of currency RUB = "))
    return input_data

def exchange_usd(money):
    int_money_usd = round(int(money) / 72.88)
    return int_money_usd

def exchange_eur(money):
    int_money_eur = round(int(money) / 86.11)
    return int_money_eur

def exchange_chf(money):
    int_money_chf = round(int(money) / 79.35)
    return int_money_chf

def exchange_gbp(money):
    int_money_gbp = round(int(money) / 100.71)
    return int_money_gbp

def exchange_cny(money):
    int_money_cny = round(int(money) / 11.32)
    return int_money_cny

main()