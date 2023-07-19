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

temp = []
for i in range(len(df)):
    if df["expiryDate"][i] == "20-Jul-2023":
        temp.append(df["CE"][i])


sum = 0
for i in temp:
    sum += i["openInterest"]
    # print(i["openInterest"])

print(sum)
