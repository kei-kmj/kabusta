from src.token_manager import TokenManager
from src.buy_order_sender import BuyOrderSender
from src.sell_order_sender import SellOrderSender
from src.positions import Positions
from config import Config
import argparse


def return_environment_from_args():
    parser = argparse.ArgumentParser(description='Fetch API token')
    parser.add_argument('--env', choices=['test', 'prod'], default='test', help='Specify environment (test or prod)')
    args = parser.parse_args()
    return Config.ENV_TEST if args.env == 'test' else Config.ENV_PROD


if __name__ == '__main__':
    config = return_environment_from_args()
    token_manager = TokenManager(config)
    token = token_manager.fetch_token()

    positions = Positions(config, token)
    position_quantity = positions.get_positions()

    if position_quantity == 0:
        buy_order = BuyOrderSender(config, token)
        buy_order.send_order()
    else:
        sell_order = SellOrderSender(config, token)
        sell_order.send_order()


