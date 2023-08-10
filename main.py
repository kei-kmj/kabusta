from src.token_manager import TokenManager
from src.send_order_buy import SendOrderBuy
from config import Config
import argparse

parser = argparse.ArgumentParser(description='Fetch API token')
parser.add_argument('--env', choices=['test', 'prod'], default='test', help='Specify environment (test or prod)')
args = parser.parse_args()

if __name__ == '__main__':
    config = Config.ENV_TEST if args.env == 'test' else Config.ENV_PROD
    token_manager = TokenManager(config)
    token = token_manager.fetch_token()

    send_order_buy = SendOrderBuy(config, token)
    send_order_buy.send_order()

