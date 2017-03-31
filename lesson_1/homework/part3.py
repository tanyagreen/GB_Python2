#! /usr/bin/env python
# -*- coding: utf-8 -*-


path = 'files/file1/parts.md5'
line_new = []
with open(path, 'r', encoding='UTF-8') as f:
    for i, line in enumerate(f):
       print(line)
