#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import hashlib
from collections import OrderedDict


def get_hash_sum(byte, mode):
    """На входе: посдедовательность байт, название алгоритма хэш-суммы
	На выходе: hex-представление хэш-суммы 
    """
    
    dct_modes = dict(
        sha1 = hashlib.sha1,
        md5 = hashlib.md5,
        sha512 = hashlib.sha512
        )

    h = dct_modes[mode]()
    h.update(byte)
    return h.hexdigest()


def glue_file(dir_name, hash_file, res_file):
    """
    функцию "склеивания" файла на основе упорядоченных хэш-сумм

    На входе: имя директории с файлами-кусочками, имя файла с хэш-суммами, имя выходного файла
    На выходе: размер полученного файла 

    """
    
    dir_name_in = os.path.join('files', dir_name)
    hash_file_path = os.path.join(dir_name_in, hash_file)
    res_file_path = os.path.join('files', res_file)
    
    list_files = [file_name for file_name in os.listdir(dir_name_in)
              if not file_name == hash_file]
    
    hash_summ = {}
    with open(hash_file_path, 'r') as f:
        hash_summ = OrderedDict(map(lambda line: (line.replace('\n', ''), ''), f))
    
    for file in list_files:
        with open(os.path.join(dir_name_in, file), 'rb') as f:
            data = f.read()
        h = get_hash_sum(data, 'md5')
        hash_summ[h] = file
    
    with open(res_file_path, 'wb') as f_result:
        for hash, file in hash_summ.items():
            with open(os.path.join(dir_name_in, file), 'rb') as f:
                data = f.read()
            f_result.write(data)

    return os.path.getsize(res_file_path)    
  

def main():   
    """
    main func 
    """

    print(glue_file('file2','parts.md5', 'resss3'))


if __name__ == '__main__':
    main()

 


