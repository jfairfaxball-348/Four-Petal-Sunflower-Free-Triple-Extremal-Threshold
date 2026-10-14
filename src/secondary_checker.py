"""Independent oracle using matching certificates in link graphs and whole hypergraph.
No unordered four-tuple intersection comparison or shared generator predicate.
"""
from itertools import combinations

def check(edges):
    ee=[frozenset(e) for e in edges]
    if any(len(e)!=3 for e in ee) or len(ee)!=len(set(ee)):
        raise ValueError('invalid simple triple family')
    vertices=set().union(*ee) if ee else set()
    # kernel 2
    for x,y in combinations(sorted(vertices),2):
        if sum({x,y}<=e for e in ee)>=4:
            return False, 'pair-kernel'
    # kernel 1
    for x in vertices:
        edges_x=[e-{x} for e in ee if x in e]
        if has_matching_of_four(edges_x):
            return False,'point-kernel'
    # kernel 0
    if has_matching_of_four(ee):
        return False,'empty-kernel'
    return True,None

def has_matching_of_four(edges):
    edges=list(edges)
    def rec(start,used,k):
        if k==4:
            return True
        if len(edges)-start < 4-k:
            return False
        for i in range(start,len(edges)):
            if not (edges[i]&used) and rec(i+1,used|edges[i],k+1):
                return True
        return False
    return rec(0,frozenset(),0)
