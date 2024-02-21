def fun_generator():
    yield "CP1890"
    yield "Instructor"
    yield "Students"


objt = fun_generator()

print(type(objt))

print(next(objt))
print(next(objt))
print(next(objt))
# print(next(objt)) <- error.

test_list = [1, 4, 5, 6, 7]


def print_even(some_list):
    for i in some_list:
        if i % 2 == 0:
            yield i


print("\nThe even numbers in the list are:", end=" ")
for x in print_even(test_list):
    print(x, end=" ")
print("")