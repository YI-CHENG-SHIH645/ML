from sklearn.model_selection import train_test_split
from utils import DataLoader


def fetch_iowa():
    cols = ['LotArea', 'OverallQual', 'OverallCond', 'SalePrice']
    data = DataLoader.load_data('iowa_original')[cols].values
    x, y = data[:, :3], data[:, -1]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33)

    return (x_train, x_test), (y_train, y_test)


def stdize(x_train, x_test):
    mu, sigma = x_train.mean(0), x_train.std(0)

    return (x_train - mu) / sigma, (x_test - mu) / sigma
