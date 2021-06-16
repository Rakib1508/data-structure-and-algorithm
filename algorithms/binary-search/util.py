import time


def stopwatch(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(function.__name__, 'took', str(
            (end - start) * 1000), 'millisecond')
        return result
    return wrapper
