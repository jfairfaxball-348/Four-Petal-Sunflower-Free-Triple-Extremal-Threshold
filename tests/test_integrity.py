import importlib.util
import pathlib
import unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("bootstrap_validate",ROOT/"scripts/validate.py")
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
class IntegrityTests(unittest.TestCase):
    def test_schema_and_handoff(self):
        self.assertTrue(mod.check())
    def test_sunflower_kernel_controls(self):
        # Pedagogical exact semantics only: not an experiment or extremal search.
        def sunflower(edges):
            self.assertEqual(len(edges),4)
            sets=[frozenset(e) for e in edges]
            self.assertTrue(all(len(s)==3 for s in sets))
            self.assertEqual(len(set(sets)),4)
            ints=[sets[i]&sets[j] for i in range(4) for j in range(i+1,4)]
            return len(set(ints))==1
        self.assertTrue(sunflower([{0,1,2},{3,4,5},{6,7,8},{9,10,11}])) # empty kernel
        self.assertTrue(sunflower([{0,1,2},{0,3,4},{0,5,6},{0,7,8}])) # singleton
        self.assertTrue(sunflower([{0,1,2},{0,1,3},{0,1,4},{0,1,5}])) # pair kernel
        self.assertFalse(sunflower([{0,1,2},{0,1,3},{0,4,5},{6,7,8}])) # unequal sets
if __name__=="__main__":unittest.main()
