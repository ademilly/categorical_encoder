"""Encoder service module provides an EncoderService class handling
encoding usage
"""
from categorical_encoder.binary_encoder import BinaryEncoder
from categorical_encoder.ordinal_encoder import OrdinalEncoder
from categorical_encoder.utils import transpose


class EncoderService(object):
    """Encoding service class

    Manages encoders for a categorical dataset

    encoder_dict -- dict of encoders available to all instance of
    EncoderService
    """

    encoder_dict = {
        'binary': BinaryEncoder,
        'ordinal': OrdinalEncoder
    }

    def __init__(self, encoder_type='binary', value_mask=None):
        """Initialize class

        Keyword arguments:
        encoder_type -- string to be chosen among encoder_dict.keys()
            (defaut: 'binary')
        value_mask -- dict transforming values for each columns of dataset
        """

        self.encoders = {}
        self.encoder_type = encoder_type
        self.value_mask = value_mask

    def apply_mask(self, columns):
        """Transform data following value_mask"""

        new_columns = []
        for i, col in enumerate(columns):
            new_columns += [
                [self.value_mask[str(i)][_] for _ in col]
            ]

        return new_columns

    def fit_transform(self, data):
        """Fit categorical dataset to encoding then transform it"""

        columns = transpose(data)
        if self.value_mask is not None:
            columns = self.apply_mask(columns)

        for i, _ in enumerate(columns):
            self.encoders[str(i)] = self.encoder_dict[
                self.encoder_type
            ].__call__()
            columns[i] = self.encoders[str(i)].fit(columns[i]) \
                .transform(columns[i])

        return transpose(
            columns,
            flatten=self.encoder_type in ['binary']
        )
