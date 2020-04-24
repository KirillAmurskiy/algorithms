from .time import timed
from matplotlib import pyplot as plt
import collections


def compare(fs, f_args, xs=None, n_iter=20):
    if not xs:
        xs = f_args
    if not isinstance(f_args[0], collections.Iterable):
        f_args = [[x] for x in f_args]
    for f in fs:
        plt.plot(xs, [timed(f, *arg, n_iter=n_iter) for arg in f_args], label=f.__name__)
        plt.legend()
        plt.grid(True)
    plt.show()
