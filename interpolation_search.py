from typing import Iterable, Optional


class InterpolationSearcher:
    def __init__(self, collection: Optional[Iterable] = None):
        self._array = [] if collection is None else list(collection)
        self._array.sort()

    def find_element_index(self, el):
        min_index = 0
        max_index = len(self._array) - 1
        while self._array[min_index] < el < self._array[max_index]:
            if self._array[min_index] == self._array[max_index]:
                break
            mid_index = min_index + (((el - self._array[min_index]) * (max_index - min_index))
                                     // (self._array[max_index] - self._array[min_index]))
            if self._array[mid_index] == el:
                return mid_index
            elif self._array[mid_index] < el:
                min_index = mid_index + 1
            else:
                max_index = mid_index - 1
        if self._array[min_index] == el:
            return min_index
        if self._array[max_index] == el:
            return max_index
        return -1

    def find_element(self, el):
        return self.find_element_index(el) != -1

    def add_element(self, el):
        min_index = 0
        max_index = len(self._array) - 1
        while self._array[min_index] < el < self._array[max_index]:
            if self._array[min_index] == self._array[max_index]:
                break
            mid_index = min_index + (((el - self._array[min_index]) * (max_index - min_index))
                                     // (self._array[max_index] - self._array[min_index]))
            if self._array[mid_index] == el:
                self._array.insert(mid_index, el)
                return
            elif self._array[mid_index] < el:
                min_index += mid_index + 1
            else:
                max_index = mid_index - 1
        if self._array[min_index] == el:
            self._array.insert(min_index, el)
        elif self._array[max_index] == el:
            self._array.insert(max_index, el)
        else:
            self._array.insert(min(min_index, max_index), el)

    def delete_element(self, el):
        index = self.find_element_index(el)
        if index != -1:
            self._array.pop(index)


if __name__ == '__main__':
    arr = [4, 8, 34, -6, 11, 7, 1, 0, -5, 2]
    searcher = InterpolationSearcher(arr)
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
