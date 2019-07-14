import json

"""
* HTTP レスポンスヘッダを出力するようなデコレータ？
"""



class Utils:

    @staticmethod
    def dump2json(segment: str, filename: str, response_json: dict) -> None:
        path = '../../response_samples/{}/{}.json'.format(segment, filename)
        with open(path, mode='w', encoding='utf-8') as f:
            json.dump(response_json, f,
                      ensure_ascii=False,
                      indent=4,
                      separators=(',', ':')
                      )
