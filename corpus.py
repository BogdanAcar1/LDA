#!/usr/bin/python3
import string
import glob
import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from bs4 import BeautifulSoup

nltk.download("stopwords")
stopwords = stopwords.words("english")

MIN_WORD_LENGTH = 5

def lemmatize(word):
	return WordNetLemmatizer().lemmatize(word)

def normalize(word):
	return lemmatize(word.translate(str.maketrans('', '', string.punctuation)).lower())

def filter(word):
	return word not in stopwords and len(word) >= MIN_WORD_LENGTH and word.isalpha()

class Corpus(object):

	def buildObservations(self, documents):
		index = 0
		wordIndex = {}
		vocab = {}
		for doc in documents:
			for word in doc:
				if word not in wordIndex:					
					wordIndex[word] = index					
					vocab[index] = word
					index = index + 1
		words = []
		for doc in documents:
			words.append([wordIndex[word] for word in doc])
		return index - 1, words, vocab

	def readBleiApCorpus(self):		
		dataset = BeautifulSoup(open("blei-ap.txt"), "html.parser")
		documents = [text.contents[0] for  text in dataset.findAll("text")]
		return documents

	def readResourceCorpus(self):
		files = glob.glob("res/*.txt")
		documents = []
		for file in files:
			with open(file, "r") as doc:
				documents.append(doc.read())
		return documents;

	def __repr__(self):
		return """Document corpus summary: source: %s, documents: %d, words: %d""" % (self.source, self.documentCount, self.wordCount)

	def __init__(self, default = True, size = 50):
		self.source = "blei-ap corpus" if default == True else "res"
		self.documents = []
		self.vocabulary = {}

		docs = []
		if default == True:
			allDocs = self.readBleiApCorpus()			
			for i in np.linspace(0, len(allDocs) - 1, dtype = int, num = size):
				docs.append(allDocs[i])
		else:
			docs = self.readResourceCorpus()
		for doc in docs:
			self.documents.append([normalize(word) for word in doc.split() if filter(normalize(word))])

		self.documentCount = len(self.documents)
		(self.wordCount, self.observations, self.vocabulary) = self.buildObservations(self.documents)

		print(self)