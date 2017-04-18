"""Demo module for categorical_encoder package
"""
from sklearn import cross_validation, linear_model

import categorical_encoder
from loader import loader, downloader


def study(data, target, mask=None):
    """Produces scores for different encoding
    """

    ordinal_scores = scores_for(data, target, 'ordinal', mask)
    binary_scores = scores_for(data, target, 'binary', mask)

    return ordinal_scores, binary_scores


def scores_for(data, target, encoding_type, mask=None):
    """Get scores for the couple data, target with encoding_type
    """

    encoding_svc = categorical_encoder.EncoderService(
        encoder_type=encoding_type,
        value_mask=mask
    )
    data = encoding_svc.fit_transform(data)

    clf = linear_model.LogisticRegression()
    scores = cross_validation.cross_val_score(
        clf, data, target, cv=10
    )

    return scores


def print_accuracy(scores, text='', terminator='\n'):
    """Print to standard output accuracy and standard deviation"""

    the_str = text + '\n' + "Accuracy: %0.4f (+/- %0.4f)" % (
        scores.mean(),
        scores.std() * 2
    ) + terminator
    print the_str


def run(data_source):
    """run study for data_source
    """

    data, target, mask = loader.get_car_data(data_source)
    ordinal, binary = study(data, target, mask)

    print_accuracy(ordinal, text='Car data, ordinal')
    print_accuracy(binary, text='Car data, binary')


if __name__ == '__main__':
    """Quick encoding tests on multiple categorical datasets
    """

    downloader.download_car_data()
    run('data/cars/car.data.txt')

    downloader.download_mushroom_data()
    run('data/mushrooms/agaricus-lepiota.data.txt')

    downloader.download_splice_data()
    run('data/splice/splice.data.txt')
