#!/opt/homebrew/bin/python3
"""mapper_ip.py"""

import sys
import re

pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?"\w+ (?P<subdir>.*?) ')
for line in sys.stdin:
    match = pat.search(line)
    if match:
        print('%s\t%s' % (match.group('ip'), 1))