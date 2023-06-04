import functools
import logging

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


def logged(custom_exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except custom_exception as e:
                if mode == "console":
                    logging.basicConfig(level=logging.INFO)
                    logging.error(e)
                elif mode == "file":
                    logging.basicConfig(level=logging.INFO, filename="exception.log", filemode="a")
                    logging.error(e)
                else:
                    raise ValueError("Invalid logging mode. Please choose 'console' or 'file'.")
        return wrapper
    return decorator

