#! /usr/bin/python3
import sched
import time
import threading

scheduler = sched.scheduler(time.time, time.sleep)

def print_event(name):
    global scheduler
    print('Event:', time.time(),"(",time.strftime("%d %b %y %H %M %S",time.localtime(time.time())),")", name)


scheduler.enterabs(time.mktime(time.strptime("24 Jan 17 22 56 03", "%d %b %y %H %M %S")),1, print_event, ('First',))
scheduler.enterabs(time.mktime(time.strptime("24 Jan 17 22 56 09", "%d %b %y %H %M %S")),1, print_event, ('Second',))
scheduler.enterabs(time.mktime(time.strptime("24 Jan 17 22 56 42", "%d %b %y %H %M %S")),1, print_event, ('Third',))
t=threading.Thread(target=scheduler.run)
t.start()

while 1:
    global scheduler
    print(len(scheduler.queue), " Events left in the queue")
    if len(scheduler.queue) == 0: break
    time.sleep(15)

#for x in range (50):
#    global scheduler
#    time.sleep(.1)
#t.join()
#print (time.strptime("24 Jan 17 22 21", "%d %b %y %H %M") )
