import time

local_time = time.strftime("%H:%M", time.localtime())
utc_time = time.strftime("%H:%M", time.gmtime())
action = "to have a sleep"

print(f"It's {local_time}. Time {action}.")
print(f"It's {utc_time}. Time {action}.")
print("=====")
print(time.gmtime(0))  # Epoch start time
print("=====")
print(time.asctime())
print(time.ctime(time.time()))
print("=====")
print("Let's calculate time difference for performance measurement:")
start = time.perf_counter()
time.sleep(1)
end = time.perf_counter()
total_time = end - start
print(total_time)
print("=====")
print(total_time.total_seconds())
