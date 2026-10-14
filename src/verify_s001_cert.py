"""Certificate verification independent of certificate creation and search predicates."""
from itertools import combinations
from pathlib import Path
import json,hashlib
from s001_oracle import normalize,first
ROOT=Path(__file__).resolve().parents[1]
EDGE_SHA="1d9e73a5c0f60fb0526f1a2f31593a908d58e0989c2b4f0f92bc30654d3649cb"
CERT_SHA="a76dfb6436bc19d37839a6fb21a8ef76642ed1032cd326f0e9e36cedfd8f801e"
def load_edges():
    data=(ROOT/"experiments/S001_F39_edges.txt").read_bytes()
    assert hashlib.sha256(data).hexdigest()==EDGE_SHA
    es=normalize([tuple(map(int,r.split(","))) for r in data.decode().splitlines()])
    assert len(es)==39 and first(es) is None
    return es
def verify():
    es=load_edges()
    data=(ROOT/"experiments/S001_C1_CERTIFICATES.json").read_bytes()
    assert hashlib.sha256(data).hexdigest()==CERT_SHA
    cert=json.loads(data)
    candidates={",".join(map(str,e)) for e in combinations(range(16),3) if e not in es}
    assert len(candidates)==521 and set(cert)==candidates
    for k,pair in cert.items():
        e=tuple(map(int,k.split(",")))
        assert len(pair)==2 and len(pair[0])==len(pair[1])==3
        assert all(type(i) is int and 0<=i<39 for w in pair for i in w)
        assert len(set(pair[0]+pair[1]))==6
        for w in pair:
            q=[es[i] for i in w]+[e]
            sun=first(q)
            assert sun is not None and len(sun[0])==4
    return len(cert)
if __name__=="__main__":print("S001 certificate PASS",verify())
