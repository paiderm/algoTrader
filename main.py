import robin_stocks as rs
import os
import time


file = open("stockList.txt", 'r')

fileContent = file.read()
stockList = fileContent.split('\n')

file.close()

file = open("cryptoList.txt", 'r')

fileContent = file.read()
cryptoList = fileContent.split('\n')

file.close()

rs.login(username=os.environ.get("robinhood_username"), password=os.environ.get("robinhood_password"), expiresIn=86400, by_sms=True)



print ("LOGGED INTO THE MAINFRAME\n")

print("\nStocks:")
for stock in stockList:
    print(str(stock) + ": $" + str(rs.stocks.get_latest_price(str(stock))[0]))

print("\nCrypto:")
for crypto in cryptoList:
    print(str(crypto) + ": $" + str(rs.crypto.get_crypto_quote(str(crypto), 'mark_price')))


rs.logout()