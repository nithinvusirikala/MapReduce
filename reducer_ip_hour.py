#!/opt/homebrew/bin/python3
"""reducer_ip_hour.py"""

from operator import itemgetter
import sys

dict_ip_hour_count = {}

for line in sys.stdin:
    line = line.strip()
    hour, ip, count = line.split('\t')
    try:
        count = int(count)
        dict_ip_hour_count[hour] = dict_ip_hour_count.get(hour, {})
        dict_ip_hour_count[hour][ip] = dict_ip_hour_count[hour].get(ip, 0) + count
    except ValueError:
        pass

sorted_dict_ip_hour_count = {}

for hour in dict_ip_hour_count.keys():
    sorted_dict_ip_hour_count[hour] = sorted(dict_ip_hour_count[hour].items(), key=itemgetter(1), reverse=True)

for hour in sorted_dict_ip_hour_count.keys():
    stop = 0
    for ip, count in sorted_dict_ip_hour_count[hour]:
        print('%s\t%s\t%s' % (hour, ip, count))
        stop += 1
        if stop == 3:
            break
