# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 22:13:26 2018

@author: jingtan
"""

'''
download youtube

Tested with Python 3
'''

import subprocess
from time import time

filename = 'list.txt'  # pylint: disable=invalid-name

then = time()  # pylint: disable=invalid-name

with open(filename, 'r') as fhandle:
    for line in fhandle.readlines():
        print(line)
        if line.strip():
            print('Downloading %s...' % line)
            p = subprocess.Popen(
                ['youtube-dl', '-f', '160', line],
                shell=True,
                # stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            p.wait()
            out, err = p.communicate()
            # print(out, err)
            if err:
                print('\n\t>>>Failed, err: %s\n' % err)
print('Tot time: %.2f s' % (time() - then))





















































































