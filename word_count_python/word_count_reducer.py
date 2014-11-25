#!/usr/bin/env python
import sys

if __name__ == '__main__':
    current_word = None
    key_count = 0
    for line in sys.stdin:
        key,value = line.strip().split("\t")
        try:
            record_count = int(value)
        except ValueError:
            continue #?!?
        if key != current_word:
            if current_word != None:
                print "{0}\t{1}".format(key, key_count)
            key_count = record_count
            current_word = key
        else:
            key_count += record_count

    if current_word == key:
        print "{0}\t{1}".format(key, key_count)
