"""Independent labelled expansion of Axante et al. Theorem 5.1."""
from itertools import combinations,product
from s001_oracle import normalize
def build():
    v=[tuple(range(3*i,3*i+3)) for i in range(3)]
    groups=list(v)
    stars=[(9,*p) for z in v for p in combinations(z,2)]
    bridges=[(10+i+j-1,a,b) for i,j in combinations(range(3),2) for a,b in product(v[i],v[j])]
    return normalize(groups+stars+bridges)
