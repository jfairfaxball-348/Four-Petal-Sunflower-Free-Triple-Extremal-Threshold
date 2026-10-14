import unittest,sys,pathlib,hashlib
from itertools import combinations
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from s001_oracle import first,normalize
from s001_secondary import free
class S002StructuralControls(unittest.TestCase):
    def test_frozen_spec_integrity(self):
        p=ROOT/"experiments/S002_PRE_REGISTRATION_v1.md"
        self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(),
           "0f3976ddbe37111626f6da259f355e46d09bb01acd12c40b1efb0570d00a94b7")
    def test_full_semantics(self):
        for q in ([[0,1,2],[3,4,5],[6,7,8],[9,10,11]],
                  [[0,1,2],[0,3,4],[0,5,6],[0,7,8]],
                  [[0,1,2],[0,1,3],[0,1,4],[0,1,5]]):
            self.assertIsNotNone(first(q));self.assertFalse(free(q))
        q=[[0,1,2],[0,1,3],[0,2,3],[1,2,3]]
        self.assertIsNone(first(q));self.assertTrue(free(q))
    def test_s002_archive_is_partial(self):
        import json,csv
        state=json.loads((ROOT/"authoritative/STATE.json").read_text())
        self.assertEqual(state["s002"]["search_outcome"],"ITERATION_CAP_NOT_UNSAT")
        self.assertEqual(state["s002"]["iterations"],40)
        data=list(csv.DictReader((ROOT/"experiments/S002_ITERATIONS_v1.csv").open()))
        self.assertEqual(len(data),40)
        self.assertEqual(sum(int(r["new_four_sunflower_cuts"]) for r in data),12095)
        self.assertEqual(int(data[-1]["total_cuts"]),12095)
if __name__=="__main__":unittest.main()
