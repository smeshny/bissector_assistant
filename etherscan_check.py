import time
import datetime

import requests

from config import etherscan_token


# Get ETHER LastPrice Price
#
#     https://api.etherscan.io/api?module=stats&action=ethprice&apikey=YourApiKeyToken
#

#  Token Info
#
#
# Get ERC20-Token TotalSupply by ContractAddress
#
#     https://api.etherscan.io/api?module=stats&action=tokensupply&contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055&apikey=YourApiKeyToken
#


def ether_scan():
    api_key = etherscan_token
    wallet = "0xF694Db83C3dFD050c5a8a82BeB09bC1Ec35b58cA"

    try:
        request_balance = requests.get('https://api.etherscan.io/api?module=account&action=balance&address=' +
                                      wallet +'&tag=latest&apikey=' + api_key).json()
        request_usd_price = requests.get('https://api.etherscan.io/api?module=stats&action=ethprice&apikey='
                                         + api_key).json()
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

    return "\n" + "*Эфира на кошельке: " + str(balance_eth) + "ETH" + "\n" \
           "В долларах: " + str(balance_usd) + "USD" + "\n" \
           "Курс эфира к доллару: " + str(eth_usd) + "*"

