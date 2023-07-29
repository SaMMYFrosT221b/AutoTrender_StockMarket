import pandas as pd
import requests
from openpyxl import load_workbook

URL = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"

header = {
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
}


session = requests.session()

data = session.get(url=URL, headers=header).json()["records"]["data"]

df = pd.DataFrame(data)

count = 0
list = [
    "openInterest",
    "changeinOpenInterest",
    "totalTradedVolume",
    "lastPrice",
    "change",
    "strikePrice",
]
CE_data = []
PE_data = []
for i in range(len(df)):
    if df["expiryDate"][i] == "03-Aug-2023":
        CE_data.append(df["CE"][i])
        PE_data.append(df["PE"][i])


openInterestCE = []
changeinOpenInterestCE = []
totalTradedVolumeCE = []
lastPriceCE = []
changeCE = []
strikePrice = []
openInterestPE = []
changeinOpenInterestPE = []
totalTradedVolumePE = []
lastPricePE = []
changePE = []


# print(CE_data)

for i in range(len(CE_data)):
    openInterestCE.append(CE_data[i]["openInterest"])
    changeinOpenInterestCE.append(CE_data[i]["changeinOpenInterest"])
    totalTradedVolumeCE.append(CE_data[i]["totalTradedVolume"])
    lastPriceCE.append(CE_data[i]["lastPrice"])
    changeCE.append(CE_data[i]["change"])

    strikePrice.append(CE_data[i]["strikePrice"])

    openInterestPE.append(PE_data[i]["openInterest"])
    changeinOpenInterestPE.append(PE_data[i]["changeinOpenInterest"])
    totalTradedVolumePE.append(PE_data[i]["totalTradedVolume"])
    lastPricePE.append(PE_data[i]["lastPrice"])
    changePE.append(PE_data[i]["change"])


headings = pd.DataFrame(
    {
        "OI": openInterestCE,
        "CHNG": changeinOpenInterestCE,
        "VOLUME": totalTradedVolumeCE,
        "LTP": lastPriceCE,
        "Change": changeCE,
        "Strike": strikePrice,
        "Chnage ": changePE,
        "LTP ": lastPricePE,
        "Volume ": totalTradedVolumePE,
        "CHNG ": changeinOpenInterestPE,
        "OI ": openInterestPE,
    }
)


headings.to_excel("./Option.xlsx", index=False)
