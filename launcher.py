import subprocess
import time
import schedule
import psutil
from config import Config
from src.api.token_fetcher import TokenFetcher
from src.util.keyring_util import KeyringUtil

keyring_util = KeyringUtil()

def open_app():
    subprocess.Popen(
        r"C:\Users\kei-c\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\kabu.com\kabuステーション.appref-ms")


def save_token(env):
    """Fetch and store the token based on the environment."""

    if not is_kabuS_running():
        clear_token(env)
        return

    if keyring_util.is_token_set(env): return

    print(f"{env}用トークンを取得します。")

    config = Config.ENV_TEST if env == 'test' else Config.ENV_PROD

    token_manager = TokenFetcher(config)
    token = token_manager.fetch_token()

    keyring_util.set_token(env, token)

    print(f"{env}のトークンを取得しました。")


def clear_token(env):
    keyring_util.clear_token(env)
    print(f"{env}用トークンを削除しました。")


def is_kabuS_running():
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == 'KabuS.exe':
            return True
    return False

# clear_token('test')
# clear_token('prod')
schedule.every().day.at("07:50").do(open_app)
schedule.every().day.at("07:55").do(clear_token, 'test')
schedule.every().day.at("07:56").do(clear_token, 'prod')
schedule.every(10).minutes.do(save_token, 'test')
schedule.every(10).minutes.do(save_token, 'prod')

while True:
    schedule.run_pending()
    time.sleep(1)
