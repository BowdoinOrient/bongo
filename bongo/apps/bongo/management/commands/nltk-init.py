from django.core.management.base import BaseCommand
import nltk
import os
from django.conf import settings
from tagger.extras import build_dict_from_nltk

class Command(BaseCommand):

    def handle(self, *args, **options):

        try:
            nltk.data.load('tokenizers/punkt/english.pickle')
            print("NLTK tokenizers already present!")
        except:
            print("Downloading NLTK tokenizers...")
            nltk.download("punkt")

        try:
            from nltk.corpus import brown
            print("Brown corpus already present!")
        except:
            print("Downloading Brown corpus...")
            nltk.download("brown")

        try:
            from nltk.corpus import stopwords
            print("NLTK stopwords already present!")
        except:
            print("Downloading NLTK stopwords...")
            nltk.download("stopwords")

        if os.path.exists(os.path.join(settings.SITE_ROOT, "data", "dict.pkl")):
            print("Tagging dictionary already present!")
        else:
            print("Building tagging dictionary...")
            build_dict_from_nltk(
                os.path.join(settings.SITE_ROOT, "data", "dict.pkl"),
                nltk.corpus.brown,
                nltk.corpus.stopwords.words('english'),
                measure='ICF'
            )