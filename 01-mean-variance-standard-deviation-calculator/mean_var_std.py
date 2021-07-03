import numpy as np

ITEMS_SIZE = 9
NOT_ENOUGH_ITEMS_ERROR_MESSAGE = 'List must contain nine numbers.'


def calculate(items):
    if len(items) < ITEMS_SIZE:
        raise ValueError(NOT_ENOUGH_ITEMS_ERROR_MESSAGE)

    items_list = items[:ITEMS_SIZE] if len(items) > ITEMS_SIZE else items
    items_matrix = np.array(items_list).reshape((3, 3))
    items_metrics = {
        'mean': get_metric(items_matrix, np.mean),
        'variance': get_metric(items_matrix, np.var),
        'standard deviation': get_metric(items_matrix, np.std),
        'max': get_metric(items_matrix, np.max),
        'min': get_metric(items_matrix, np.min),
        'sum': get_metric(items_matrix, np.sum)
    }

    return items_metrics


def get_metric(matrix, metric_func):
    return [metric_func(matrix, axis=0).tolist(), metric_func(matrix, axis=1).tolist(), metric_func(matrix)]
