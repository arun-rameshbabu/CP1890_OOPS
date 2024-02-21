def fun_generator():
    yield 'CP1850 Class is fantastic'
    yield "Maybe it's because of the instructor?"
    yield 'Or is it the students? Putting in the points?'


obj = fun_generator()

print(type(obj))
print(next(obj))
print(next(obj))
print(next(obj))

test_list = [1, 2, 3, 4, 5, 6, 7]


def print_even(some_list):
    for i in some_list:
        if (i % 2) == 0:
            yield i


for k in print_even(test_list):
    print(k, end=' ')
