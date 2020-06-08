import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        taken = time.time() - start
        print('Time taken: {:0.2f}'.format(taken))

        return taken

    return wrapper
