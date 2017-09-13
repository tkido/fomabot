#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import time
from config import HOME
from twitter import tweet
from twitter import selfdm

unixtime = int(time.time())
print unixtime

minute = 60
hour = minute * 60
day = hour * 24
week = day * 7
month = day * 30.436875
year = day * 365.2425

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

per(week, 'survival.txt', tweet)
per(week, 'franklin.txt', tweet)
