# Pymc Latent Dirichlet Allocation 

Pymc implemetation of topic extraction algorithm using Latent Dirichlet Allocation for Probabilistic Programming course. 

### Installing

```
pip3 install requirements.txt
```

## Project Structure

The two main classes are:
 * ```Corpus.py``` reads a corpus of documents  and builds the observed variable that is later used in the LDA model. The corpus source can either be the a ```size```-document subset of the blei-ap corpus from https://github.com/tdhopper/topic-modeling-datasets/blob/master/data/lda-c/blei-ap/ap.txt or a collection of ```.txt``` files under the ```/res``` directory of the project (set ```default = False``` when creating the corpus object). In the corpus creation, basic word normalization and clean-up is performed via lemmatization and stopword removal.
 * ```Model.py```  creates and fits the LDA model based on http://www.cs.columbia.edu/~blei/papers/Blei2012.pdf. The constructor for this class has one required parameter, ```corpus``` and three optional ones: ```K``` - number of topics expected in the corpus, ```iterations``` - the number of model fitting iterations, and ```burn``` the number of fitting samples to discard. The method ```showTopWordsPerTopic``` displays the ```top``` most descriptive words in the vocabulary for each topic.

## Running

Run project using ```python3 main.py```. Change constructor arguments in ```main.py``` for variations in the topic modelling algorithm parameters.

## Results

The following ```top = 10``` most significant words per topic were obtained for a subset of ```size = 100``` documents from the blei-ap corpus, using the following LDA model parameters ```K = 10, iterations = 4000, burn = 500```:
```
Topic 0:  ['original', 'slain', 'private', 'character', 'earlier', 'company', 'wonder', 'christian', 'rumored', screen']
Topic 1:  ['resolved', 'shell', 'grzegorz', 'pistol', 'killed', 'personality', 'jesus', 'tunnel', 'efficient', 'district']
Topic 2:  ['snapped', 'aircraft', 'report', 'grade', 'snapshot', 'democracy', 'instrument', 'group', 'peggy', 'economy']
Topic 3:  ['though', 'parent', 'constant', 'incident', 'widely', 'racism', 'airplane', 'would', 'california', 'screen']
Topic 4:  ['sometimes', 'first', 'afroamerican', 'arabian', 'anything', 'floor', 'kielce', 'revenue', 'considered', 'might']
Topic 5:  ['totaled', 'manadatory', 'worst', 'mattress', 'plane', 'purchased', 'determine', 'pastor', 'borrowed', 'relation']
Topic 6:  ['junior', 'tonsil', 'potential', 'antisubmarine', 'detective', 'anchor', 'slightly', 'firing', 'authority', 'firstdegree']
Topic 7:  ['robinson', 'collection', 'think', 'north', 'peggy', 'troubled', 'composition', 'finally', 'executed', 'sweet']
Topic 8:  ['companion', 'debra', 'didnt', 'economy', 'united', 'christian', 'safety', 'expected', 'manadatory', 'sometimes']
Topic 9:  ['experienced', 'serious', 'killjoy', 'elliott', 'statement', 'building', 'maurice', 'power', 'although', 'survivor']
```