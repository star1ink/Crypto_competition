import math
import numpy
import hashlib
import random


def gen_para(file_len, b_num, p):
    length = math.ceil(-(b_num * math.log(p)) / ((math.log(2)) ** 2))
    h_num = math.ceil((length / b_num) * math.log(2))
    print(length,h_num)
    return length, h_num


def add_to_bf(val, vec, para):
    for i in range(para[1]):
        loc = gen_hash(val, para[0], i+1)
        vec[loc] += 1
    return 1


def gen_hash(value, bits, k):
    m = hashlib.md5()
    m.update(str(value).encode(encoding='UTF-8'))
    hash_str = m.hexdigest()
    random.seed(int(hash_str,base=16))
    for i in range(k):
        random.randint(0,bits-1)
    return random.randint(0,bits-1)


def init_bf(size):
    return numpy.zeros(size)
