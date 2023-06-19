import time

print(time.time())

start = time.time()
print(time.asctime())  #po mestnomuvremeni

print(time.gmtime()[3])  # type -- <class 'time.struct_time'>

print(time.localtime())

time.sleep(5)
stop = time.time()
print(stop - start)
