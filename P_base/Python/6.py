#!/usr/bin/python3
# -*- codring: -*-

import sys

l = [1, 2, 3, 4, 5]
a = iter(l)

while True:
	try:
		print(next(a))
	except StopIteration:
		sys.exit()