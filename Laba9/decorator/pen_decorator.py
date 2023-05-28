import functools


def log_arguments_to_file(file_path):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with open(file_path, 'a') as file:
                file.write(f"{func.__name__}: ")
                for arg_name, arg_value in kwargs.items():
                    file.write(f"{arg_name}={arg_value} ")
                file.write('\n')
            return func(*args, **kwargs)
        return wrapper
    return decorator


def log_exceptions_to_file(file_path):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                with open(file_path, 'a') as file:
                    file.write(f"{func.__name__}: {type(e).__name__}\n")
                raise
        return wrapper
    return decorator
