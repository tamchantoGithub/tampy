from multiprocessing import *
#from multiprocessing.spawn import spawn_main
import time
from os import getpid, getppid


start = time.perf_counter()
def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done sleeping...')

do_something()
finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')
time.sleep(3)

def f1(name):
    #print("Hello {} pid={} ppid={}   sleep 3 sec".format(name, getpid(), getppid()))
    time.sleep(1)
    print("Good morning", name)

def f2(*args, **kwargs):
    print("args=", args, " kwargs=",kwargs)
    print("Hello", kwargs["name"], " pid", getpid(), getppid())
    print("Sleeping... {}s".format(kwargs["len"]))
    time.sleep(kwargs["len"])
    print("Good morning", kwargs["name"])

#1 = Process(target=f1, args=("Bob",))
p2 = Process(target=f2, args=("Bob",), kwargs={"name": "Alice", "len":1})
do_something()
#p2.start()
#p2.join()
#time.sleep(1)
print("Process joined.")
print(p2)
# set args append list object
args="Bob"
kwargs={"name": "Alice", "len":1}
#f2(p2)
print("Hello", kwargs["name"], " pid", getpid(), getppid())

# add list
animals = ['cats','dogs', 'horses']
print(kwargs["name"]," likes ...",animals)
print(animals)

print("Going to ..change like...")
animals.append("Going to ..change like..."'hodges')
print(animals)
finish2 = time.perf_counter()
print(f'Finished in {round(finish2-start, 2)} second(s)')
