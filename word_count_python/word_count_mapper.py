#!/usr/bin/env python
import sys

'''
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.5.0-mr1-cdh5.2.0.jar \
-input pp/word_count \
-output output/word_count_python \
-mapper bin/word_count_mapper.py \
-reducer bin/word_count_reducer.py \
-file bin
'''

if __name__ == '__main__':
    for line in sys.stdin:
        words = line.strip().split()
        for word in words:
            print "%s\t%d" % (word, 1)

