from topia.termextract import extract

# Python 3 moves HTMLParser to html.parser
try:
    from HTMLParser import HTMLParser as htmlparse
except ImportError:
    from html.parser import HTMLParser as htmlparse

class MLStripper(htmlparse):
    def __init__(self):
        self.convert_charrefs=False
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
    text = strip_tags(text)

    extractor = extract.TermExtractor()
    extractor.filter = extract.DefaultFilter(singleStrengthMinOccur=4)

    return [w for (w, x, y) in extractor(text)[:5] if len(w) < 25]