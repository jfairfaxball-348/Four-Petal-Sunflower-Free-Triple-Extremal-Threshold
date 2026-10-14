# S001 — Exact reconstruction, incremental lemma and deletion-resistant local saturation

## Definition and prior art

A simple 3-uniform family \(\mathcal F\) is free of 4-sunflowers if there is no unordered 4-subfamily of **four distinct edges** whose six *sets* of pairwise intersections are identical. Empty kernel is forbidden too. The full independent quartet oracle is `src/s001_oracle.py`. An algorithmically independent oracle in `src/s001_secondary.py` instead uses: no disjoint matching of 4 edges (kernel empty), no disjoint matching of 4 pairs in any vertex link (kernel singleton), and no 4 edges containing the same pair (kernel size two). These three alternatives are exhaustive since distinct triples cannot have kernel size 3.

Axante et al., arXiv:2609.06175v1, Theorem 5.1 gave a 39-triple family on 13 vertices; this is PRIOR ART. Reconstruct it by taking \(V_1=\{0,1,2\},V_2=\{3,4,5\},V_3=\{6,7,8\}\), 3 group triples, all 9 triples \(\{9\}\cup P\) where \(P\) is a 2-subset of a single group, and all 27 \(\{l_{ij},x,y\}\) for pairs of groups \(i<j\), vertices \(x\in V_i\), \(y\in V_j\), and \(l_{12}=10,l_{13}=11,l_{23}=12\). This is listed verbatim in `experiments/S001_F39_edges.txt`, SHA256 `1d9e73a5c0f60fb0526f1a2f31593a908d58e0989c2b4f0f92bc30654d3649cb`. Independently check 82,251 unordered quadruples and matching/link/pair criteria. Both pass. This does not establish any new extremal bound.

## Human-checkable incremental lemma — PROVED

Let \(\mathcal G\) be 4-sunflower-free and let \(e\notin\mathcal G\) be a triple. Then \(\mathcal G\cup\{e\}\) has a 4-sunflower if and only if there exist three distinct \(a,b,c\in\mathcal G\) and a set \(K\) such that

\[
a\cap b=a\cap c=b\cap c=e\cap a=e\cap b=e\cap c=K.
\]

Proof: a new forbidden quartet must use \(e\) (otherwise one was already in \(\mathcal G\)); its remaining members are some three distinct old edges and necessarily satisfy all six equalities. Conversely six equalities are precisely the prohibited sunflower condition. This reduction checks candidate extension e by 3-edge patterns, with no isomorphism or ambient-universe shortcut.

## Finite two-obstruction theorem — PROVED COMPUTATIONALLY WITH AUDITABLE CERTIFICATE

Let \(F_{39}\) be the **particular** 13-point family above. For *every* triple \(e\notin F_{39}\) on any finite ambient set containing the original vertices, there exist two collections \(T_e,U_e\) of three old edges each, such that:
1. \(T_e\cap U_e=\varnothing\) as collections of old edges (six distinct old edges);
2. \(T_e\cup\{e\}\) and \(U_e\cup\{e\}\) are both four-petal sunflowers, each verified by comparing ALL SIX intersection sets.

In consequence, for every \(d\in F_{39}\) and any \(e\notin F_{39}\), the family \((F_{39}\setminus\{d\})\cup\{e\}\) is not sunflower-free: at most one of the two three-edge obstruction collections contains \(d\), so the other forbidden quartet survives. The same holds with no deletion, because a certificate yields a forbidden quartet directly.

**Why the 521 cases cover ANY ambient finite set:** The candidate triple \(e\) has at most three vertices outside \([0,12]\). Relabel only those new vertices in increasing order as 13,14,15; all old F39 edges stay fixed. This relabelling preserves all intersection sets under a bijection; unused isolated vertices do not affect any intersection. Thus \(e\) is equivalent to one of \(\binom{16}{3}-39=521\) cases, with no other symmetry reductions used. This argument covers only extensions of the fixed F39, not every 39-family or all 40-families.

**Certificate:** `experiments/S001_C1_CERTIFICATES.json`; SHA256 `a76dfb6436bc19d37839a6fb21a8ef76642ed1032cd326f0e9e36cedfd8f801e`, 521 canonical keys, each pointing to TWO old edge index triples. Index zero through 38 is defined by lexicographically sorted `S001_F39_edges.txt`. Source `src/verify_s001_cert.py` is independent of generator: hash verify input and JSON; ensure all 521 exactly covered, 6 distinct old edge indices; for each of 1042 declared quartets recompute exact six set-intersections via `src/s001_oracle.py`. Additionally independent link/degree/matching oracle certifies F39 itself. These finite data, verification code and relabelling proof constitute the certificate: no SAT unsat status, universal search bound, or unverifiable solver claim is imported.

## Registered local search results — FINITE NEGATIVES

Pre-registered v1 (BEFORE run): 521 candidate one-edge extensions; all rejected. Removing each of 39 old edges left zero individually admissible novel triples on original 13 support, so no 40 witness via one-removal/two-new-edge exchange there. The latter avoids brute-force `39 * C(247,2)=1,184,859` pair tests: if no first new edge can be admitted, no admissible pair exists. This logical pruning is lossless by hereditary sunflower-freeness.

Pre-registered v2 (BEFORE run): C1 521 two-obstruction certificates, no exception. C2 removes each unordered pair of old F39 edges (741 cases), enumerates the individually admissible old-support novel triples, finds at most one per deleted pair, with aggregate admissible singles 54; thus no selection of three novel triples exists and no 40 witness in the 2-deletion/3-insertion original-support neighbourhood. Because any admissible 3-insertion must have each one-edge subset admissible, pruning is lossless. Logs `experiments/S001_RUN_v1.txt` and `S001_RUN_v2.txt`. No exhaustive bound on \(|V|\) or all families is asserted.

## Unresolved

New \(\ge40\) construction OPEN. Universal \(\le48\) OPEN; author \(\le49\) computer certificate identified but not independently replayed. The local theorem's global mathematical priority is UNCLEARED; it may be implicit in existing work and is not yet publishable. Any claim of fixed-rank Erdős–Rado asymptotic breakthrough is unwarranted. Verdict CONTINUE for one FUTURE S002 independent-architecture attack, not local trivial extension.
