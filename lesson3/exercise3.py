#!/usr/bin/python3
import time
start_time = time.time()
timeout = 5
while (time.time() < start_time + timeout):
    time.sleep(1)
    print(f"Amount of time elapsed: {time.time() - start_time} seconds ")
    continue
print(f"Exited the loop after {time.time() - start_time} seconds") 
