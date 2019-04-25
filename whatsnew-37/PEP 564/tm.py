"""
clock_gettime_ns(): Returns the time of a specified clock
clock_settime_ns(): Sets the time of a specified clock
monotonic_ns(): Returns the time of a relative clock that cannot go backwards (for instance due to daylight savings)
perf_counter_ns(): Returns the value of a performance counter—a clock specifically designed to measure short intervals
process_time_ns(): Returns the sum of the system and user CPU time of the current process (not including sleep time)
time_ns(): Returns the number of nanoseconds since January 1st 1970


>>> 0.1 + 0.1 + 0.1
0.30000000000000004

>>> 0.1 + 0.1 + 0.1 == 0.3
False
"""

import time

print(time.time(), f"type: {type(time.time())}")
print(time.time_ns(), f"type: {type(time.time_ns())}")
