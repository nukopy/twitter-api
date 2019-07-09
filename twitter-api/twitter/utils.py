"""
* HTTP レスポンスヘッダを出力するようなデコレータ？
"""

API_VERSION = '1.1'
URL = f'https://api.twitter.com/{API_VERSION}/'


class Utils:
    @staticmethod
    def create_endpoint(segment: str) -> str:
        """
        ex)
        endpoint: 'lists/members'
            * category: lists
            * name: members
        """
        return URL + segment + '.json'
