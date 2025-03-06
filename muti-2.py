import multiprocessing
import time

start = time.perf_counter()
start2 = round(start)
def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done sleeping...')

#start = time.perf_counter()
do_something()
finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} second(s)')

p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)
finish = time.perf_counter()
#print(f'Finished in {round(finish - start, 2)} second(s)')
print('-----------end--------')
print(start)
print(finish)
print('-----------finished--------')
print(start2)

finish2 = round(finish)
print(f'finished in {(finish - start2)} second(s)')
print(f'finished in around {(finish2 - start2)} second(s)')