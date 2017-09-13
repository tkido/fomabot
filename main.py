#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import sys
import time

from config import HOME
from const import minute, hour, day, week, month, year
from twitter import tweet, selfdm

mode = sys.argv[1]
pace = sys.argv[2]

unixtime = int(time.time())
print unixtime

def per(interval, filename, func):
	path = os.path.join(HOME, 'text', filename)
	f = open(path)
	lines = f.readlines()
	f.close()

	size = len(lines)
	tick = unixtime // interval
	count = tick % size
	msg = lines[count].replace('\\n', '\n')
	"""
	print('size: %s' % size)
	print('tick: %s' % tick)
	print('count: %s' % count)
	print('msg: %s' % msg)
	"""
	func(msg)

func = tweet if sys.argv[1] == 'prod' else selfdm

if pace == "daily":
	pass
elif pace == "weekly":
	per(week, 'survival.txt', func)
	per(week, 'franklin.txt', func)
elif pace == "monthly":
	per(month, 'survival.txt', func)
