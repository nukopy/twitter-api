from pycallgraph import PyCallGraph, Config
from pycallgraph.output import GraphvizOutput
import time
import pandas as pd


def hello():
    print('Hello')


def world():
    pass


class Banana:
    def __init__(self, *args, **kwargs):
        pass

    def eat(self):
        self.secret_function()
        for i in range(3):
            self.chew()
        for j in range(5):
            self.swallow()

    def secret_function(self):
        time.sleep(0.2)

    def chew(self):
        pass

    def swallow(self):
        pass


def main():
    config = Config(max_depth=2)
    graphviz = GraphvizOutput(output_file='filter_none.png')

    with PyCallGraph(output=graphviz, config=config):
        foo = Banana()
        foo.eat()
        foo.chew()
        bar = Banana()
        bar.eat()
        bar.chew()

        for i in range(3):
            hello()
        for i in range(7):
            world()

        df = pd.DataFrame([i for i in range(10)])


if __name__ == "__main__":
    main()
