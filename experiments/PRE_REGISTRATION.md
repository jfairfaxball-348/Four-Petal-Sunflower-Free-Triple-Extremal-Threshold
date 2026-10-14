# Experiment registry: S001 frozen studies completed

P001B-S000 administrative bootstrap only. Future P001B-S001 must write FROZEN versioned `experiments/S001_*.md` BEFORE nontrivial search, with: exact hypothesis and source reproduction; universe/population cutoff plus global justification if upper target; edge-count/search ranges; isomorphism/symmetry algorithms and proof of coverage; environment/runtime/versions/seed; resource/time cap and abort; file formats and sha256; independent set-intersection checker; positive/negative controls; success criteria; STOP rules; evidence preservation/failed approaches; separate bounded numerical vs universal conclusions. Changes require pre-execution frozen version, never retroactive updates. Pedagogical test examples are not search evidence.


## S001 completed and frozen versions (do not retroactively edit)
- experiments/S001_PRE_REGISTRATION_v1.md SHA256 at local experiment freeze: 9f1a84657c7563f8c48da18279d3bbfc65ee4a2116ca1cdfdf8c108897cada2a; v1 A/B before search.
- experiments/S001_PRE_REGISTRATION_v2.md SHA256 at local experiment freeze: c81d8ca6fa2408117170474cf9b634356ec8dc7fe2ca075e33b7276d520089e4; v2 C1/C2 before search.
- Source witness sha256 1d9e73a5c0f60fb0526f1a2f31593a908d58e0989c2b4f0f92bc30654d3649cb; C1 cert sha256 a76dfb6436bc19d37839a6fb21a8ef76642ed1032cd326f0e9e36cedfd8f801e.
- All experiments bounded to F39 local exchange. S002 new runs require separate prior frozen plan.

## S002 complete frozen v1
- experiments/S002_PRE_REGISTRATION_v1.md SHA256 `0f3976ddbe37111626f6da259f355e46d09bb01acd12c40b1efb0570d00a94b7`, written/hash-fixed BEFORE local solver invocation.
- Full 286-triple population on 13 vertices, 40 selected, anchor (0,1,2), independent oracles, codegree3 + lazy quartet cuts, Python3.13.5/scipy1.17.0, 40-iteration/65s cap. Actual run stopped ITERATION_CAP. Results: experiments/S002_RUN_v1.md and S002_ITERATIONS_v1.csv. Not exhaustiveness.

## S003 frozen before experiment
- experiments/S003_PRE_REGISTRATION_v1.md committed as first S003 branch commit 5683c00424d85f711faae72bc4aece2e2a3ec181 BEFORE local run. Immutable original plan: all 988 cyclic Z12 orbit unions (0-3 ordinary orbits), source F39 controls, full quartet and separate matching/link/pair oracle. Completed 2.302 seconds Python3.13.5. See S003_RUN_v1.md, S003_CYCLIC_CERTIFICATE.json, S003_BEST_CYCLIC_edges.txt and src/s003_cyclic.py. Restricted result only.
