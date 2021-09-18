from get_money import get_money
from exchange_currency import exchange_usd,exchange_gbp,exchange_eur,exchange_chf,exchange_cny


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
    except ValueError as error:
        print(error)


main()
