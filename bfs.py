#!/bin/python
from queue import Queue
from facebook import adjacency_list,name
from sys import argv,exit
q=Queue()
beginning=name.index(argv[2])
q.put(beginning)
parent=list(range(len(name)))
parent[beginning]=-1
while not q.empty():
    node=q.get()
    if name[node]==argv[1]:
        n=node
        while parent[n]!=-1:
            print(f"{name[n]}->",end='')
            n=parent[n]
        print(argv[2])
        exit(0)
    for i,n in enumerate(name):
        if (f'{name[node]}-{n}' in adjacency_list or f'{n}-{name[node]}' in adjacency_list) and parent[i]==i:
            parent[i]=node
            q.put(i)
print(f"No path between {argv[1]} and {argv[2]}.")
