import time
t = 0
T= 0
ask = raw_input("Start/Stop[Y/N]:")
while ask == "Y":
    time.sleep(0.1)
    t = t+1
    if t == 100:
        T= T+1
        t = 0
    print T,":",t
