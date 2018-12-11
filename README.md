# Pymc Latent Dirichlet Allocation 

Pymc implemetation of topic extraction algorithm using Latent Dirichlet Allocation for Probabilistic Programming course. 

### Installing

```
pip3 install requirements.txt
```

### Project Structure

The two main classes are:
 * ```Corpus.py``` reads a corpus of documents  and builds the observed variable that is later used in the LDA model. The corpus source can either be the a ```size```-document subset of the blei-ap corpus from https://github.com/tdhopper/topic-modeling-datasets/blob/master/data/lda-c/blei-ap/ap.txt or a collection of ```.txt``` files under the ```/res``` directory of the project (set ```default = False``` when creating the corpus object). In the corpus creation, basic word normalization and clean-up is performed via lemmatization and stopword removal.
 * ```Model.py```  creates and fits the LDA model based on http://www.cs.columbia.edu/~blei/papers/Blei2012.pdf. The constructor for this class has one required parameter, ```corpus``` and three optional ones: ```K``` - number of topics expected in the corpus, ```iterations``` - the number of model fitting iterations, and ```burn``` the number of fitting samples to discard. The method ```showTopWordsPerTopic``` displays the ```top``` most descriptive words in the vocabulary for each topic.

### Running

Run project using ```python3 main.py```. Change constructor arguments in ```main.py``` for variations in the topic modelling algorithm parameters.

### Results

The following ```top = 10``` most significant words per topic were obtained for a subset of ```size = 100``` documents from the blei-ap corpus, using the following LDA model parameters ```K = 10, iterations = 4000, burn = 500```:
```
Topic 0:  ['radio', 'affirmative', 'corralled', 'alarmed', 'elsewhere', 'damned', 'treatment', 'shearson', 'pressure', 'commitment']
Topic 1:  ['suspended', 'consider', 'effort', 'secondmost', 'marked', 'perfect', 'announced', 'pleaded', 'precipitous', 'witness']
Topic 2:  ['okinawa', 'backdating', 'measurement', 'moving', 'manslaughter', 'proponent', 'overall', 'attack', 'withheld', 'breakin']
Topic 3:  ['foreign', 'allen', 'restriction', 'horner', 'preparing', 'searing', 'ballet', 'detroit', 'attention', 'instinct']
Topic 4:  ['russian', 'latin', 'gairy', 'assistant', 'silesian', 'caucus', 'prosoviet', 'check', 'agent', 'baltic']
Topic 5:  ['solving', 'industrial', 'vashem', 'couture', 'privatization', 'nayokpuk', 'manufacturer', 'attention', 'anymore', 'sometime']
Topic 6:  ['joined', 'altman', 'trusted', 'mechanic', 'nimitz', 'unseasonably', 'stepped', 'trunk', 'merger', 'cicero']
Topic 7:  ['percent', 'wealthier', 'reducing', 'million', 'growth', 'found', 'symbol', 'dollar', 'softening', 'selling']
Topic 8:  ['lowerfat', 'reduce', 'another', 'backfire', 'comedian', 'sequined', 'procrastinating', 'nimitz', 'alleging', 'aircraft']
Topic 9:  ['figure', 'surveyed', 'weight', 'cryostat', 'driver', 'represented', 'champagne', 'beleaguered', 'reality', 'oxymoron']
```
It can be observed that topic 7 may be associated with the financial domain, while most words in topic 2 seem to be related to crime.