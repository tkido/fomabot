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
week = hour * 7
month = day * 30.436875
year = day * 365.2425

msg = """3. 希望：
船が沈み始めたら祈るな、飛び込め。
小さな損失は人生の現実として甘んじて受けよ。
大きな利益を待つ間には、何度かそういう経験をすると考えろ。"""

print(msg)
#tweet(msg)
selfdm(msg)
