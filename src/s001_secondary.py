"""Independent three-kernel matching oracle; does not use quartet-intersection test."""
from itertools import combinations
def matching4(edges):
    E=list(map(frozenset,edges))
    def recurse(i,used,n):
        if n==4:return True
        if len(E)-i<4-n:return False
        for j in range(i,len(E)):
            if not E[j]&used and recurse(j+1,used|E[j],n+1):return True
        return False
    return recurse(0,frozenset(),0)
def free(edges):
    es=list(map(frozenset,edges))
    if len(es)!=len(set(es)) or any(len(e)!=3 for e in es):raise ValueError("not simple triples")
    verts=sorted(set().union(*es)) if es else []
    for a,b in combinations(verts,2):
        if sum({a,b}<=e for e in es)>=4:return False
    for a in verts:
        if matching4([e-{a} for e in es if a in e]):return False
    return not matching4(es)
