import subprocess
import time
import schedule
import psutil
from config import Config
from src.token_manager import TokenManager


def open_app():
    subprocess.Popen(
        r"C:\Users\kei-c\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\kabu.com\kabuステーション.appref-ms")


def fetch_token(env):
    """Fetch and store the token based on the environment."""

    if not is_kabuS_running():
        clear_token(env)
        return

    file_path = get_file_path(env)

    if not is_file_empty(file_path):
        return

    print(f"{env}のトークンを取得します。")

    config = Config.ENV_TEST if env == 'test' else Config.ENV_PROD

    token_manager = TokenManager(config)
    token = token_manager.fetch_token()

    write_to_file(file_path, token)

    print(f"{env}のトークンを取得しました。")


def get_file_path(env):
    """Get file for token writing"""
    return f"{env}_token.txt"


def write_to_file(file_path, token):
    with open(file_path, 'w') as f:
        f.write(token)


def is_file_empty(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip() == ''


def clear_token(env):
    with open(f"{env}_token.txt", 'w') as f:
        f.write('')


def is_kabuS_running():
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == 'KabuS.exe':
            return True
    return False


schedule.every().day.at("07:50").do(open_app)
schedule.every().day.at("07:55").do(clear_token, 'test')
schedule.every().day.at("07:56").do(clear_token, 'prod')
schedule.every(10).minutes.do(fetch_token, 'test')
schedule.every(10).minutes.do(fetch_token, 'prod')

while True:
    schedule.run_pending()
    time.sleep(1)
