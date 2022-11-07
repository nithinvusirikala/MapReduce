#!/opt/homebrew/bin/python3
"""reducer_ip_hour.py"""

from operator import itemgetter
import sys
import argparse

# Instantiate the parser
parser = argparse.ArgumentParser(description='Hour to find')
parser.add_argument('--hrange', '-hr',type=str,
                    help='Range of hours to get top 3 IPs for')

args = parser.parse_args()
hour_range = args.hrange

if hour_range is not None:
    hour_start, hour_end = hour_range.split('-')
    hours = [(f'[{val:02}:00]') for val in range(int(hour_start), int(hour_end))]
    dict_ip_count = {}
    for line in sys.stdin:
        line = line.strip()
        hour, ip, count = line.split('\t')
        if hour in hours:
            try:
                count = int(count)
                dict_ip_count[ip] = dict_ip_count.get(ip, 0) + count
            except ValueError:
                pass

    stop = 0
    sorted_dict_ip_count = sorted(dict_ip_count.items(), key=itemgetter(1), reverse=True)
    for ip, count in sorted_dict_ip_count:
        print('%s\t%s' % (ip, count))
        stop += 1
        if stop == 3:
            break

else:
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

