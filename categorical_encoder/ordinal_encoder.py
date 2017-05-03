"""Ordinal encoder module implements Ordinal encoding
"""
from collections import Counter

from categorical_encoder.base_encoder import Encoder


class OrdinalEncoder(Encoder):
    """Ordinal encoder class

    Ordinal transformation
    """

    def fit(self, column):

        count = Counter(column)
        self.most_common = count.most_common(1)[0][0]

        for i, k in enumerate(sorted(count.keys())):
            self.translation_dict[k] = i

        return self
