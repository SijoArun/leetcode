from datetime import *
import time

startime=time.perf_counter()
ldates=[]

d1=date(2016,2,3)
d2=date(2016,1,3)
d3=date(2018,2,3)
d4=date(2017,2,3)
d5=date(2016,2,1)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)
ldates.append(d4)
ldates.append(d5)
ldates.sort()
#time.sleep(3)

for d in ldates:
    print(d)

endtime = time.perf_counter()
print(endtime-startime)

