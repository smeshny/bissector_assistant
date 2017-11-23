import requests

from config import etherscan_token


def ether_scan():
    api_key = etherscan_token
    wallet = "0xF694Db83C3dFD050c5a8a82BeB09bC1Ec35b58cA"

    try:
        request_balance = requests.get('https://api.etherscan.io/api?module=account&action=balance&address=' +
                                      wallet +'&tag=latest&apikey=' + api_key).json()
        request_usd_price = requests.get('https://api.etherscan.io/api?module=stats&action=ethprice&apikey='
                                         + api_key).json()
        request_usd_rub_cb_price = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()
    except requests.HTTPError as errh:
        return "HTTP error: ", errh
    except requests.Timeout as errt:
        return "Time out error: ", errt
    except requests.ConnectionError as errc:
        return "Connect error: ", errc
    except requests.RequestException as erre:
        return "Error. Something going wrong: ", erre


    balance_eth = round(int(request_balance["result"]) / 1000000000000000000, 3)
    eth_usd = float(request_usd_price['result']['ethusd'])
    balance_usd = round(float(balance_eth) * eth_usd, 2)
    cb_usd_rub = float(request_usd_rub_cb_price["Valute"]["USD"]["Value"])
    cb_usd_rub_round = round(cb_usd_rub, 2)
    balance_RUR = round(cb_usd_rub * balance_usd, 2)

    return "\n" + "*ETH на кошельке: " + str(balance_eth) + "ETH" + "\n" \
           "В долларах: " + str(balance_usd) + "USD" + "\n" \
           "В рублях: " + str(balance_RUR) + "RUR" + "\n" \
           "Курс ETH: " + str(eth_usd) + "USD" + "\n" \
           "Курс USD ЦБ: " + str(cb_usd_rub_round) + "RUR" + "*"
