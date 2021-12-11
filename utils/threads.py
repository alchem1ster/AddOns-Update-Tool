"""Multithreading module"""

from functools import wraps
from threading import Thread
from typing import Callable


def threaded(callable_func: Callable):
    """Multi-threaded function wrapper

    Args:
        callable_func (function): wrapped function

    Returns:
        Thread: wrapped function
    """

    @wraps(callable_func)
    def wrapper(*args, **kwargs):
        thread: Thread = Thread(target=callable_func, args=args, kwargs=kwargs)
        args[0].threads.append(thread)
        thread.start()
        return thread

    return wrapper
