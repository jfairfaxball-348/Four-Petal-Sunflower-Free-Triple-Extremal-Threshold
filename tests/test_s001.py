import sys,pathlib,itertools,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/"src"))
from s001_oracle import normalize,first
from s001_secondary import free
from s001_reconstruct import build
from verify_s001_cert import load_edges,verify
class SunflowerControls(unittest.TestCase):
    def test_published(self):
        w=build()
        self.assertEqual(w,load_edges());self.assertEqual(len(w),39)
        self.assertIsNone(first(w));self.assertTrue(free(w))
    def test_certificate(self):self.assertEqual(verify(),521)
    def test_all_kernels(self):
        for es in ([[[i*3+j for j in range(3)] for i in range(4)],
              [[0,1,2],[0,3,4],[0,5,6],[0,7,8]],
              [[0,1,2],[0,1,3],[0,1,4],[0,1,5]]):
            self.assertIsNotNone(first(es));self.assertFalse(free(es))
    def test_near_miss(self):
        a=[[0,1,2],[0,1,3],[0,2,3],[1,2,3]]
        self.assertIsNone(first(a));self.assertTrue(free(a))
    def test_disjoint_union(self):
        a=[[0,1,2],[3,4,5]]
        b=[[20,21,22],[23,24,25]]
        self.assertIsNone(first(a));self.assertIsNone(first(b))
        self.assertIsNotNone(first(a+b));self.assertFalse(free(a+b))
    def test_invalid_and_relabel(self):
        for es in ([[[0,1,2],[2,1,0]],[[0,0,1]],[[0,1,2,3]]):
            with self.assertRaises(ValueError):normalize(es)
        es=[[0,1,2],[0,3,4],[0,5,6],[0,7,8]]
        moved=[[100+7*v for v in e] for e in es]
        self.assertEqual(first(es) is None, first(moved) is None)
        self.assertIsNone(first([]));self.assertIsNone(first([[4,5,6]]))
    def test_secondary_small_controls(self):
        universe=list(itertools.combinations(range(5),3))
        for k in [0,1,3,4,5]:
            for es in itertools.combinations(universe,k):
                self.assertEqual(first(es) is None,free(es))
if __name__=="__main__":unittest.main()
