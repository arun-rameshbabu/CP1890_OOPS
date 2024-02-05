# def f1():
#     print("Called F1")
#
# def f2(f):
#     f()
#
# f2(f1)

def f1(func):
    def wrapper():
        print("Started")
        func()
        print("Finished")

    return wrapper

@f1
def f():
    print("Hello")

# x = f1(f)
# x()

f()
