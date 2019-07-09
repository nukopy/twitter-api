import os
import tweepy
from pycallgraph import PyCallGraph, Config
from pycallgraph.output import GraphvizOutput


def main():
    # config
    depth = 7
    config = Config(max_depth=depth)
    graphviz = GraphvizOutput(output_file='test_tweepy.png')

    with PyCallGraph(output=graphviz, config=config):
        # const
        consumer_key = os.environ['TW_CONSUMER_KEY']
        consumer_secret = os.environ['TW_CONSUMER_SECRET']
        access_token = os.environ['TW_ACCESS_TOKEN']
        access_secret = os.environ['TW_ACCESS_SECRET']

        # api
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        api = tweepy.API(auth)

        # search
        word = ['Python']
        set_count = 10
        results = api.search(q=word, count=set_count)


if __name__ == "__main__":
    main()
