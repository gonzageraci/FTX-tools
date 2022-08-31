from datetime import datetime
import FTXAPI as ftx
import apiKeys

pair = "SNX-PERP"
client = ftx.FtxClient(api_key=apiKeys.apiKey, api_secret=apiKeys.apiSign, subaccount_name="SNX")
trades = client.get_funding_rates(future=pair)

for i in trades:
    print(i)