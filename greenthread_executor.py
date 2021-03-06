#!/usr/bin/env python
# -*- coding: utf-8 -*-

# NOTE: enable printing timestamp for additional data

import datetime

import eventlet
import futurist


def delayed_func():
    print("started")
    eventlet.sleep(3)
    print("done")


print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
e = futurist.GreenThreadPoolExecutor()
print("before submit")
fut = e.submit(delayed_func)
eventlet.sleep(1)
print("1 seconds after submit")
eventlet.sleep(1)
print("2 seconds after submit")
e.shutdown()
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
