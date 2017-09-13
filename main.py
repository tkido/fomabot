#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
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
	f = open('text/%s.txt' % filename)
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

per(day, 'survival', selfdm)
per(day, 'franklin', selfdm)
