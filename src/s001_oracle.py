"""Exact semantic reference: every unordered quartet and six SET intersections."""
from itertools import combinations
def normalize(edges):
    out=[]
    for e in edges:
        try: t=tuple(sorted(e))
        except (TypeError,ValueError) as ex: raise ValueError("invalid triple") from ex
        if len(t)!=3 or len(set(t))!=3 or not all(type(x) is int for x in t):
            raise ValueError("non-simple triple")
        out.append(t)
    if len(set(out))!=len(out): raise ValueError("duplicate")
    return tuple(sorted(out))
def first(edges):
    es=normalize(edges)
    for w in combinations(es,4):
        s=list(map(frozenset,w))
        meets=[s[i]&s[j] for i,j in combinations(range(4),2)]
        if all(x==meets[0] for x in meets): return tuple(w),tuple(sorted(meets[0]))
    return None
