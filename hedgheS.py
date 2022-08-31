from unicodedata import name
import FTXAPI as ftx
import apiKeys
from datetime import datetime
def getFees(pair):
    client = ftx.FtxClient(api_key=apiKeys.apiKey, api_secret=apiKeys.apiSign, subaccount_name="SNX")
    trades = client.get_order_history(market=pair)
    times = []
    _sizes = [0]
    for i in trades:
        time = i["createdAt"]
        dtime = datetime(int(time[0:4]), int(time[5:7]), int(time[8:10]), int(time[11:13])).timestamp()
        if i["side"] == "sell":
            try:
                price = float(i["price"])
            except:
                price = float(i["avgFillPrice"])
            size = i["filledSize"] * price
        else:
            size = -1*(i["filledSize"]) * float(i["price"])
        _sizes.insert(0,(size))
        times.insert(0,dtime)

        for j in i:
            print(f"{j} {i[j]}")
        print(dtime)
        print("---------------")
    _sizes.pop()

    sizes = _sizes[::-1]
    sizes = [0]
    for i in range(len(_sizes)):
        sizes.append(_sizes[i]+sizes[i])
    sizes.pop(0)

    fee = 0 

    for i in range(len(times)):
        try:
            _funds = client.get_funding_rates(future=pair, start_time=times[i], end_time=times[i+1])
        except:
            _funds = client.get_funding_rates(future=pair, start_time=times[i])
        
        funds = []
        for fund in _funds:
            funds.append(fund["rate"])

        for j in range(len(funds)):
            print(f"fee: {(funds[j] * sizes[i])} | size: {sizes[i]}")
            fee += (funds[j] * sizes[i])

    return(fee)

print(getFees("SNX-PERP"))