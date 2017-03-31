#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import hashlib


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


def glue_file(dir_name, hash_file_name, res_file_name):
    """
    функцию "склеивания" файла на основе упорядоченных хэш-сумм

    На входе: имя директории с файлами-кусочками, имя файла с хэш-суммами, имя выходного файла
    На выходе: размер полученного файла 
    """

    DIR = os.path.join('files', dir_name)
    
    with open(os.path.join(DIR, hash_file_name), 'r', encoding='UTF-8') as f:
        lst_hashes = [line.replace('\n', '') for line in f]

    list_files = [file_name for file_name in os.listdir(DIR)
              if not file_name == hash_file_name]
    res_lst = []
    
    for file in list_files:
        with open(os.path.join(DIR, file), 'rb') as f:
            read_data = f.read()
            h_summ = get_hash_sum(read_data, 'md5')
   
        for i, item in enumerate(lst_hashes):
            if h_summ == item:
                print('{} + {}'.format(h_summ, i))
                res_lst.insert(i, file)

    with open(os.path.join('files', res_file_name), 'wb') as f_res:
        for file in res_lst:
            with open(os.path.join(DIR, file), 'rb') as f:
                read_data = f.read()
            f_res.write(read_data)
            
    return os.path.getsize(os.path.join('files', res_file_name))


def main():   
    """
    main func 
    """

    print(glue_file('file2','parts.md5', 'resss2'))


if __name__ == '__main__':
    main()

 


