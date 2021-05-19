from utils import DataLoader


def fetch_iowa():
    cols = ['LotArea', 'OverallQual', 'OverallCond', 'SalePrice']
    data = DataLoader.load_data('iowa_original')[cols].values
    x_train, y_train = data[:2000, :3], data[:2000, -1]
    x_test, y_test = data[2000:, :3], data[2000:, -1]

    return (x_train, x_test), (y_train, y_test)


def stdize(x_train, x_test):
    mu, sigma = x_train.mean(0), x_train.std(0)

    return (x_train - mu) / sigma, (x_test - mu) / sigma
