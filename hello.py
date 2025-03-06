prinnt("hello py!!")

names = ['mike', 'pochi', 'blacky', 'whity']
ranks = [5, 2, 4, 1, 3]

for name,rank in zip(names, ranks):
    print(f'{name}: {rank}')