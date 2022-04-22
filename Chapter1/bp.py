__author__ = 'Robert W. Curtiss'
__project__ = 'blood pressure'
# https://www.youtube.com/watch?v=1aHNs1aEATg&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&index=7
# Author: Robert W. Curtiss
# bp.py was created on April 18 2022 @ 12:24 PM
# Project: FluentPython


import collections
import csv
from datetime import datetime
from collections import namedtuple
from pathlib import Path

DATE_FORMAT = '%m-%d-%Y'
file_path = Path.home()
LOG_DATE = 0

Reading = collections.namedtuple("Reading",'systolic diastolic time'.split())
DailyLog = collections.namedtuple('daily_entries', 'Date Morning Evening'.split())
daily_entries = [
    DailyLog('4/13/2022', Reading(130,67,'8AM'), Reading(161,80,'9PM')),
    DailyLog('4/14/2022', Reading(131,69,'9AM'), Reading(138,72,'9PM')),
    DailyLog('4/15/2022', Reading(128,71,'9AM'), Reading(152,76,'9PM')),
    DailyLog('4/16/2022', Reading(137,75,'9AM'), Reading(137,61,'9PM')),
    DailyLog('4/17/2022', Reading(135,67,'11AM'), Reading(144,72,'7PM')),
    DailyLog('4/18/2022', Reading(145,74,'10AM'), Reading(0,0,'7PM')),
                # Reading(131,69,'04/14/2022','AM'),
                # Reading(138,72,'04/14/2022','PM'),
                # Reading(128,71,'04/15/2022','AM'),
                # Reading(153,67,0,'04/15/2022','PM'),
                # Reading(137,75,'04/16/2022','AM'),
                # Reading(137,61,'04/16/2022','PM'),
                # Reading(135,67,'04/17/2022','AM'),
                # Reading(144,72,'04/17/2022','PM'),
                # Reading(145,74,'04/17/2022','AM'),
                ]

class Measure:
    def __init__(self):
        self.daily_entries = daily_entries

    def __getitem__(self, position):
        return self.daily_entries[position]

    def __len__(self):
        return len(self.daily_entries)

    def __contains__(self, item):
        for i in self.daily_entries:
            # print(i[0])
            if item == i[0]:
                return True
        return False

if __name__ == '__main__':
    # log = Measure()
    # for dat,(am_systolic,am_diastolic,am),(systolic) in log.daily_entries:
    #     print(f"{dat} | {am_systolic:3}/{am_diastolic:<3} {am:4} | {systolic[0]:3}/{systolic[1]:<3} {systolic[2]:4}")
    # print(len(log))
    # print( f"={'4/13/2022' in log}")

    with open(Path('bp.txt')) as file:
        reader = csv.reader(file,delimiter=',')
        rawResult = namedtuple("log", next(reader), rename=True)
        for row in reader:
            data = rawResult(*row)
            print(f'{data.DATE} | {data.AM_SYSTOLIC:3}/{data.AM_DIASTOLIC:<3} {data.AM_TIME:<4}',end='')
            print(f' | {data.PM_SYSTOLIC:>3}/{data.PM_DIASTOLIC:<3} {data.PM_TIME:<4}')


