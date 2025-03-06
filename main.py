from multiprocessing import Process
from time import sleep
from os import getpid, getppid

def f1(name):
    print("Hello {} pid={} ppid={}   sleep 3 sec".format(name, getpid(), getppid()))
    sleep(5)
    print("Good morning", name)

def f2(*args, **kwargs):
    print("args=", args, " kwargs=",kwargs)
    print("Hello", kwargs["name"], " pid", getpid(), getppid())
    print("Sleeping... {}s".format(kwargs["tlen"]))
    sleep(kwargs["tlen"])
    print("Good morning", kwargs["name"])


if __name__ == "__main__":
    # make sub job thread
    print(__name__, " pid", getpid())
    p1 = Process(target=f1, args=("Bob",))
    p2 = Process(target=f2, args=("Bob",), kwargs={"name": "Alice", "tlen":10})

    # start sub process
    p1.start()
    p2.start()
    print("Process started.")

    # end until subprosess 
    p1.join()
    p2.join()
    print("Process joined.")