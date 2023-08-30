import urllib.request
import json
import pprint
from dotenv import load_dotenv

load_dotenv()


class CashHolding:

    def __init__(self, config, token):
        self.config = config
        self.token = token

    def get_cash(self):

        url = f"{self.config['URL']}wallet/cash"
        req = urllib.request.Request(url, method='GET')
        req.add_header('Content-Type', 'application/json')
        req.add_header('X-API-KEY', self.token)

        try:
            with urllib.request.urlopen(req) as res:
                content = json.loads(res.read())
                return content['StockAccountWallet'] if self.config['env'] == 'prod' else 10000
        except urllib.error.HTTPError as e:
            print(e)
            content = json.loads(e.read())
            pprint.pprint(content)
        except Exception as e:
            print(e)
