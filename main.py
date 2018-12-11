#!/usr/bin/python3

from model import Model
from corpus import Corpus

if __name__ == '__main__':
	corpus = Corpus(default = True, size = 100)
	model = Model(corpus, iterations = 4000, burn = 500)
	model.showTopWordsPerTopic()