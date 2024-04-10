from typing import Iterable, Optional


class BinarySearch:

    NAME = "Бинарный поиск"

    def __init__(self, collection: Optional[Iterable] = None):
        self._array = [] if collection is None else list(collection)
        self._array.sort()

    def add_element(self, el):
        start_index = 0
        end_index = len(self._array) - 1
        while True:
            index = (end_index + start_index) // 2
            if self._array[index] == el:
                self._array.insert(index, el)
                return
            elif self._array[index] < el:
                if start_index == index:
                    self._array.insert(index, el)
                    return
                start_index = index
            elif start_index == end_index:
                self._array.insert(index, el)
                return
            else:
                end_index = index

    def find_element_index(self, el):
        start_index = 0
        end_index = len(self._array) - 1
        while True:
            index = (end_index + start_index) // 2
            if self._array[index] == el:
                return index
            elif self._array[index] < el:
                if start_index == index:
                    return -1
                start_index = index
            elif start_index == end_index:
                return -1
            else:
                end_index = index

    def find_element(self, el):
        return self.find_element_index(el) != -1

    def delete_element(self, el):
        index = self.find_element_index(el)
        if index != -1:
            self._array.pop(index)


if __name__ == '__main__':
    arr = [4, 8, 34, -6, 11, 7, 1, 0, -5, 2]
    searcher = BinarySearch(arr)
    print(searcher.find_element(7))
    print(searcher.find_element(-1))
    searcher.add_element(-1)
    searcher.add_element(-8)
    print(searcher.find_element(-1))
    searcher.delete_element(7)
    print(searcher.find_element(7))
