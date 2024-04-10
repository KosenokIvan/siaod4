import time
from random import sample, randrange
from simple_rehash import SimpleRehash
from random_rehach import RandomRehash
from chaine_hash import ChaineHash


for length in (100, 400, 2000, 4000):
    nums = sample(range(length * 2), length)
    print(f"Length: {length}")
    for hasher_type in (SimpleRehash, RandomRehash, ChaineHash):
        hasher = hasher_type()
        start_time = time.time()
        for num in nums:
            hasher.add_num(num)
        print(hasher_type.NAME + " --- {0} ms ---".format(round((time.time() - start_time) * 1000)))
        print("="*30 + "\n")
