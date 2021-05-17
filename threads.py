import functools
import threading

def simple_thread(func):
    @functools.wraps(func)
    def wrapper():
        thread = threading.Thread(target=func)
        return thread
    return wrapper

def daemon_thread(func):
    @functools.wraps(func)
    def wrapper():
        thread = threading.Thread(target=func)
        thread.setDaemon(True)
        return thread
    return wrapper
