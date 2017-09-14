#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os.path
import sys
import time

from config import HOME
import const
from twitter import tweet, selfdm

mode = sys.argv[1]
pace = sys.argv[2]

unixtime = int(time.time())
#print unixtime
now = datetime.datetime.now()
#print now

def select(rule, interval, size):
	return rule(interval, size)

def message(rule, interval, filename, func):
	path = os.path.join(HOME, 'text', filename)
	f = open(path)
	lines = f.readlines()
	f.close()

	index = rule(interval, len(lines))
	msg = lines[index].replace('\\n', '\n')
	func(msg)

def fixed(interval, size):
	index = 0
	if interval == const.week:
		index = now.weekday()
	elif interval == const.month:
		index = now.month - 1
	return index

def rotation(interval, size):
	tick = unixtime // interval
	index = tick % size
	return index

func = tweet if sys.argv[1] == 'prod' else selfdm

if pace == "daily":
	message(fixed, const.month, 'honki.txt', selfdm)
	message(rotation, const.week, 'franklin.txt', selfdm)
	message(rotation, const.week, 'survival.txt', selfdm)
elif pace == "weekly":
	message(fixed, const.month, 'honki.txt', func)
	message(rotation, const.week, 'franklin.txt', func)
	message(rotation, const.week, 'survival.txt', func)
elif pace == "monthly":
	pass
