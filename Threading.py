from threading import Thread

def for_loops() -> None:
    for j in range (1,1000):
        for k in range (1,100000):
            pass
    print ("Finished both for loops")

t = Thread (target = for_loops, args = ())
t.start()
#for_loops()
