highest=0
adjacency_list=set()
with open('facebook_combined.txt','r') as datafile:
    for line in datafile:
        adjacency_list.add(line[:-1].replace(' ','-'))
        highest=max(highest,*[int(i) for i in line.split(' ')])
name=tuple(str(i) for i in range(highest))
