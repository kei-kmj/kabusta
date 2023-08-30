import os
import urllib.request
import json
import pprint
from src.order_constants import OrderConstants
from dotenv import load_dotenv

load_dotenv()


class BuyOrderSender:

    def __init__(self, config, token):
        self.config = config
        self.token = token

    @property
    def order_details(self):
        return {
            'Password': os.getenv('ORDER_PASSWORD'),
            'Symbol': os.getenv('HJ'),
            'Exchange': 1,
            'SecurityType': OrderConstants.STOCK,
            'Side': OrderConstants.BUY,
            'CashMargin': OrderConstants.CASH,
            'DelivType': OrderConstants.DEPOSIT,
            'FundType': OrderConstants.PROTECTION,
            'AccountType': OrderConstants.SPECIFIC,
            'Qty': 100,
            'FrontOrderType': 20,
            'Price': 550,
            'ExpireDay': 20230908
        }

    def send_order(self):

        json_data = json.dumps(self.order_details).encode('utf-8')

        url = f"{self.config['URL']}sendorder"
        req = urllib.request.Request(url, json_data, method='POST')
        self.set_request_headers(req)
        try:
            with urllib.request.urlopen(req) as res:
                print(f"{self.order_details['Symbol']}の買い注文を出しました")
        except urllib.error.HTTPError as e:
            print(f"HTTPError: {e}")
            content = json.loads(e.read())
            pprint.pprint(content)
        except Exception as e:
            print(f"ExceptionError: {e}")

    def set_request_headers(self, req):
        req.add_header('Content-Type', 'application/json')
        req.add_header('X-API-KEY', self.token)
