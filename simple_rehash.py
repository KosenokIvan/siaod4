class SimpleRehash:

    NAME = "Простое рехеширование"
    MOD = 8192

    def __init__(self):
        self._hash_table = [None for _ in range(self.MOD)]

    @staticmethod
    def hash_function(num):
        return sum(map(int, str(abs(num)))) % SimpleRehash.MOD

    def add_num(self, num):
        hash_value = self.hash_function(num)
        while self._hash_table[hash_value] is not None:
            hash_value += 1
            hash_value %= self.MOD
        self._hash_table[hash_value] = num


if __name__ == '__main__':
    nums = [11, 22, 12, 201, 43, 67, 34, 55, 4060]
    table = SimpleRehash()
    for n in nums:
        table.add_num(n)
