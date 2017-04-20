"""Base encoder module implements Encoder object
from which every encoder inherits
"""
from collections import Counter, defaultdict


class Encoder(object):
    """Base encoder class

    Identity transformation
    """

    def __init__(self):
        """Simple initialization

        translation_dict -- python dict use to associate values to encoding
        most_common -- used to translate unknown value ; unknown value is
            encoded as most common value
        """

        self.translation_dict = {}
        self.most_common = ''
        self.encoding_length = 1

    def __repr__(self):
        """Representation of class is its translation dictionnary"""

        return str(self.translation_dict)

    def fit(self, column):
        """Fit a column of values

        - Count modalities
        - Save most common
        - Build translation dictionnary
        """

        count = Counter(column)
        self.most_common = count.most_common(1)[0][0]

        translation_dict = {}
        for _, k in enumerate(count.keys()):
            translation_dict[k] = k

        self.translation_dict = defaultdict(
            lambda: translation_dict[self.most_common]
        )
        for key, value in translation_dict.items():
            self.translation_dict[key] = value

        return self

    def transform(self, column):
        """Transform a column of values
        """

        return [self.translation_dict[_] for _ in column]
