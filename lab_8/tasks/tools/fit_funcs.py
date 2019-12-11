import numpy as np


def least_sq(xy):
    """
    Fits linear function to given vector of 2D points.

    Funkcja liczy parametry funkcji liniowej ax+b do danych za pomocą metody
    najmniejszych kwadratów.
    (1 pkt.)

    A = (Sum(x^2)*Sum(y)-Sum(x)*Sum(xy))/Delta
    B = (N*Sum(xy)-Sum(x)*Sum(y))/Delta
    Delta = N*Sum(x^2) - (Sum(x)^2)

    :param xy: vector of 2D points (shape (2, n))
    :type xy: np.ndarray
    :return: Tuple of fitted parameters
    """
    n = xy.shape[1]
    delta = n*np.sum(np.power(xy[0], 2)) - np.power(np.sum(xy[0]), 2)
    b = (np.sum(np.power(xy[0], 2))*np.sum(xy[1]) - np.sum(xy[0])*np.sum(xy[0] * xy[1])) / delta
    a = (n*np.sum(xy[0] * xy[1]) - np.sum(xy[0])*np.sum(xy[1])) / delta

    return tuple([a, b])

