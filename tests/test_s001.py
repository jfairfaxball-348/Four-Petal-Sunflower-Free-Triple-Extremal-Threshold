import itertools
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'src'))
from s001_oracle import normalize, first
from s001_secondary import free
from s001_reconstruct import build
from verify_s001_cert import load_edges, verify


class SunflowerControls(unittest.TestCase):
    def test_published_39(self):
        edges = build()
        self.assertEqual(edges, load_edges())
        self.assertEqual(len(edges), 39)
        self.assertIsNone(first(edges))
        self.assertTrue(free(edges))

    def test_complete_two_obstruction_certificate(self):
        self.assertEqual(verify(), 521)

    def test_all_three_kernel_types(self):
        controls = [
            [[3 * i + j for j in range(3)] for i in range(4)],
            [[0, 1, 2], [0, 3, 4], [0, 5, 6], [0, 7, 8]],
            [[0, 1, 2], [0, 1, 3], [0, 1, 4], [0, 1, 5]],
        ]
        for edges in controls:
            with self.subTest(edges=edges):
                self.assertIsNotNone(first(edges))
                self.assertFalse(free(edges))

    def test_equal_intersection_cardinality_is_not_equality(self):
        edges = [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]]
        self.assertIsNone(first(edges))
        self.assertTrue(free(edges))

    def test_disjoint_union_trap(self):
        part_a = [[0, 1, 2], [3, 4, 5]]
        part_b = [[20, 21, 22], [23, 24, 25]]
        self.assertIsNone(first(part_a))
        self.assertIsNone(first(part_b))
        self.assertIsNotNone(first(part_a + part_b))
        self.assertFalse(free(part_a + part_b))

    def test_invalidity_relabelling_and_isolated_vertices(self):
        invalids = [
            [[0, 1, 2], [2, 1, 0]],
            [[0, 0, 1]],
            [[0, 1, 2, 3]],
        ]
        for edges in invalids:
            with self.assertRaises(ValueError):
                normalize(edges)
        edges = [[0, 1, 2], [0, 3, 4], [0, 5, 6], [0, 7, 8]]
        moved = [[100 + 7 * v for v in e] for e in edges]
        self.assertEqual(first(edges) is None, first(moved) is None)
        self.assertIsNone(first([]))
        self.assertIsNone(first([[4, 5, 6]]))

    def test_independent_oracles_agree_on_small_families(self):
        universe = list(itertools.combinations(range(5), 3))
        for k in (0, 1, 3, 4, 5):
            for edges in itertools.combinations(universe, k):
                self.assertEqual(first(edges) is None, free(edges))


if __name__ == '__main__':
    unittest.main()
