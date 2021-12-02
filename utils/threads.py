from functools import wraps
from threading import Thread
from typing import Callable


def threaded(fn: Callable):
    """Multi-threaded function wrapper

    Args:
        fn (function): wrapped function

    Returns:
        Thread: wrapped function
    """

    @wraps(fn)
    def wrapper(*args, **kwargs):
        thread: Thread = Thread(target=fn, args=args, kwargs=kwargs)
        args[0].threads.append(thread)
        thread.start()
        return thread

    return wrapper
