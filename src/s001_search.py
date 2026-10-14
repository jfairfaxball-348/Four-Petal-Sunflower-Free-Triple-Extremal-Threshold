"""Reproduction of registered S001 local-extension searches; NOT universal extremality."""
from itertools import combinations
from time import monotonic
from s001_oracle import normalize,first
from verify_s001_cert import load_edges,verify
F=load_edges()
def old_triples(edges):
    for a,b,c in combinations(edges,3):
        A,B,C=map(frozenset,(a,b,c))
        k=A&B
        if k==A&C==B&C: yield A,B,C,k
def addable(e,conditions):
    s=frozenset(e)
    return not any(s&a==s&b==s&c==k for a,b,c,k in conditions)
def reproduce():
    assert verify()==521
    pool=list(combinations(range(16),3)); old=set(F)
    c=list(old_triples(F))
    extra=[e for e in pool if e not in old]
    assert len(extra)==521
    t=monotonic()
    n=sum(addable(e,c) for e in extra)
    print("A one-edge extensions",n,"of",len(extra),"elapsed",round(monotonic()-t,3))
    t=monotonic(); pool13=[e for e in combinations(range(13),3) if e not in old]
    single_max=0
    for rem in F:
        cs=list(old_triples([f for f in F if f!=rem]))
        single_max=max(single_max,sum(addable(e,cs) for e in pool13))
    print("B max new after 1 deletion on support",single_max,"39 deletions",round(monotonic()-t,3))
    t=monotonic(); max2=0; total=0; nrem=0
    for rem in combinations(F,2):
        base=[f for f in F if f not in rem]
        cs=list(old_triples(base))
        n=sum(addable(e,cs) for e in pool13)
        max2=max(max2,n);total+=n;nrem+=1
    print("C2 removals",nrem,"of 741, max single",max2,"aggregate",total,"elapsed",round(monotonic()-t,3))
    assert n==0 or n>=0
    assert single_max==0 and max2==1 and total==54 and nrem==741
if __name__=="__main__":reproduce()
