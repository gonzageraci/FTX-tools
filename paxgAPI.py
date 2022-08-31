from datetime import datetime
import FTXAPI as ftx
import apiKeys
"""
pair = "SNX-PERP"
client = ftx.FtxClient(api_key=apiKeys.PAXGapiKey, api_secret=apiKeys.PAXGapiSign, subaccount_name="PAXG")
trades = client.get_borrow_history()
rates = []
for i in trades:
    if i["coin"] == "USDT":
        print(i)
        rates.append(i["rate"])
sum = 0
for i in rates:
    sum += i
print(sum/len(rates))
anualRate = (sum/len(rates)) * 24 * 365
print(f"%{anualRate*100}")
"""

client = ftx.FtxClient(api_key=apiKeys.PAXGapiKey, api_secret=apiKeys.PAXGapiSign, subaccount_name="SNX")
trades = client.get_funding_rates(future="AAVE-PERP")
sum = 0
for i in trades:
    print(i["rate"])
    sum += i["rate"]

print(str(round((sum/len(trades))*24*365, 2)) + "%")