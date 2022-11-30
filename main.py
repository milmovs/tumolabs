import time

enter = (input("Insert time to countdown (h:m:s): ").split(":"))
h = int(enter[0])
m = int(enter[1])
s = int(enter[2])
def countdown(h,m,s):
  t = (h*3600) + (m*60) + (s)
  while t >= 0:
    print("%02d:%02d:%02d" % (t / 3600, (t / 60) % 60, t % 60))
    time.sleep(1)
    t -= 1
countdown(h,m,s)
