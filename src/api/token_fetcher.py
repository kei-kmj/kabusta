import urllib.request
import json


class TokenFetcher:
    def __init__(self, config):
        self.config = config

    def fetch_token(self):
        obj = {'APIPassword': self.config['APIPassword']}
        json_data = json.dumps(obj).encode('utf8')

        url = f"{self.config['URL']}token"
        req = urllib.request.Request(url, json_data, method='POST')
        req.add_header('Content-Type', 'application/json')

        try:
            with urllib.request.urlopen(req) as res:
                content = json.loads(res.read())
                return content['Token']
        except urllib.error.HTTPError as e:
            content = json.loads(e.read())
            print(content)
        except Exception as e:
            print(e)
