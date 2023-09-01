import os
import keyring
from dotenv import load_dotenv

load_dotenv()


class KeyringUtil:

    def __init__(self):
        self.service_name = os.getenv('SERVICE_NAME')

    def set_token(self, env, token):
        keyring.set_password(self.service_name, env, token)

    def get_token(self, env):
        return keyring.get_password(self.service_name, env)

    def clear_token(self, env):
        keyring.delete_password(self.service_name, env)

    def is_token_set(self, env):
        return self.get_token(env) is not None
