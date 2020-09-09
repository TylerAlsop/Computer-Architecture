#!/usr/bin/env python3

# Run this file to test your code.

"""Main."""

import sys
from cpu import *

cpu = CPU()

cpu.load(sys.argv[1])
cpu.run()