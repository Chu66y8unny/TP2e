#!/usr/bin/env python3.7
from datetime import timedelta
from datetime import time
from datetime import date
from datetime import datetime

if __name__ == '__main__':
    leave = datetime.combine(date.today(), time(hour=6, minute=52))
    easy = timedelta(minutes=8, seconds=15)
    tempo = timedelta(minutes=7, seconds=12)
    get_home = leave + easy + 3 * tempo + easy
    print(get_home.time())
