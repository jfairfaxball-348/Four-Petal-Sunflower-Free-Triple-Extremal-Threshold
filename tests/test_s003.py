import json, pathlib, sys, unittest, hashlib, itertools
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from s003_cyclic import classify,first_quartet,secondary_free,orbits

class S003CyclicTests(unittest.TestCase):
    def test_finite_exhaustive_replay(self):
        d=classify()
        self.assertEqual([d["counts"][str(i)]["free"] for i in range(4)],[1,13,16,0])
        self.assertEqual(sum(d["counts"][str(i)]["tested"] for i in range(4)),988)
        self.assertEqual(d["representative_sha256"],"727fdeeb9239b0f23bc0d46f60d0cbc9e0180310d959cdb92ae1c74e7ba94802")
        f=[tuple(map(int,row.split(','))) for row in (ROOT/"experiments/S003_BEST_CYCLIC_edges.txt").read_text().splitlines()]
        self.assertEqual(len(f),24)
        self.assertIsNone(first_quartet(f))
        self.assertTrue(secondary_free(f))
        self.assertEqual(hashlib.sha256((ROOT/"experiments/S003_BEST_CYCLIC_edges.txt").read_bytes()).hexdigest(),d["representative_sha256"])
        self.assertEqual(tuple(f),d["representative_triples"])
        self.assertEqual(set(f),{tuple(sorted((x+t)%12 for x in e)) for e in f for t in range(12)})

    def test_compact_obstruction_certificate(self):
        d=classify(); c=json.loads((ROOT/"experiments/S003_CYCLIC_CERTIFICATE.json").read_text())
        self.assertEqual(c["free_counts"],{k:v["free"] for k,v in d["counts"].items()})
        free_pairs=set(tuple(p) for p in c["free_pairs"])
        self.assertEqual(free_pairs,set(tuple(p) for p in d["survivors"]["2"]))
        f=orbits()
        triangles=[x for x in itertools.combinations(range(18),3)
          if all(tuple(p) in free_pairs for p in itertools.combinations(x,2))]
        self.assertEqual(triangles,[tuple(q["orbits"]) for q in c["compatible_pair_graph_triangles"]])
        for datum in c["compatible_pair_graph_triangles"]:
            e=tuple(sorted({t for i in datum["orbits"] for t in f[i]}))
            q=[tuple(t) for t in datum["quartet"]]
            self.assertTrue(set(q)<=set(e))
            self.assertEqual(first_quartet(q)[1],tuple(datum["core"]))
        self.assertEqual(len(triangles),8)

if __name__=="__main__":unittest.main()
