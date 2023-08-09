import urllib.request
import json
import pprint

class TokenManager:
    @staticmethod
    def fetch_token():
        obj = { 'APIPassword': 'testtest' }
        json_data = json.dumps(obj).encode('utf8')

        url = 'http://localhost:18081/kabusapi/token'
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

        return None


if __name__ == '__main__':
    print(TokenManager.fetch_token())