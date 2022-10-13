import requests
import json


def get_info_buy(pay_method, buy_coin, result_buy):
    headers = {
        'authority': 'p2p.binance.com',
        'x-trace-id': 'f6f0dbe1-ceaa-4ce6-8aa1-40233d2018fd',
        'c2ctype': 'c2c_merchant',
        'csrftoken': 'd41d8cd98f00b204e9800998ecf8427e',
        'x-ui-request-trace': 'f6f0dbe1-ceaa-4ce6-8aa1-40233d2018fd',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.145 Safari/537.36',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'lang': 'ru',
        'fvideo-id': '33890fcf83eeaeafbed97cc3a6fcba0bdcf01b29',
        'sec-ch-ua-mobile': '?0',
        'device-info': 'eyJzY3JlZW5fcmVzb2x1dGlvbiI6Ijg2NCwxNTM2IiwiYXZhaWxhYmxlX3NjcmVlbl9yZXNvbHV0aW9uIjoiODM0LDE1MzYiLCJzeXN0ZW1fdmVyc2lvbiI6IldpbmRvd3MgMTAiLCJicmFuZF9tb2RlbCI6InVua25vd24iLCJzeXN0ZW1fbGFuZyI6ImVuLVVTIiwidGltZXpvbmUiOiJHTVQrMyIsInRpbWV6b25lT2Zmc2V0IjotMTgwLCJ1c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Mi4wLjQ1MTUuMTQ1IFNhZmFyaS81MzcuMzYiLCJsaXN0X3BsdWdpbiI6IkNocm9taXVtIFBERiBQbHVnaW4sQ2hyb21pdW0gUERGIFZpZXdlcixOYXRpdmUgQ2xpZW50IiwiY2FudmFzX2NvZGUiOiIxOWVhYWM5ZSIsIndlYmdsX3ZlbmRvciI6Ikdvb2dsZSBJbmMuIChBTUQpIiwid2ViZ2xfcmVuZGVyZXIiOiJBTkdMRSAoQU1ELCBBTUQgUmFkZW9uKFRNKSBHcmFwaGljcyBEaXJlY3QzRDExIHZzXzVfMCBwc181XzAsIEQzRDExLTI3LjIwLjE0MDMyLjgpIiwiYXVkaW8iOiIxMjQuMDQzNDc1Mjc1MTYwNzQiLCJwbGF0Zm9ybSI6IldpbjMyIiwid2ViX3RpbWV6b25lIjoiRXVyb3BlL01vc2NvdyIsImRldmljZV9uYW1lIjoiQ2hyb21lIFY5Mi4wLjQ1MTUuMTQ1IChXaW5kb3dzKSIsImZpbmdlcnByaW50IjoiNzczNDJiNzAyMTlhMjZhYjhkYWNhNDJmMjg3NDZjZDAiLCJkZXZpY2VfaWQiOiIiLCJyZWxhdGVkX2RldmljZV9pZHMiOiIxNjU5MDk4MzI0ODMyQUZ1SWZBcEQwb1Z1MHRhQWxORiJ9',
        'bnc-uuid': '093a8289-3c5b-4914-9f2e-8541d1fe8b40',
        'clienttype': 'web',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="92"',
        'accept': '*/*',
        'origin': 'https://p2p.binance.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': f'https://p2p.binance.com/ru/trade/{pay_method}/{buy_coin}?fiat=RUB',
        'accept-language': 'en-US,en;q=0.9',
    }

    json_data = {
        'page': 1,
        'rows': 10,
        'payTypes': [
            f'{pay_method}'
        ],
        'countries': [],
        'publisherType': None,
        'asset': f'{buy_coin}',
        'fiat': 'RUB',
        'tradeType': 'BUY',
    }
    response = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=json_data).json()
    min_price = 9999999999
    result_pay_method = []
    for item in response['data']:
        res_pay_method = {
            'nickname': item.get('advertiser').get('nickname'),
            'price': item.get('adv').get('price'),
            'surplusAmount': item.get('adv').get('surplusAmount'),
            'link': f'https://p2p.binance.com/ru/{pay_method}/USDT?fiat=RUB'
        }
        result_pay_method.append(res_pay_method)
        if min_price > float(item.get('adv').get('price')):
            min_price = float(item.get('adv').get('price'))
            res_coin_method = {
                'mn': f'Minimal Price RUB -> {buy_coin } with {pay_method}: {min_price} руб',
                'link': f'https://p2p.binance.com/ru/{pay_method}/USDT?fiat=RUB'
            }
            result_buy.append(res_coin_method)
    data_base(result_pay_method, pay_method, buy_coin, result_buy)

def data_base(result_pay_method, pay_method, buy_coin, result_buy):
    with open(f'{pay_method}.json', 'w') as file:
        json.dump(result_pay_method, file, indent=4, ensure_ascii=False)
    with open(f'{buy_coin}.json', 'w') as files:
        json.dump(result_buy, files, indent=4, ensure_ascii=False)

def main(buy_coin):
    pay_method = ['TinkoffNew', 'RosBankNew', 'RaiffeisenBank', 'QIWI', 'YandexMoneyNew', 'CashInPerson']
    result_buy = []
    for pay in pay_method:
        get_info_buy(pay, buy_coin, result_buy)


