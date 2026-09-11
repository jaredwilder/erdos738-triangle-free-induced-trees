# Erdős #738 — triangle-free induced-tree structure

**A 174-claim research bank on triangle-free induced trees and the Gyárfás–Sumner direction, with exact sharp bounds, an attaining construction, cross-theorems with triangle-cover number, explicit refutations, and two standalone finite verifiers.**

Author: Jared Wilder. Banks dated 2026-08-04. First public timestamp: 2026-09-11.

This repository is the focused public home for the Erdős #738 program. The parent induced-tree problem remains a larger frontier; the results below have the exact scopes stated in their individual cards.

## Sharp type-count theorem

For a complete ordered `d`-ary rooted tree (`d>=3`) of height `k` embedded path-induced, level-stable and type-uniform in a triangle-free graph, let `c` be the join depth and `n=k-c`.

**T06.** The number of active ordered types at depth `c` is at most

`floor(n^2/2)`.

**T07.** Summing over join depths gives

`sum_{n=1}^k floor(n^2/2)`,

with closed forms

- `k=2m`: `m(m+1)(4m-1)/3`;
- `k=2m+1`: `m(m+1)(4m+5)/3`.

The closed forms were independently checked against direct summation for `k=1..24`.

### Attaining construction

**T08.** Start with the complete rooted `d`-ary tree, keep every tree edge, and join two incomparable vertices exactly when their depths have opposite parity. The resulting host is triangle-free, and the rooted tree remains path-induced, level-stable and type-uniform.

**T09.** In this host the type indicator `A_c(a,b)` is active exactly when `a,b` have opposite parity. Hence every slice has

`2 floor(n/2) ceil(n/2) = floor(n^2/2)`

active ordered types. The upper bound is therefore sharp. The parity count was independently checked for `n=1..39`.

## Exact path-signature enumeration

**P05.** For an `n`-vertex induced path in a triangle-free graph, an outside vertex's neighbourhood signature is a subset of path positions containing no two consecutive vertices. Hence there are at most `F_(n+2)` signatures.

**P06.** If successive contacts must have index gap at least `d>=2`, the signature count satisfies

`a_d(n)=a_d(n-1)+a_d(n-d)`.

The finite verifier checks this recurrence for `d=2,3,4`; at `d=2` it recovers the Fibonacci sequence required by P05.

## Triangle-cover cross-hierarchy

The program interacts with the broader triangle-cover theory now housed at `jaredwilder/triangle-cover-number`.

A central cross-result is:

**XLINK03.** For every graph `G`,

`tc(G) <= sup_v chi(G[N(v)])`.

The generated next-layer target **XLAYER10** asks whether for every finite tree `T` and integer `m>=1` there is `f(T,m)` such that every graph with `tc(G)<=m` and `chi(G)>f(T,m)` contains an induced `T`. The case `m=1` recovers the Erdős #738 direction; `m=2` is the first proposed extension frontier.

This target is recorded as unproved.

## Exact refutations

The bank also removes two tempting false routes.

**595:T66.** The claim that every edge of a K4-free graph belongs to at most a fixed constant number of triangles is false even for finite graphs: arbitrarily large page-book graphs give counterexamples.

**XCONE10.** A lower bound on chromatic number, criticality, induced-tree richness or type-tensor complexity of a single K4-free vertex link does not by itself force `tc(G)>2`.

These are useful negative theorems because they delimit the cross-program strategy rather than merely recording failed experiments.

## Verification

Run:

```bash
python verifiers/verify_erdos738_theorem_bank.py
python verifiers/verify_erdos738_x_595_cross_forge.py
```

Both were rerun from committed source on 2026-09-11 and exited 0.

| verifier | result |
|---|---|
| `verify_erdos738_theorem_bank.py` | active-type counts match the closed formulas exactly in the packaged finite cases |
| `verify_erdos738_x_595_cross_forge.py` | **11,347 assertions across 1,099 graphs** through 5 vertices for the listed cross-results |

A second finite audit covers **1,032 K4-free graphs**, **3,220 maximal layers**, **6,438 signature-fiber checks**, and **35,502 assertions**.

These computations certify their stated finite kernels. They are not substitutes for proofs of infinite/cardinal statements.

## Evidence state

The 174-card bank mixes proved-in-packet statements, finite computations, targets, refutations and cross-program statements. Those statuses remain distinct in the source bank.

The emitted Lean missions were **not executed**, so this repository does not describe the 174 cards as Lean-certified. Historical novelty has likewise not been globally adjudicated.

One historical verifier artifact lists 16 recursive claims under `invalidated_by_retraction`; that file is a synthetic retraction-propagation test, not a live retraction of those claims.

## Provenance

Earlier release copies of this program remain in broad repositories such as `erdos-theorems/erdos738-frontier/` and the public archive. This focused repository is now the preferred human/citation home; the broader copies are provenance mirrors.

## License

Apache-2.0.
