from api import TwitterAPI
from utils import Utils
from error import TwitterError
import requests


def bind(**config):
    api = config['api']
    path: str = config['path']
    method: str = config['method']
    params: dict = config['params']

    with requests.Session() as session:
        try:

            pass

        except TwitterError as err:
            pass
