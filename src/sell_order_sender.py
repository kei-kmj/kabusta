import os
import urllib.request
import json
import pprint
from src.order_constants import OrderConstants
from dotenv import load_dotenv

load_dotenv()


class SellOrderSender:

    def __init__(self, config, token):
        self.config = config
        self.token = token

    @property
    def order_details(self):
        return {
            'Password': self.config['APIPassword'],
            'Symbol': os.getenv('NT'),
            'Exchange': 1,
            'SecurityType': 1,
            'Side': OrderConstants.SELL,
            'CashMargin': OrderConstants.CASH,
            'DelivType': OrderConstants.PHYSICAL_SELL,
            'FundType': OrderConstants.PHYSICAL,
            'AccountType': OrderConstants.SPECIFIC,
            'Qty': 100,
            'FrontOrderType': 20,
            'Price': 1380,
            'ExpireDay': OrderConstants.TODAY
        }

    def send_order(self):

        json_data = json.dumps(self.order_details).encode('utf-8')

        url = f"{self.config['URL']}sendorder"
        req = urllib.request.Request(url, json_data, method='POST')
        self.set_request_headers(req)
        try:
            with urllib.request.urlopen(req) as res:
                print(res.status, res.reason)
                for header in res.getheaders():
                    print(header)
                content = json.loads(res.read())
                pprint.pprint(content)
                print('売り注文を出しました')
        except urllib.error.HTTPError as e:
            print(f"HTTPError: {e}")
            content = json.loads(e.read())
            pprint.pprint(content)
        except Exception as e:
            print(f"ExceptionError: {e}")

    def set_request_headers(self, req):
        req.add_header('Content-Type', 'application/json')
        req.add_header('X-API-KEY', self.token)
