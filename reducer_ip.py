#!/opt/homebrew/bin/python3
"""reducer_ip.py"""

from operator import itemgetter
import sys


dict_ip_count={}

for line in sys.stdin:
    line = line.strip()
    ip, num = line.split('\t')
    try:
        num = int(num)
        dict_ip_count[ip] = dict_ip_count.get(ip, 0) + num
    except ValueError:
        pass

stop=0
sorted_dict_ip_count = sorted(dict_ip_count.items(), key=itemgetter(1),reverse=True)
for ip, count in sorted_dict_ip_count:
        print('%s\t%s' % (ip, count))
        stop += 1
        if stop == 3:
            break

#stop = 0
#sorted_dict_ip_count = sorted(dict_ip_count, key=dict_ip_count.get, reverse=True)
#for ip in sorted_dict_ip_count:
#    print('%s\t%s'% (ip,sorted_dict_ip_count[ip]))
#    stop += 1
#    if stop == 3:
#        break