# This is a python program
from concurrent.futures import ThreadPoolExecutor
"""nice know nothing about python"""
def vector_add(a, b):
    return [x + y for x, y in zip(a, b)]

def dot_product(a, b):

    if len(a) != len(b):
        raise ValueError("Vectors must be of the same length.")
    return sum([x * y for x, y in zip(a, b)])

    with ThreadPoolExecutor() as executor:
        results = executor.map(lambda pair: pair[0] * pair[1], zip(a, b))
    return sum(results)


if __name__ == "__main__":
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    v3 = [10,11,12]
    print("Vector sum:", vector_add(v1, v2))
    print("Parallel Dot Product of vector:", dot_product(v1, v2))
