#!/usr/bin/env python3
"""P001B-S003: pre-registered COMPLETE cyclic Z12 orbit enumeration only."""
import itertools as I
import hashlib
import json

def normalize(f):
    f=tuple(sorted(tuple(sorted(x)) for x in f))
    if len(set(f))!=len(f) or any(len(x)!=3 or len(set(x))!=3 for x in f):
        raise ValueError("non-simple triple family")
    return f

def first_quartet(f):
    # Explicit equality of all SIX intersection SETS, including empty.
    for q in I.combinations(normalize(f),4):
        s=list(map(frozenset,q))
        meets=[s[i]&s[j] for i,j in I.combinations(range(4),2)]
        if len(set(meets))==1:return q,tuple(sorted(meets[0]))
    return None

def matching4(f):
    ee=list(map(frozenset,f))
    def rec(i,used,k):
        if k==4:return True
        if len(ee)-i<4-k:return False
        for j in range(i,len(ee)):
            if not (ee[j]&used) and rec(j+1,used|ee[j],k+1):return True
        return False
    return rec(0,frozenset(),0)

def secondary_free(f):
    f=normalize(f)
    ss=list(map(frozenset,f))
    vs=sorted(set().union(*ss)) if ss else []
    for x,y in I.combinations(vs,2):
        if sum({x,y}<=e for e in ss)>=4:return False
    for x in vs:
        if matching4([e-{x} for e in ss if x in e]):return False
    return not matching4(ss)

def source39():
    g=[tuple(range(3*i,3*i+3)) for i in range(3)]
    f=list(g)+[(9,*pair) for v in g for pair in I.combinations(v,2)]
    for (i,j),s in zip(I.combinations(range(3),2),(10,11,12)):
        f.extend((s,x,y) for x in g[i] for y in g[j])
    return normalize(f)

def controls():
    cases=(
      (((0,1,2),(3,4,5),(6,7,8),(9,10,11)),False),
      (((0,1,2),(0,3,4),(0,5,6),(0,7,8)),False),
      (((0,1,2),(0,1,3),(0,1,4),(0,1,5)),False),
      (((0,1,2),(0,1,3),(0,4,5),(6,7,8)),True),
    )
    for f,valid in cases:
        assert (first_quartet(f) is None)==valid
        assert secondary_free(f)==valid
    for check in (first_quartet,secondary_free):
        try:check(((0,1,2),(2,1,0)))
        except ValueError:pass
        else:raise AssertionError("duplicate accepted")
    f=source39()
    assert len(f)==39 and first_quartet(f) is None and secondary_free(f)

def orbits():
    triples=I.combinations(range(12),3)
    O={frozenset(tuple(sorted((x+k)%12 for x in t)) for k in range(12)) for t in triples}
    groups=sorted((tuple(sorted(o)) for o in O),key=lambda o:(len(o),o))
    assert len(groups)==19 and sum(map(len,groups))==220
    short=[o for o in groups if len(o)==4]
    full=[o for o in groups if len(o)==12]
    assert len(short)==1 and len(full)==18 and len(set().union(*map(set,short[0])))==12
    assert first_quartet(short[0]) is not None and not secondary_free(short[0])
    return full

def classify():
    controls()
    full=orbits()
    result={}
    survivors={}
    for k in range(4):
        good=[]
        for ids in I.combinations(range(18),k):
            f=normalize(e for i in ids for e in full[i])
            exact=first_quartet(f) is None
            secondary=secondary_free(f)
            assert exact==secondary,(ids,exact,secondary)
            if exact:good.append(ids)
        result[str(k)]={"tested":len(list(I.combinations(range(18),k))),"free":len(good)}
        survivors[str(k)]=good
    assert sum(v["tested"] for v in result.values())==988
    assert [(result[str(i)]["free"]) for i in range(4)]==[1,13,16,0]
    ids=survivors["2"][0]
    f=normalize(e for i in ids for e in full[i])
    witness="".join(",".join(map(str,t))+"\n" for t in f)
    return {"counts":result,"survivors":survivors,"orbit_generators":[list(o[0]) for o in full],
        "representative_indices":ids, "representative_triples":f,
        "representative_sha256":hashlib.sha256(witness.encode()).hexdigest()}

if __name__=="__main__":
    print(json.dumps(classify(),indent=2))
