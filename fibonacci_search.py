from typing import Iterable, Optional


class FibonacciSearcher:
    def __init__(self, collection: Optional[Iterable] = None):
        self._array = [] if collection is None else list(collection)
        self._array.sort()

    def find_element_index(self, el):
        fib1 = 1
        fib2 = 0
        fib = 1
        shift = 0
        while fib1 + shift < len(self._array):
            index = fib + shift - 1
            if self._array[index] == el:
                return index
            elif self._array[index] < el:
                fib2 = fib1
                fib1 = fib
                fib = fib1 + fib2 if fib1 + fib2 + shift < len(self._array) else len(self._array) - shift
            else:
                shift += fib1
                fib2 = 0
                fib1 = 1
                fib = 1
        return -1

    def find_element(self, el):
        return self.find_element_index(el) != -1

    def add_element(self, el):
        fib1 = 1
        fib2 = 0
        fib = 1
        shift = 0
        max_index_lt = 0
        min_index_gt = len(self._array) - 1
        while fib1 + shift < len(self._array):
            index = fib + shift - 1
            if self._array[index] == el:
                self._array.insert(index, el)
                break
            elif min_index_gt - max_index_lt <= 1:
                self._array.insert(max_index_lt, el)
                break
            elif self._array[index] < el:
                max_index_lt = max(max_index_lt, index)
                fib2 = fib1
                fib1 = fib
                fib = fib1 + fib2 if fib1 + fib2 + shift < len(self._array) else len(self._array) - shift
            else:
                min_index_gt = min(min_index_gt, index)
                shift += fib1
                fib2 = 0
                fib1 = 1
                fib = 1

    def delete_element(self, el):
        index = self.find_element_index(el)
        if index != -1:
            self._array.pop(index)


if __name__ == '__main__':
    arr = [4, 8, 34, -6, 11, 7, 1, 0, -5, 2]
    searcher = FibonacciSearcher(arr)
    print(searcher.find_element(7))
    print(searcher.find_element(-1))
    searcher.add_element(-1)
    searcher.add_element(-8)
    print(searcher.find_element(-1))
    searcher.delete_element(8)
    print(searcher.find_element(8))
    searcher.delete_element(4)
    print(searcher.find_element(4))
    print(searcher.find_element(-6))
    print(searcher.find_element(7))
