"""Download downloads datasets
"""
import os
import urllib

"""Download datasets
from https://archive.ics.uci.edu/ml/machine-learning-databases/
"""

DATA_ROOT = 'https://archive.ics.uci.edu/ml/machine-learning-databases/'


def download_car_data():
    """Download car data
    """

    local_dir = 'data/cars/'
    data_source = DATA_ROOT + 'car/car.data'

    if not os.path.isdir(local_dir):
        os.makedirs(local_dir)

    urllib.URLopener().retrieve(data_source, local_dir + 'car.data.txt')


def download_mushroom_data():
    """Download mushroom data
    """

    local_dir = 'data/mushrooms/'
    data_source = DATA_ROOT + 'mushroom/agaricus-lepiota.data'

    if not os.path.isdir(local_dir):
        os.makedirs(local_dir)

    urllib.URLopener().retrieve(
        data_source,
        local_dir + 'agaricus-lepiota.data.txt'
    )


def download_splice_data():
    """Download splice data
    """

    local_dir = 'data/splice/'
    data_source = DATA_ROOT + \
        'molecular-biology/splice-junction-gene-sequences/splice.data'

    if not os.path.isdir(local_dir):
        os.makedirs(local_dir)

    urllib.URLopener().retrieve(data_source, local_dir + 'splice.data.txt')
