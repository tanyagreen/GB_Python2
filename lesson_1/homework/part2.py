#! /usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib

def get_hash(string, mode):
    """На входе: строка, название алгоритма хэш-суммы
	На выходе: hex-представление хэш-суммы для строки
    """
    s = string.encode('utf8')

    if mode == 'md5':
        h = hashlib.md5()
    elif mode == 'sha1':
        h = hashlib.sha1()
    elif mode == 'sha512':
        h = hashlib.sha512()

    h.update(s)
    return h.hexdigest()


path = 'need_hashes.csv'
line_new = []
with open(path, 'r', encoding='UTF-8') as f:
    for i, line in enumerate(f):
        l = line.split(';')
        hash_sum = get_hash(l[0], l[1])
        if i > 0:
            line_new.insert(i,'{};{};{}{}'.format(l[0], l[1], hash_sum, '\n'))
        else:
            line_new.insert(i,line)

with open(path, 'w', encoding='UTF-8') as f:
    f.writelines(line_new)
