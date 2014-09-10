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