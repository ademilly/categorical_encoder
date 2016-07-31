import os
import urllib

"""Download datasets
from https://archive.ics.uci.edu/ml/machine-learning-databases/
"""

data_root = 'https://archive.ics.uci.edu/ml/machine-learning-databases/'

def download_car_data():

    local_dir = 'data/cars/'
    data_source = data_root + 'car/car.data'

    if not os.path.isdir(local_dir):
        os.makedirs(local_dir)

    urllib.URLopener().retrieve(data_source, local_dir + 'car.data.txt')

def download_mushroom_data():

    local_dir = 'data/mushrooms/'
    data_source = data_root + 'mushroom/agaricus-lepiota.data'

    if not os.path.isdir(local_dir):
        os.makedirs(local_dir)

    urllib.URLopener().retrieve(
        data_source,
        local_dir + 'agaricus-lepiota.data.txt'
    )

def download_splice_data():

    local_dir = 'data/splice/'
    data_source = data_root + \
        'molecular-biology/splice-junction-gene-sequences/splice.data'

    if not os.path.isdir(local_dir):
        os.makedirs(local_dir)

    urllib.URLopener().retrieve(data_source, local_dir + 'splice.data.txt')
