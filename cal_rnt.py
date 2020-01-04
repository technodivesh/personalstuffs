#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""cal_rnt.py: Description of what this script does."""
"script to calculate unpaid rent with interest"

__author__      = "Divesh Chandolia"
__copyright__   = "Copyright 2019, Dchandolia"

__credits__ = [" Divesh Chandolia", ""] # includes people who reported bug fixes, made suggestions, etc. 
                                        #but did not actually write the code.
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Divesh Chandolia"
__email__ = "technodivesh@gmail.com"
__status__ = "Production"

# import os    # standard library
# import sys

# import requests  # 3rd party packages

# import mypackage.mymodule  # local source
# import mypackage.myothermodule 

import calendar
from datetime import datetime, timedelta,date
rent = 363

date_start = datetime(2018, 9, 1)
# date_end = datetime.today()
date_end = datetime(2019, 12, 31)

increment_dates = [] # [date(2019,1,1),date(2019,6,1)]

# print(type(increment_date),"---------")


def days_in_month(dt):
    return calendar.monthrange(dt.year, dt.month)[1]

def monthly_range(dt_start, dt_end):
    forward = dt_end >= dt_start
    finish = False
    dt = dt_start

    while not finish:
        yield dt.date()
        if forward:
            days = days_in_month(dt)
            dt = dt + timedelta(days=days)            
            finish = dt > dt_end
        else:
            _tmp_dt = dt.replace(day=1) - timedelta(days=1)
            dt = (_tmp_dt.replace(day=dt.day))
            finish = dt < dt_end


def total_rent():

    rent = 363
    total_rent = 0 
    total_month = 0
    total_intr = 0
    only_rent = 0
    for m in monthly_range(date_start, date_end):
        print(m)
        if m in increment_dates:
            # print("------------")
            rent = rent + (rent * 10 / 100)
            # print(rent)
            increment_dates.remove(m)
        else:
            pass
            # print(rent)
            
        only_rent += rent
        total_rent += rent
        # add int
        intr = (total_rent *1) / 100
        # print(intr)
        total_rent += intr
        total_month += 1
        total_intr += intr

    return total_rent,total_month,total_intr,only_rent

if __name__ == "__main__": 

    total_rent,total_month,total_intr,only_rent = total_rent()

    print('total_month--',total_month)
    # print('total_amt--',(rent * total_month))
    print('total_amt--',only_rent)
    print('total_intr--',total_intr)
    print('total_rent--',total_rent)
