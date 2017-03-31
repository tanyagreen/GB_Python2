import hashlib
import os


__author__ = "Tatiana Karavaeva"

def get_hash_sum(string, mode):
    """На входе: строка, название алгоритма хэш-суммы
	На выходе: hex-представление хэш-суммы 
    """
    
    dct_modes = dict(
        sha1 = hashlib.sha1,
        md5 = hashlib.md5,
        sha512 = hashlib.sha512
        )

    s = string.encode('utf8')

    h = dct_modes[mode]()
    h.update(s)
    return h.hexdigest()

def main():
    """
    Читает need_hashes.csv, добывает хешсуммы для каждой строки в файле
    дописывает полученную хешсумму обратно в файл 
    """
    
    path = 'need_hashes.csv'
    line_new = []
    with open(path, 'r', encoding='UTF-8') as f:
        for i, line in enumerate(f):
            l = line.split(';')
            hash_sum = get_hash_sum(l[0], l[1])
            if i > 0:
                 line_new.insert(i,'{};{};{}{}'.format(l[0], l[1], hash_sum, '\n'))
            else:
                 line_new.insert(i,line)

    with open(path, 'w', encoding='UTF-8') as f:
        f.writelines(line_new)


if __name__ == '__main__':
    main()




