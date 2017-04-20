"""Binary encoder implements Binary encoding
"""
from collections import Counter, defaultdict

from categorical_encoder.base_encoder import Encoder


class BinaryEncoder(Encoder):
    """Binary encoder class

    Binary transformation
    """

    def fit(self, column):

        count = Counter(column)
        self.most_common = count.most_common(1)[0][0]

        binary = len('{0:b}'.format(len(count) - 1))
        self.encoding_length = binary

        translation_dict = {}
        for i, k in enumerate(sorted(count.keys())):
            translation_dict[k] = [
                int(_) for _ in '{0:b}'.format(i).zfill(binary)
            ]

        self.translation_dict = defaultdict(
            lambda: translation_dict[self.most_common]
        )
        for key, value in translation_dict.items():
            self.translation_dict[key] = value

        return self
