import requests
from datetime import datetime


def request():
    try:
        r = requests.get(url='https://api.ethermine.org/'
                             'miner/F694Db83C3dFD050c5a8a82BeB09bC1Ec35b58cA/currentStats',
                         timeout=3)
    except requests.HTTPError as errh:
        return "HTTP error: ", errh
    except requests.Timeout as errt:
        return "Time out error: ", errt
    except requests.ConnectionError as errc:
        return "Connect error: ", errc
    except requests.RequestException as erre:
        return "Error. Something going wrong: ", erre

    return r


def check_status_ethermine():
    r = request().json()

    lastSeen_timestamp_moscow_time = int(r['data']['lastSeen']) + 60 * 60 * 3
    reportedHashrate = int(round((int(r['data']['reportedHashrate'])/1000000), 3))
    realHashrate = int(round((int(r['data']['averageHashrate'])/1000000), 3))
    activeWorkers = r['data']['activeWorkers']
    unpaid_balance = round(int(r['data']['unpaid'])/1000000000000000000, 3)
    coins_per_min = float(r['data']['coinsPerMin'])
    usd_per_min = float(r['data']['usdPerMin'])

    coins_per_24 = round(coins_per_min * 60 * 24, 5)
    coins_per_month = round(coins_per_min * 60 * 24 * 30, 5)
    usd_per_24 = round(usd_per_min * 60 * 24, 1)
    usd_per_month = round(usd_per_min * 60 * 24 * 30, 1)

    moscow_time = datetime.utcfromtimestamp(lastSeen_timestamp_moscow_time).strftime('%H:%M:%S %d-%m-%Y')

    return "*Ригов в работе: *" + str(activeWorkers) + "\n" + \
           "Последний пинг: " + str(moscow_time) + "\n" + \
           "Хэшрэйт на ригах: " + str(reportedHashrate) + " Mh/s" + "\n" + \
           "Учтенный хэшрейт: " + str(realHashrate) + " Mh/s" + "\n" + \
           "Текущий баланс на пуле: " + str(unpaid_balance) + " ETH" + "\n" + \
           "*Эфира в сутки: *" + str(coins_per_24) + " ETH" + "\n" + \
           "Эфира в месяц: " + str(coins_per_month) + " ETH" + "\n" + \
           "Долларов в сутки: " + str(usd_per_24) + " USD" + "\n" + \
           "*Долларов в месяц: *" + str(usd_per_month) + " USD" + "\n"
