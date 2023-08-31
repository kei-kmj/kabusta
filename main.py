from src.buy_executor import BuyExecutor
from src.sell_order_sender import SellOrderSender
from src.stock_holding import StockHolding
from src.cash_holding import CashHolding
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
    token = read_token(env)

    stock_holding = StockHolding(config, token)
    stock_count = stock_holding.get_positions()

    cash_holding = CashHolding(config, token)
    buying_power = cash_holding.get_cash()
    print(buying_power)

    buy_executor = BuyExecutor(config, token)
    buy_executor.send_order()

    # if stock_count == 0:
    #     buy_order = BuyOrderSender(config, token)
    #     buy_order.send_order()
    # else:
    #     sell_order = SellOrderSender(config, token)
    #     sell_order.send_order()
