import requests
import json

from sympy import EX
symbols = ["BTC", "ETH", "AVAX", "BNB", "FTM", "SOL", "MATIC", "ADA", "DOT"]

def getFR(symbol):
    url = f"https://fapi.coinglass.com/api/fundingRate/v2/history/chart?symbol={symbol}&type=U&interval=h8"
    json = requests.get(url).json()
    fr = {}
    for i in json["data"]["dataMap"]:
        fr[i] = json["data"]["dataMap"][i]
    return fr

def getAPRs(symbol):
    fundrates = getFR(symbol)
    avgfundrates = {}
    
    

    for i in fundrates:
        if i == "":
            pass

        sum = 0
        for j in fundrates[i][:(3*30)]:
            try:
                sum += j
            except:
                continue
        #print(f"Avg {i} = {sum/len(fundrates[i])}")
        avgfundrates[i] = sum/len(fundrates[i])

    maxName = ""
    max = {maxName:-1000}
    minName = ""
    min = {minName:1000}
    for i in avgfundrates:
        if avgfundrates[i] < min[minName]:
            minName = i
            min[i] = avgfundrates[i]
        if avgfundrates[i] > max[maxName]:
            maxName = i
            max[i] = avgfundrates[i]
        else:
            continue
    print("-----------------------------")
    print(f"Arbitraje for {symbol}")
    print(f"Long {minName}: {round(min[minName]*3*365,2)}% | Short {maxName}: {round(max[maxName]*3*365,2)}%")
    print(f"AVG APR: {round((max[maxName]-min[minName])*3*365,2)}%")


for symbol in symbols:
    getAPRs(symbol)

