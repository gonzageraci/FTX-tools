from datetime import datetime
from os import times
import FTXAPI as ftx
import apiKeys

pair = "SNX-PERP"
client = ftx.FtxClient(api_key=apiKeys.SNXapiKey, api_secret=apiKeys.SNXapiSign, subaccount_name="SNX")
trades = client.get_order_history(market=pair)
#pays = client.get_funding_payments(start_time=1658793600.0, end_time=1658962800.0)

times = []
for i in trades:
    time = i["createdAt"]
    dtime = datetime(int(time[0:4]), int(time[5:7]), int(time[8:10]), int(time[11:13])).timestamp()
    """for j in i:
        print(f"{j} {i[j]}")
    print(dtime)"""
    times.append(dtime)
    """#sum += float(i["filledSize"]* i["avgFillPrice"])
    print("amount price: " + str(i["filledSize"]* i["avgFillPrice"]))
    print("---------------")"""

#print(times)




for time in range(-1, len(times)*-1, -1):
    sum = 0
    values = ""
    #try:
    pays = client.get_funding_payments(start_time=times[time], end_time=times[time-1])
    values = f"{times[time]} - {times[time-1]}"
        #print(f"{times[time]}, {times[time-1]}")
    """except:
        pays = client.get_funding_payments(start_time=times[time])
        values = f"{times[time]}"
        #print(f"{times[time]}")"""
    for i in pays:
        if i["future"] == "SNX-PERP":
            sum += i["payment"]
        else:
            continue
    print(f"{time}->{str(round(sum,2))}$ -> {values}")
"""
sum2 = 0
for i in client.get_funding_payments(start_time=1659582000.0, end_time=1658962800.0):
        if i["future"] == "SNX-PERP":
            sum2 += i["payment"]
        else:
            continue
print(sum2)"""
