import pandas as pd
import requests

URL = "https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY"

header = {
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
}


session = requests.session()

data = session.get(url=URL, headers=header).json()["records"]["data"]

df = pd.DataFrame(data)

CE_data = []
PE_data = []
for i in range(len(df)):
    if df["expiryDate"][i] == "20-Jul-2023":
        CE_data.append(df["CE"][i])
        PE_data.append(df["PE"][i])

max_OI_CE = -10000000
change_at_max_OI_CE = 0
strike_price_CE = 0
open_CE = []
for i in CE_data:
    value = i["openInterest"]
    open_CE.append(value)
    if value > max_OI_CE:
        max_OI_CE = value
        change_at_max_OI_CE = i["changeinOpenInterest"]
        strike_price_CE = i["strikePrice"]

open_CE.sort()

max_OI_PE = -10000000
change_at_max_OI_PE = 0
strike_price_PE = 0
open_PE = []
for i in PE_data:
    value = i["openInterest"]
    open_PE.append(i["openInterest"])
    if value > max_OI_PE:
        max_OI_PE = value
        change_at_max_OI_PE = i["changeinOpenInterest"]
        strike_price_PE = i["strikePrice"]


open_PE.sort()
open_PE = open_PE[-20:]
open_CE = open_CE[-20:]


# Finding total CE and PE
total_OI_CE = 0
for i in open_CE:
    total_OI_CE += i

total_OI_PE = 0
for i in open_PE:
    total_OI_PE += i


all_value = [
    max_OI_CE,
    change_at_max_OI_CE,
    strike_price_CE,
    total_OI_PE / total_OI_CE,
    max_OI_PE,
    change_at_max_OI_PE,
    strike_price_PE,
]

print(
    f"Call: ({all_value[0]}, {all_value[1]}, {all_value[2]}) :: PCR-> {all_value[3]} ::  Put: ({all_value[4]}, {all_value[5]}, {all_value[6]})"
)
