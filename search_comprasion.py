import time
from random import sample, randrange
from typing import Iterable, Optional
from binary_search import BinarySearch
from binary_tree import BinaryTree
from fibonacci_search import FibonacciSearcher
from interpolation_search import InterpolationSearcher


class StandardSearch:
    """Надстройка над стандартной функцией для унификации интерфейса с реализованными в задании"""

    NAME = "Стандартная функция поиска"

    def __init__(self, collection: Optional[Iterable] = None):
        self._array = [] if collection is None else list(collection)

    def add_element(self, el):
        self._array.append(el)

    def find_element(self, el):
        return el in self._array

    def delete_element(self, el):
        if el in self._array:
            self._array.remove(el)


for length in (100000, 400000, 2000000, 4000000):
    nums = sample(range(length * 2), length)
    print(f"Length: {length}")
    for searcher_type in (BinarySearch, BinaryTree, FibonacciSearcher, InterpolationSearcher, StandardSearch):
        searcher = searcher_type(nums)
        start_time = time.time()
        for i in range(5):
            el = randrange(length * 2)
            if searcher.find_element(el):
                print(f"{el} is in array")
            else:
                print(f"{el} is not in array")
        print(searcher_type.NAME + " --- {0} ms ---".format(round((time.time() - start_time) * 1000)))
        print("="*30 + "\n")
