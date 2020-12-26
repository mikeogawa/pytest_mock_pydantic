import torch
from numpy.random import random
import MeCab

def generate_random():
    return random()

def amplify_10(x):
    return 10 * x

def process_10(x):
    return amplify_10(x)


def parse_sent(x):
    mecab = MeCab.Tagger("-d /tmp/xxxxx")
    return mecab.parse(x).split()
