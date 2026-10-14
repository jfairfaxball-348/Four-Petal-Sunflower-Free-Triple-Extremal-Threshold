"""Reproduce S001's two-edge-disjoint obstruction certificate; generator is separate from verifier."""
from itertools import combinations
import hashlib,json,pathlib
from s001_reconstruct import build
from s001_oracle import first
ROOT=pathlib.Path(__file__).resolve().parents[1]
TARGET="a76dfb6436bc19d37839a6fb21a8ef76642ed1032cd326f0e9e36cedfd8f801e"
def generate():
    F=build()
    saved={}
    for e in combinations(range(16),3):
        if e in F: continue
        hits=[]
        for idx in combinations(range(39),3):
            s=[F[i] for i in idx]+[e]
            if first(s) is not None: hits.append(idx)
        pair=None
        for i,w in enumerate(hits):
            for z in hits[i+1:]:
                if set(w).isdisjoint(z):
                    pair=[list(w),list(z)]
                    break
            if pair is not None:break
        if pair is None: raise AssertionError(("no pair",e))
        saved[",".join(map(str,e))]=pair
    out=(json.dumps(saved,sort_keys=True,separators=(",",":"))+"\n").encode()
    got=hashlib.sha256(out).hexdigest()
    print("generated",len(saved),"sha256",got)
    assert len(saved)==521 and got==TARGET
    assert out==(ROOT/"experiments/S001_C1_CERTIFICATES.json").read_bytes()
if __name__=="__main__":generate()
