"""Reference 4-sunflower oracle: exact six set intersections; no search heuristics."""
from itertools import combinations


def normalize(edges):
    out=[]
    for edge in edges:
        try:
            t=tuple(sorted(edge))
        except (TypeError, ValueError) as exc:
            raise ValueError('invalid triple') from exc
        if len(t)!=3 or len(set(t))!=3 or not all(isinstance(x,int) and not isinstance(x,bool) for x in t):
            raise ValueError('each input must be three distinct integer vertices')
        out.append(t)
    if len(set(out))!=len(out):
        raise ValueError('duplicate triple')
    return tuple(sorted(out))


def first_sunflower(edges):
    es=normalize(edges)
    for quartet in combinations(es,4):
        ss=[frozenset(t) for t in quartet]
        six=[ss[i]&ss[j] for i,j in combinations(range(4),2)]
        if all(x==six[0] for x in six[1:]):
            return {'edges':[list(t) for t in quartet], 'kernel':sorted(six[0])}
    return None


def check(edges):
    e=normalize(edges)
    witness=first_sunflower(e)
    return {'valid':witness is None,'edges':len(e),'quadruples':len(list(combinations(e,4))), 'sunflower':witness}
