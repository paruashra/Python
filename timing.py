from functools import wraps
from time import time


def speed_test(fn):
    
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"executing  {fn.__name__}")
        print(f"Time Elapsed: {end_time - start_time}")
        return result

    return wrapper


@speed_test
def sum_nums_gen():
    return sum(x for x in range(1, 100))        


@speed_test
def sum_nums_list():
    return sum([x for x in range(1, 100)])     


print(sum_nums_gen())
print(sum_nums_list())
