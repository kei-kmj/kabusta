from src.buy_order_sender import BuyOrderSender
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

    positions = StockHolding(config, token)
    position_quantity = positions.get_positions()

    cash = CashHolding(config, token)
    cash_quantity = cash.get_cash()
    print(cash_quantity)

    # if position_quantity == 0:
    #     buy_order = BuyOrderSender(config, token)
    #     buy_order.send_order()
    # else:
    #     sell_order = SellOrderSender(config, token)
    #     sell_order.send_order()
