#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.rstrip('\n')
    length = len(line)
    padding_length = max(0, 90 - length - 1)
    print(line + ' ' + ('*' * padding_length), end='')
