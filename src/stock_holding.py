import urllib.request
import json
import pprint
import os
from src.order_constants import OrderConstants
from dotenv import load_dotenv

load_dotenv()


class StockHolding:
    def __init__(self, config, token):
        self.config = config
        self.token = token

    def get_positions(self):
        url = f"{self.config['URL']}positions"
        params = {
            'product': OrderConstants.CASH,
            'symbol': os.getenv('NT'),
            'side': OrderConstants.BUY,
            'addinfo': 'true'
        }
        req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)), method='GET')

        req.add_header('Content-Type', 'application/json')
        req.add_header('X-API-KEY', self.token)

        try:
            with urllib.request.urlopen(req) as res:
                content = json.loads(res.read())
                return content[0]['LeavesQty'] if content else 0

        except urllib.error.HTTPError as e:
            print(e)
            content = json.loads(e.read())
            pprint.pprint(content)
        except Exception as e:
            print(e)
