import time


def timer(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        func(*args, **kwargs)
        print("Function took: ", time.time() - before, "seconds")

    return wrapper


@timer
def run():
    time.sleep(2)


run()


@timer
def say_hello():
    print("Hello")


say_hello()
