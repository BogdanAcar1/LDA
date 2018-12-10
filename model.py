#!/usr/bin/python3
import numpy as np
import pymc as pm

class Model(object):

	def __init__(self, corpus, K = 10, iterations = 1000, burn = 100):
		print("Building model ...")
		self.K = K
		self.V = corpus.wordCount + 1
		self.M = corpus.documentCount
		self.alpha = np.ones(self.K)
		self.beta = np.ones(self.V)
		self.corpus = corpus
		self.observations = np.array(corpus.observations)

		self.phi = np.empty(self.K, dtype = object)
		for i in range(self.K):
			self.phi[i] = pm.CompletedDirichlet("Phi[%i]" % i, pm.Dirichlet("phi[%i]" % i, theta=self.beta))
		self.phi = pm.Container(self.phi)

		self.theta = np.empty(self.M, dtype = object)
		for i in range(self.M):
			self.theta[i] = pm.CompletedDirichlet("Theta[%i]" % i, pm.Dirichlet("theta[%i]" % i, theta=self.alpha))
		self.theta = pm.Container(self.theta)

		self.z = np.empty(self.observations.shape, dtype = object)
		for i in range(self.M):
			self.z[i] = pm.Categorical("z[%i]" % i, 
				                       size = len(self.observations[i]), 
				                  	   p = self.theta[i], 
				                  	   value = np.random.randint(self.K, size=len(self.observations[i])))
		self.z = pm.Container(self.z)

		self.w = []
		for i in range(self.M):
			self.w.append([])
			for j in range(len(self.observations[i])):
				self.w[i].append(pm.Categorical("w[%i][%i]" % (i, j), 
				                         		p = pm.Lambda("phi[z[%i][%i]]" % (i, j), lambda z = self.z[i][j], phi = self.phi: phi[z]), 
				                         		value = self.observations[i][j],
				                         		observed = True))
		self.w = pm.Container(self.w)				

		self.mcmc = pm.MCMC(pm.Model([self.theta, self.phi, self.z, self.w]))

		print("Fitting model ...")
		self.mcmc.sample(iter = iterations, burn = burn)

	def showTopWordsPerTopic(self, top = 10):
		wordDistribution = self.phi.value
		topWordsPerTopic = []
		for k in range(self.K):			
			topWordsIdx = np.argsort(wordDistribution[k][0])[-top:]
			topWords = [self.corpus.vocabulary[idx] for idx in topWordsIdx]
			topWordsPerTopic.append(topWords)
			print("Topic %i: " % k, str(topWords))




		
