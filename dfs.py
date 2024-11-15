#!/bin/python
from facebook import adjacency_list,name
from sys import argv,exit
beginning=name.index(argv[2])
parent=list(range(len(name)))
parent[beginning]=-1
def dfs(current:int):
    if name[current]==argv[1]:
        n:int=current
        while parent[n]!=-1:
            print(f"{name[n]}->",end='')
            n=parent[n]
        print(argv[2])
        return True
    ret:bool=False
    for i,n in enumerate(name):
        if (f'{name[current]}-{n}' in adjacency_list or f'{n}-{name[current]}' in adjacency_list) and parent[i]==i:
            parent[i]=current
            if(ret:=ret or dfs(i)):
                break
    return ret
if not dfs(beginning):
    print(f"No path between {argv[1]} and {argv[2]}.")
