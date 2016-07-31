from sklearn import cross_validation, linear_model

import categorical_encoder
from loader import loader, downloader


def study(X, y, mask=None):
    """Produces scores for different encoding"""

    ordinal_scores = scores_for(X, y, 'ordinal', mask)
    binary_scores = scores_for(X, y, 'binary', mask)

    return ordinal_scores, binary_scores


def scores_for(X, y, encoding_type, mask=None):
    """Get scores for the data X, y with the encoding encoding_type"""

    eSvc = categorical_encoder.EncoderService(
        encoder_type=encoding_type,
        value_mask=mask
    )
    X = eSvc.fit_transform(X)

    clf = linear_model.LogisticRegression()
    scores = cross_validation.cross_val_score(
        clf, X, y, cv=10
    )

    return scores


def print_accuracy(scores, text='', terminator='\n'):
    """Print to standard output accuracy and standard deviation"""

    the_str = text + '\n' + "Accuracy: %0.4f (+/- %0.4f)" % (
        scores.mean(),
        scores.std() * 2
    ) + terminator
    print the_str

if __name__ == '__main__':
    """Quick encoding tests on multiple categorical datasets"""

    downloader.download_car_data()

    X, y, mask = loader.get_car_data('data/cars/car.data.txt')
    o_scores, b_scores = study(X, y, mask)
    print_accuracy(o_scores, text='Car data, ordinal')
    print_accuracy(b_scores, text='Car data, binary')

    downloader.download_mushroom_data()

    X, y = loader.get_mushroom_data('data/mushrooms/agaricus-lepiota.data.txt')
    o_scores, b_scores = study(X, y)
    print_accuracy(o_scores, text='Mushroom data, ordinal')
    print_accuracy(b_scores, text='Mushroom data, binary')

    downloader.download_splice_data()

    X, y = loader.get_splice_data('data/splice/splice.data.txt')
    o_scores, b_scores = study(X, y)
    print_accuracy(o_scores, text='Splice data, ordinal')
    print_accuracy(b_scores, text='Splice data, binary')
