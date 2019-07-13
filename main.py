import locale
language = locale.getdefaultlocale()[0]


def get_price_info():

    if language == "de_DE":
        stock_price = float(input("Aktienkurs eingeben "))
        certificate_price = float(input("Zertifikatskurs eingeben "))
        conversion_ratio = float(input("Bezugsverhältnis eingeben "))
    else:
        stock_price = float(input("enter stockprice "))
        certificate_price = float(input("enter certificate price "))
        conversion_ratio = float(input("enter conversion ratio "))

    return stock_price, certificate_price, conversion_ratio


def get_stop_loss_start_buy_price():
    if language == "de_DE":
        stop_loss_or_start_buy = float(input("Stop-Loss/Start-Buy Kurs eingeben "))
    else:
        stop_loss_or_start_buy = float(input("enter Stop-Loss/Start-Buy price "))

    return stop_loss_or_start_buy


def main():

    (stock_price, certificate_price, conversion_ratio) = get_price_info()

    leverage = stock_price / ((1 / conversion_ratio) * certificate_price)

    print()
    if language == "de_DE":
        print(("\033[1m" + "Der Hebel des Zertifikats beträgt: {}" + "\033[0m").format(leverage))
    else:
        print(("\033[1m" + "The leverage of the certificate is: {}" + "\033[0m").format(leverage))
    print()

    stop_loss_or_start_buy = get_stop_loss_start_buy_price()

    # distance between stock price and set stop-loss or start-buy in percent
    distance_in_percent = 1-(stop_loss_or_start_buy/stock_price)

    stop_loss_or_start_buy_of_the_certificate = (1-(distance_in_percent * leverage)) * certificate_price

    if stop_loss_or_start_buy_of_the_certificate < 0:
        stop_loss_or_start_buy_of_the_certificate = 0

    if language == "de_DE":
        print(("\033[1m" + "Der Stop-Loss/Start-Buy Kurs des Zertifikats liegt bei: {}" + "\033[0m")
              .format(round(stop_loss_or_start_buy_of_the_certificate, 2)))
    else:
        print(("\033[1m" + "The Stop-Loss/Start-Buy price of the certificate is: {}" + "\033[0m")
              .format(round(stop_loss_or_start_buy_of_the_certificate, 2)))


if __name__ == '__main__':
    main()