import nltk
from nltk.collocations import *
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def tagify(text):
    bigram_measures = nltk.collocations.BigramAssocMeasures()

    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    print tokenizer.tokenize(
        strip_tags(
            text
        )
    )
    import ipdb; ipdb.set_trace()

    finder = BigramCollocationFinder.from_words(
        tokenizer.tokenize(
            strip_tags(
                text
            )
        )
    )

    finder.apply_freq_filter(3)
    return finder.nbest(bigram_measures.pmi, 5)