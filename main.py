import pandas as pd
import requests
import time


def NIFTY():
    # URL for fetching data
    URL = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"

    # Header file.
    header = {
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    }

    session = requests.session()

    data = session.get(url=URL, headers=header).json()["records"]["data"]
    records = session.get(url=URL, headers=header).json()["records"]

    # For calculating Expiry Date
    # print("Date: ", records["expiryDates"][0])

    df = pd.DataFrame(data)

    # Call European
    CE_data = []
    PE_data = []
    for i in range(len(df)):
        if df["expiryDate"][i] == records["expiryDates"][0]:
            CE_data.append(df["CE"][i])
            PE_data.append(df["PE"][i])

    maxChnageInOpenCE = -1000000000
    openInterestCE = 0

    for i in CE_data:
        value = i["changeinOpenInterest"]
        if value > maxChnageInOpenCE:
            maxChnageInOpenCE = value
            openInterestCE = i["openInterest"]
            strikePrice = i["strikePrice"]
    # print(maxChnageInOpenCE)
    # print(openInterestCE)

    maxChnageInOpenPE = -1000000000
    openInterestPE = 0

    for i in PE_data:
        value = i["changeinOpenInterest"]
        if value > maxChnageInOpenPE:
            maxChnageInOpenPE = value
            openInterestPE = i["openInterest"]
            strikePrice = i["strikePrice"]
    # print(maxChnageInOpenPE)
    # print(openInterestPE)

    addCE = maxChnageInOpenCE + openInterestCE
    addPE = maxChnageInOpenPE + openInterestPE

    print((addPE - addCE) / 100000)

    # print(
    #     f"Call: ({all_value[0]}, {all_value[1]}, {all_value[2]}) :: PCR-> {all_value[3]} ::  Put: ({all_value[4]}, {all_value[5]}, {all_value[6]})"
    # )


if __name__ == "__main__":
    while(True):
        NIFTY()
        time.sleep(60)
