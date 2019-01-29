#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

import futurist


def delayed_func():
    time.sleep(0.1)
    return "hello"


e = futurist.ThreadPoolExecutor()
fut = e.submit(delayed_func)
print(fut.result())
e.shutdown()
