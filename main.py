#!/usr/bin/python3

from model import Model
from corpus import Corpus

if __name__ == '__main__':
	corpus = Corpus(default = True, size = 10)
	model = Model(corpus, iterations = 50, burn = 5)
	model.showTopWordsPerTopic()