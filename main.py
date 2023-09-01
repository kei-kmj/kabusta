from src.api.buy_executor import BuyExecutor
from src.api.sell_executor import SellExecutor
from src.api.stock_holding import StockHolding
from src.api.cash_holding import CashHolding
from src.util.keyring_util import KeyringUtil
from config import Config
import argparse


def return_environment_from_args():
    parser = argparse.ArgumentParser(description='Fetch API token')
    parser.add_argument('--env', choices=['test', 'prod'], default='test', help='Specify environment (test or prod)')
    args = parser.parse_args()
    return args.env, Config.ENV_TEST if args.env == 'test' else Config.ENV_PROD


def read_token(env):
    file_name = f"{env}_token.txt"
    with open(file_name, 'r') as f:
        return f.read().strip()


if __name__ == '__main__':
    env, config = return_environment_from_args()
    keyring_util = KeyringUtil()
    token = keyring_util.get_token(env)
    # token = read_token(env)

    stock_holding = StockHolding(config, token)
    stock_count = stock_holding.get_positions()

    cash_holding = CashHolding(config, token)
    buying_power = cash_holding.get_cash()
    print(buying_power)

    if stock_count == 0:
        buy_executor = BuyExecutor(config, token)
        buy_executor.send_order()
    else:
        sell_executor = SellExecutor(config, token)
        sell_executor.send_order()
