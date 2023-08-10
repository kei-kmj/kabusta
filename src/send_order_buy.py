import os
import urllib.request
import json
import pprint
from dotenv import load_dotenv

load_dotenv()


class SendOrderBuy:

    def __init__(self, config, token):
        self.config = config
        self.token = token

    def send_order(self):

        obj = {'Password': os.getenv('ORDER_PASSWORD'),
               'Symbol': os.getenv('NT'),
               'Exchange': 1,
               'SecurityType': 1,
               'Side': '2',
               'CashMargin': 1,
               'DelivType': 2,
               'FundType': '02',
               'AccountType': 4,
               'Qty': 100,
               'FrontOrderType': 20,
               'Price': 1380,
               'ExpireDay': 0
               }

        json_data = json.dumps(obj).encode('utf-8')

        url = url = f"{self.config['URL']}sendorder"
        req = urllib.request.Request(url, json_data, method='POST')
        req.add_header('Content-Type', 'application/json')
        req.add_header('X-API-KEY', self.token)
        try:
            with urllib.request.urlopen(req) as res:
                print(res.status, res.reason)
                for header in res.getheaders():
                    print(header)
                content = json.loads(res.read())
                pprint.pprint(content)
        except urllib.error.HTTPError as e:
            print(e)
            content = json.loads(e.read())
            pprint.pprint(content)
        except Exception as e:
            print(e)
