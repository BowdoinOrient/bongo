from django.core.management.base import BaseCommand
import nltk

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