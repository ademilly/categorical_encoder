"""Various loaders for datasets
from https://archive.ics.uci.edu/ml/machine-learning-databases/
"""

def get_car_data(src_file):

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

    X, y = [], []
    with open(src_file) as fin:

        for _ in fin:

            l = _.replace('\n', '').split(',')
            X += [
                [_ for _ in l[:-1]]
            ]
            y += [l[-1]]

    return X, y, mapping_dict


def get_mushroom_data(src_file):

    X, y = [], []
    with open(src_file) as fin:

        for _ in fin:

            l = _.replace('\n', '').split(',')
            X += [l[1:]]
            y += [l[0]]

    return X, y


def get_splice_data(src_file):

    X, y = [], []
    with open(src_file) as fin:

        for _ in fin:

            l = _.replace('\n', '').replace(' ', '').split(',')
            X += [
                [_ for _ in l[2]]
            ]
            y += [l[0]]

    return X, y
