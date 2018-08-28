from collections import namedtuple
import sklearn.covariance as covariance
import numpy as np
import pandas as pd


def generate_data(a=0.5, noise=0.02, p_anomaly=0.01, size=1000, seed=None):
    size = int(size)
    if seed is not None:
        np.random.seed(seed)
    likes_given = np.random.exponential(scale=500.0, size=size).astype(int)
    log10_likes_received = (a + np.random.randn(size) * noise) * np.log10(likes_given + 1)
    likes_received = (10 ** log10_likes_received)
    likes_received[likes_received < 0] = 0
    sel_anomaly = (likes_given > 1000) & (np.random.rand(size) < p_anomaly)
    likes_received[sel_anomaly] = likes_received[sel_anomaly] * 0.05
    likes_received = likes_received.astype(int)

    data = pd.DataFrame(
        {
            'likes_given': likes_given,
            'likes_received': likes_received,
            'userid': [f'fake{i:07d}' for i in range(size)]
        }
    )
    return data


RegressionResult = namedtuple('RegressionResult', ['kind', 'a', 'b', 'r2', 'fitted_y'])


def linear_regression(x, y) -> RegressionResult:
    x = np.array(x)  # to handle Python lists or tuples
    y = np.array(y)
    a, b = np.polyfit(x, y, deg=1)
    r2 = np.corrcoef(x, y)[0, 1] ** 2
    fitted_y = np.polyval([a, b], x)
    return RegressionResult('linear', a, b, r2, fitted_y)


def summarize_linear_regression(x, y) -> str:
    result = linear_regression(x, y)
    a = result.a
    b = result.b
    r2 = result.r2
    ret = f'$y={a:.2f}x + {b:.2f}$; $R^2={r2:.2f}$'
    return ret


def loglog_regression(x, y) -> RegressionResult:
    log10_x = np.log10(x)
    log10_y = np.log10(y)
    result = linear_regression(log10_x, log10_y)
    ret = RegressionResult(
        kind='logglog',
        a=result.a,
        b=10 ** result.b,
        r2=result.r2,
        fitted_y=np.power(10, result.fitted_y)
    )
    return ret


def select_outliers(xy, n_std=2.0):
    detector = covariance.outlier_detection.MinCovDet().fit(xy)
    centered_dist = (detector.dist_ - np.mean(detector.dist_)) / np.std(detector.dist_)
    selection = centered_dist > n_std
    return selection