"""Axante et al. arXiv:2609.06175v1 Theorem 5.1, exact labelled expansion.
This is a reproduction of prior art, not an original construction.
"""
from itertools import combinations, product
from sunflower_oracle import normalize

def build():
    groups=[tuple(range(3*i,3*i+3)) for i in range(3)]
    g=[tuple(v) for v in groups]
    p=[(9,*pair) for v in groups for pair in combinations(v,2)]
    q=[(10+i+j-1,x,y) for i,j in combinations(range(3),2) for x,y in product(groups[i],groups[j])]
    # special labels: (0,1)->10, (0,2)->11, (1,2)->12
    return normalize(g+p+q)

if __name__=='__main__':
    from sunflower_oracle import check
    from secondary_checker import check as secondary
    es=build()
    assert len(es)==39
    a=check(es); b=secondary(es)
    print('primary:',a,'secondary:',b)
    assert a['valid'] and b[0]
