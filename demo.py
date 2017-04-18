"""Demo module for categorical_encoder package
"""
from sklearn import cross_validation, linear_model

from categorical_encoder.encoder_service import EncoderService
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

    encoding_svc = EncoderService(
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


def run(data, target, mask=None, **kwargs):
    """run study for data vs target
    """

    ordinal, binary = study(data, target, mask)

    print_accuracy(ordinal, text=kwargs['title'] + ', ordinal')
    print_accuracy(binary, text=kwargs['title'] + ', binary')


def run_demo():
    """Run demo for car + mushroom + splice data
    """

    downloader.download_car_data()
    data, target, mask = loader.get_car_data('data/cars/car.data.txt')
    run(data, target, mask, title='Car data')

    downloader.download_mushroom_data()
    data, target = loader.get_mushroom_data(
        'data/mushrooms/agaricus-lepiota.data.txt'
    )
    run(data, target, title='Mushroom data')

    downloader.download_splice_data()
    data, target = loader.get_splice_data(
        'data/splice/splice.data.txt'
    )
    run(data, target, title='Splice data')


if __name__ == '__main__':
    """Quick encoding tests on multiple categorical datasets
    """

    run_demo()
