from collections import Counter

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

    def __repr__(self):
        """Representation of class is its translation dictionnary"""

        return str(self.translation_dict)

    def fit(self, column):
        """Fit a column of values

        - Count modalities
        - Save most common
        - Build translation dictionnary
        """

        c = Counter(column)
        self.most_common = c.most_common(1)[0][0]

        for i, k in enumerate(c.keys()):
            self.translation_dict[k] = k

        return self

    def transform(self, column):
        """Transform a column of values"""

        new_X = [
            self.translation_dict[_] if _ in self.translation_dict.keys()
            else self.translation_dict[self.most_common]
            for _ in column
        ]

        return new_X
