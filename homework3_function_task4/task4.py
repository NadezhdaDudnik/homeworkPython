# task4
from print_currency import print_currency_list
from input_currency import input_currency_value
from summa_of_currency import get_summa
from excange_currency import *


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
        # When you are finished interacting with the interpreter, you can exit a REPL session in several ways: macOS,
        # type Command + D
        except EOFError as error:
            print(error)
            break

main()