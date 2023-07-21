import time

import pandas as pd
import requests


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

    max_OI_CE = -10000000
    change_at_max_OI_CE = 0
    strike_price_CE = 0
    open_CE = []

    # Calculating open Interest of CE
    for i in CE_data:
        value = i["openInterest"]
        open_CE.append(value)
        if value > max_OI_CE:
            max_OI_CE = value
            change_at_max_OI_CE = i["changeinOpenInterest"]
            strike_price_CE = i["strikePrice"]
    open_CE.sort()

    # Put European
    max_OI_PE = -10000000
    change_at_max_OI_PE = 0
    strike_price_PE = 0
    open_PE = []

    # Calculating open Interest of PE
    for i in PE_data:
        value = i["openInterest"]
        open_PE.append(i["openInterest"])
        if value > max_OI_PE:
            max_OI_PE = value
            change_at_max_OI_PE = i["changeinOpenInterest"]
            strike_price_PE = i["strikePrice"]

    open_PE.sort()

    # Taking only top 20 Values of OI
    open_PE = open_PE[-20:]
    open_CE = open_CE[-20:]

    # Finding total CE and PE
    total_OI_CE = 0
    for i in open_CE:
        total_OI_CE += i

    total_OI_PE = 0
    for i in open_PE:
        total_OI_PE += i

    # Putting all the values in a list
    all_value = [
        max_OI_CE,
        change_at_max_OI_CE,
        strike_price_CE,
        total_OI_PE / total_OI_CE,
        max_OI_PE,
        change_at_max_OI_PE,
        strike_price_PE,
    ]
    return all_value

    print(
        f"Call: ({all_value[0]}, {all_value[1]}, {all_value[2]}) :: PCR-> {all_value[3]} ::  Put: ({all_value[4]}, {all_value[5]}, {all_value[6]})"
    )


def BANKNIFTY():
    # URL for fetching data
    URL = "https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY"

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

    max_OI_CE = -10000000
    change_at_max_OI_CE = 0
    strike_price_CE = 0
    open_CE = []

    # Calculating open Interest of CE
    for i in CE_data:
        value = i["openInterest"]
        open_CE.append(value)
        if value > max_OI_CE:
            max_OI_CE = value
            change_at_max_OI_CE = i["changeinOpenInterest"]
            strike_price_CE = i["strikePrice"]
    open_CE.sort()

    # Put European
    max_OI_PE = -10000000
    change_at_max_OI_PE = 0
    strike_price_PE = 0
    open_PE = []

    # Calculating open Interest of PE
    for i in PE_data:
        value = i["openInterest"]
        open_PE.append(i["openInterest"])
        if value > max_OI_PE:
            max_OI_PE = value
            change_at_max_OI_PE = i["changeinOpenInterest"]
            strike_price_PE = i["strikePrice"]

    open_PE.sort()

    # Taking only top 20 Values of OI
    open_PE = open_PE[-20:]
    open_CE = open_CE[-20:]

    # Finding total CE and PE
    total_OI_CE = 0
    for i in open_CE:
        total_OI_CE += i

    total_OI_PE = 0
    for i in open_PE:
        total_OI_PE += i

    # Putting all the values in a list
    all_value = [
        max_OI_CE,
        change_at_max_OI_CE,
        strike_price_CE,
        total_OI_PE / total_OI_CE,
        max_OI_PE,
        change_at_max_OI_PE,
        strike_price_PE,
    ]
    return all_value

    print(
        f"Call: ({all_value[0]}, {all_value[1]}, {all_value[2]}) :: PCR-> {all_value[3]} ::  Put: ({all_value[4]}, {all_value[5]}, {all_value[6]})"
    )


if __name__ == "__main__":
    while True:
        nifty_value = NIFTY()
        banknifty_values = BANKNIFTY()

        # Printing
        print(
            f"Call: ({nifty_value[0]}, {nifty_value[1]}, {nifty_value[2]}) :: PCR-> {nifty_value[3]} ::  Put: ({nifty_value[4]}, {nifty_value[5]}, {nifty_value[6]})",
            end=" *** ",
        )
        print(
            f"Call: ({banknifty_values[0]}, {banknifty_values[1]}, {banknifty_values[2]}) :: PCR-> {banknifty_values[3]} ::  Put: ({banknifty_values[4]}, {banknifty_values[5]}, {banknifty_values[6]})"
        )
        time.sleep(60)
