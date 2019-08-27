#!/usr/bin/env python
# coding=utf-8

import os
import sys
import zipfile
import random

from io import open

random.seed(1111)

def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

if os.path.exists('train.txt'):
    print('Tokenized text8 already exists - skipping processing')
    sys.exit()

data = zipfile.ZipFile('smiles.zip').extractall()
data = open('smiles', 'r', encoding='utf-8').read().splitlines()

print('Length of smiles: {}'.format(len(data)))

num_train_molecules = 1800000*250

random.shuffle(data)

data = [d for d in data]

data = concatenate_list_data(data)

train_data = data[ : num_train_molecules]

#train_data = data[: -2 * num_test_molecules]
#valid_data = data[-2 * num_test_molecules: -num_test_molecules]
#test_data = data[-num_test_molecules:]

for fn, part in [('train.txt', train_data), ('valid.txt', train_data), ('test.txt', train_data)]:
    print('{} will have {} bytes'.format(fn, len(part)))
    print('- Tokenizing...')
    # Change space ' ' to underscore '_'
    part_str = ' '.join([c for c in part.strip()])
    print('- Writing...')
    f = open(fn, 'w').write(part_str)
    f = open(fn + '.raw', 'w', encoding='utf-8').write(part)
