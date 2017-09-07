import numpy as np


def matrix():
    x = np.random.normal(loc=1, scale=10, size=(1000, 50))
    print x


if __name__ == "__main__":
    matrix()