import functools

def log_call(message):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(message)
            return func(*args, *kwargs)
        return wrapper
    return decorator

@log_call("Starting function execution")
def greet(name):
    print(f'Hello, {name}!')

greet('Alice!')