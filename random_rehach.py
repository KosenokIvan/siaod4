import random


class RandomRehash:
    def __init__(self):
        self._hash_table = [None for _ in range(256)]

    @staticmethod
    def hash_function(num):
        return sum(map(int, str(abs(num)))) % 256

    def add_num(self, num):
        hash_value = self.hash_function(num)
        random.seed(213)
        while self._hash_table[hash_value] is not None:
            hash_value = random.randrange(256)
        self._hash_table[hash_value] = num


if __name__ == '__main__':
    nums = [11, 22, 12, 201, 43, 67, 34, 55, 4060]
    table = RandomRehash()
    for n in nums:
        table.add_num(n)
