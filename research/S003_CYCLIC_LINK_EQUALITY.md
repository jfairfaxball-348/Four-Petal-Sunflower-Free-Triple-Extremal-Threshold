# S003 — degree-ten link equality: obstruction to a shortcut, exact cyclic restricted theorem

## Global problem and prior art
Simple 3-uniform families; four **distinct** triples cannot have all **six pairwise set intersections identical**, including empty. Axante et al., arXiv:2609.06175v1 Lemmas 2.2/2.3 and 5.2, using Chvátal–Hanson (1976), already show that vertex link graphs have max degree 3, matching number <=3, and at most CH(3,3)=10 edges. In a 40-edge family on exactly 12 points, every vertex degree therefore equals 10. THIS IS PRIOR ART incidence deduction, not a new universal threshold result.

## A rigorous classification shortcut is false
The graph extremal equation |E(H)|=10, Δ(H)<=3, ν(H)<=3 **does not** force H to use exactly seven nonisolated vertices. Here are explicit examples of *different* link equality types:

* Seven vertices: subdivide one edge of K(3,3). There are 10 edges, maximum degree three, matching number <=floor(7/2)=3.
* Eight vertices: R disjoint union K3, where R=K5 minus disjoint P3 and K2 edges. R has 7 edges, maximum degree three and matching number two (five vertices); triangle adds 3 edges, max degree two, matching number one, totaling 10 and matching 3.
* Nine vertices: R disjoint union the claw K(1,3). This has 7+3=10 edges, max degree three, matching number 2+1=3.

All may be padded with isolated vertices to an 11-point link graph. Thus degree-10 equality does **not** provide a seven-point near-cubic structure on its own. Full global incidence compatibility and absence of four disjoint triples still require proof. The R graph is already present in Axante et al. Lemma 5.5; these examples are not asserted as novel graph classification.

## Exact new (restricted) theorem — complete finite certificate
Let G be a simple 3-uniform 4-sunflower-free family on Z/12Z invariant under x -> x+1 mod12. Then |G|<=24, and equality is achievable. Formal orbit proof: a nontrivial stabilizer of a 3-subset under regular Z12 translation has size three; it must be {0,4,8}, giving the unique exceptional orbit of four cosets {i,i+4,i+8}, i=0..3. Those are four disjoint triples, so no valid family contains them. Remaining 216 triples form exactly 18 length-12 orbits. Each ordinary orbit contributes degree three at each of 12 points. Prior-art degree bound d(v)<=10 thus implies a valid translation-invariant family is union of at most three ordinary orbits.

Finite exhaustive step: generate all combinations of zero to three of the 18 orbits, exactly 1+18+153+816=988. Two semantically independent exhaustive checks agree on all: full six-intersection quartet oracle and matching-of-four in the hypergraph / links plus pair-codegree. Free counts: 1,13,16,0 for k=0,1,2,3. This yields |G|<=24. The 24 edges in experiments/S003_BEST_CYCLIC_edges.txt form two orbits (generators {0,1,3} and {0,1,9}); both oracles validate and independent bitwise full quartet check validates all C(24,4)=10626 quartets. SHA256 727fdeeb9239b0f23bc0d46f60d0cbc9e0180310d959cdb92ae1c74e7ba94802.

Smaller exclusion certificate: 13 acceptable individual ordinary orbits produce exactly 16 mutually compatible pairs. The compatibility graph has only 8 triangles; all eight are eliminated by a specific quartet in experiments/S003_CYCLIC_CERTIFICATE.json. Consequently any 3-orbit family either contains an already-invalid subfamily, or is one of those eight with a displayed four-sunflower. This provides explicit short witness data rather than relying solely on a claim about 816 opaque tests.

## Significance and limitations
This identifies a fully resolved cyclic symmetry subproblem, hence excludes any **12-vertex 40-family possessing a regular 12-cycle symmetry**. It does NOT exclude asymmetric 40-families on 12 vertices, any n>=13, or improve the published 39<=f(3,4)<=49. Search code/standard-library version, registration and failed populations archived. No proof that equality-link graphs globally assemble, no full equality-case graph classification, no novelty clearance or publication gate achieved. Parent programme should reassess before more child search.
