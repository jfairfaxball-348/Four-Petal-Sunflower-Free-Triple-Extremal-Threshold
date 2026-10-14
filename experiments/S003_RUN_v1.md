# S003 frozen cyclic enumeration, run v1 (complete)

Date 2026-10-14. Pre-registration **committed before run** on branch in 5683c00424d85f711faae72bc4aece2e2a3ec181. Single 988-candidate run on Python 3.13.5; elapsed 2.302 seconds. Local original experiment source SHA256 7b679258130ee3bf7961a68c8c9b01167d1baf1e8a181eca6caa6670c201bf72. Hosted replay code: src/s003_cyclic.py; original local output SHA256 fad231ebf96b9b9c95ca6d2db5993313aaff6b31be98bec24b450f8ea2ea2242. Recorded exact reproducible class counts below and compact independent witness certificate in S003_CYCLIC_CERTIFICATE.json.

Controls before enumeration: source F39 reproduced and passed both six-set and link/matching oracles; empty, one-point and two-point kernels rejected; unequal intersection and duplicate controls passed. Exactly 220 initial triples split into 18 size-12 orbits and one size-4 orbit of four disjoint triples. Candidate unions 1+18+153+816=988, without further symmetry pruning.

| ordinary orbits | candidates | sunflower-free |
|---|---:|---:|
|0|1|1|
|1|18|13|
|2|153|16|
|3|816|0|

Certified max in the cyclic symmetry class: **24**, witness orbit indices (1,7), orbit representatives (0,1,3), (0,1,9), 24 canonical triples SHA256 727fdeeb9239b0f23bc0d46f60d0cbc9e0180310d959cdb92ae1c74e7ba94802. Witness independently rechecked by third bit-mask six-intersection oracle on all 10,626 four-tuples and verified translation invariance and SHA256.

For concise exhaustive certificate: 13 allowed single orbits, 16 allowed orbit pairs; there are only 8 triangles in the compatibility graph, and each has a four-edge forbidden witness in the JSON. Thus even a pairwise-gate proof can reduce 816 triple combinations to eight explicitly excluded cases. This is NOT a general n<=12 infeasibility certificate nor new f(3,4) inequality; 40 on >=13 points remains unknown. Do not extrapolate.
