from tenacity import retry, wait_fixed, stop_after_attempt, retry_if_exception_type

@retry(wait=wait_fixed(2), stop=stop_after_attempt(5), retry=retry_if_exception_type(Exception))
def retry_on_exception(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
