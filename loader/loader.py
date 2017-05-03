"""Various loaders for datasets
from https://archive.ics.uci.edu/ml/machine-learning-databases/
"""


def get_car_data(src_file):
    """Load car data
    """

    mapping_dict = {
        '0': {
            'vhigh': 3, 'high': 2, 'med': 1, 'low': 0
        },
        '1': {
            'vhigh': 3, 'high': 2, 'med': 1, 'low': 0
        },
        '2': {
            '2': 0, '3': 1, '4': 2, '5more': 3
        },
        '3': {
            '2': 0, '4': 1, 'more': 2
        },
        '4': {
            'small': 0, 'med': 1, 'big': 2
        },
        '5': {
            'low': 0, 'med': 1, 'high': 2,
        }
    }

    data, target = [], []
    with open(src_file) as fin:

        for _ in fin:

            line = _.replace('\n', '').split(',')
            data += [
                [_ for _ in line[:-1]]
            ]
            target += [line[-1]]

    return data, target, mapping_dict


def get_mushroom_data(src_file):
    """Load mushroom data
    """

    data, target = [], []
    with open(src_file) as fin:

        for _ in fin:

            line = _.replace('\n', '').split(',')
            data += [line[1:]]
            target += [line[0]]

    return data, target


def get_splice_data(src_file):
    """Load splice data
    """

    data, target = [], []
    with open(src_file) as fin:

        for _ in fin:

            line = _.replace('\n', '').replace(' ', '').split(',')
            data += [
                [_ for _ in line[2]]
            ]
            target += [line[0]]

    return data, target
