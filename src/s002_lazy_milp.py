"""S002 deterministic reproduction: full 13-vertex binary MILP with exhaustive
four-sunflower cut separation. Optional scipy 1.17.0 (not used in CI).
Strictly bounded; 40 iterations. Source-free generator; no F39 starting state.
"""
from itertools import combinations,product
from time import monotonic
from pathlib import Path
from hashlib import sha256
import json,sys
import numpy as np
import scipy
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix

P=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(P/"src"))
from s001_oracle import first,normalize
from s001_secondary import free
E=list(combinations(range(13),3))
idx={e:i for i,e in enumerate(E)}

def quartet_sunflower(q):
    sets=list(map(set,q))
    six=[sets[a]&sets[b] for a,b in combinations(range(4),2)]
    return all(s==six[0] for s in six)

def published39():
    g=[tuple(range(3*i,3*i+3)) for i in range(3)]
    rows=list(g)+[(9,*p) for z in g for p in combinations(z,2)]
    hubs={(0,1):10,(0,2):11,(1,2):12}
    rows += [(hubs[a,b],x,y) for a,b in combinations(range(3),2)
             for x,y in product(g[a],g[b])]
    return normalize(rows)

def controls():
    F=published39()
    assert len(F)==39 and first(F) is None and free(F)
    raw="".join(",".join(map(str,e))+"\n" for e in F).encode()
    assert sha256(raw).hexdigest()=="1d9e73a5c0f60fb0526f1a2f31593a908d58e0989c2b4f0f92bc30654d3649cb"
    assert all(first(q) is not None and not free(q) for q in (
        [[3*i+j for j in range(3)] for i in range(4)],
        [[0,1,2],[0,3,4],[0,5,6],[0,7,8]],
        [[0,1,2],[0,1,3],[0,1,4],[0,1,5]]))
    assert first([[0,1,2],[0,1,3],[0,2,3],[1,2,3]]) is None
    try:normalize([[0,1,2],[2,1,0]]);raise AssertionError("duplicate accepted")
    except ValueError:pass
    return True

def build(cuts):
    M=lil_matrix((79+len(cuts),286),dtype=float)
    lo=np.full(M.shape[0],-np.inf)
    hi=np.full(M.shape[0],np.inf)
    for row,(u,v) in enumerate(combinations(range(13),2)):
        for i,e in enumerate(E):
            if u in e and v in e:M[row,i]=1
        hi[row]=3
    M[78,:]=1;lo[78]=hi[78]=40
    for k,c in enumerate(cuts):
        for i in c:M[79+k,i]=1
        hi[79+k]=3
    xlo=np.zeros(286);xlo[idx[0,1,2]]=1
    return LinearConstraint(M.tocsr(),lo,hi),Bounds(xlo,np.ones(286))

def run():
    controls()
    spec=P/"experiments/S002_PRE_REGISTRATION_v1.md"
    assert sha256(spec.read_bytes()).hexdigest()=="0f3976ddbe37111626f6da259f355e46d09bb01acd12c40b1efb0570d00a94b7"
    cuts=set();start=monotonic();output=[]
    verdict="ITERATION_CAP";solution=None
    for step in range(1,41):
        remain=65-(monotonic()-start)
        if remain<2:verdict="WALL_CAP";break
        lc,bds=build(sorted(cuts))
        res=milp(np.zeros(286),integrality=np.ones(286),bounds=bds,
                 constraints=lc,options={"time_limit":min(15,max(1,remain-1)),"mip_rel_gap":0.0})
        if res.status==2:
            verdict="PROVEN_INFEASIBLE_ON_13";break
        if res.x is None:
            verdict="UNKNOWN_SOLVER_NO_INTEGER";break
        if any(abs(float(v)-round(float(v)))>1e-6 for v in res.x):
            verdict="UNKNOWN_FRACTIONAL";break
        chosen=[E[i] for i,v in enumerate(res.x) if round(float(v))==1]
        if len(chosen)!=40 or (0,1,2) not in chosen:
            verdict="BAD_INTEGER";break
        if any(sum(a in e and b in e for e in chosen)>3
               for a,b in combinations(range(13),2)):
            verdict="BAD_PAIR_CONSTRAINT";break
        violations=[q for q in combinations(chosen,4) if quartet_sunflower(q)]
        independent=free(chosen)
        if not violations:
            assert first(chosen) is None and independent
            solution=chosen;verdict="40_FOUND";break
        assert not independent, "semantic checker disagreement"
        before=len(cuts)
        cuts.update(tuple(sorted(idx[e] for e in q)) for q in violations)
        assert len(cuts)>before
        output.append((step,len(cuts)-before,len(cuts),str(res.status)))
        print(output[-1],flush=True)
    result={"outcome":verdict,"iterations":output,"new_cuts":len(cuts),
            "scipy":scipy.__version__,"python":sys.version.split()[0],
            "witness":solution}
    if solution:
        raw="".join(",".join(map(str,e))+"\n" for e in solution).encode()
        result["sha256"]=sha256(raw).hexdigest()
    print(json.dumps(result,indent=2))
    return result

if __name__=="__main__":
    run()
