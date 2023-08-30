import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    ENV_TEST = {
        'APIPassword': os.getenv('TEST_API_PASSWORD'),
        'URL': os.getenv('TEST_URL'),
        'env': 'test'
    }
    ENV_PROD = {
        'APIPassword': os.getenv('PROD_API_PASSWORD'),
        'URL': os.getenv('PROD_URL'),
        'env': 'prod'
    }