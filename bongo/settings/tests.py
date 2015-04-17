from django.test.runner import DiscoverRunner

class ReusableRunner(DiscoverRunner):
    '''Custom test runner that reuses databases, if possible.'''

    def __init__(self, **args):
        super(ReusableRunner, self).__init__(
            keepdb=True,
            pattern="*_tests.py",
            verbosity=2
        )