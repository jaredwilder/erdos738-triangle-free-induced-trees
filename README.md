# erdos738-triangle-free-induced-trees

**A 174-claim theorem bank on Erdős 738 (triangle-free induced trees, the Gyárfás–Sumner
direction), with exact bounds, a matching sharpness construction, a refutation, and two standalone
verifiers that both exit 0.**

Author: Jared Wilder. Banks dated 2026-08-04. First public timestamp: 2026-09-11.

**Erdős 738 is not closed.** What is here is a body of exact finite mathematics built around it, a
cross-hierarchy joining it to Erdős 595, and the verification that backs the finite part.

---

## Run the verifiers

```
python verifiers/verify_erdos738_theorem_bank.py
python verifiers/verify_erdos738_x_595_cross_forge.py
```

Both re-run from committed source on 2026-09-11, **exit 0**:

| verifier | result |
|---|---|
| `verify_erdos738_theorem_bank.py` | `"status": "PASS"` — active type counts match the closed formula exactly (14 = 14 at d=3,k=4; 6 = 6 at the smaller case) |
| `verify_erdos738_x_595_cross_forge.py` | `"passed": true` — **11,347 assertions, 1,099 graphs exhausted** to 5 vertices, checking XLINK01/03, XLINK05, XLINK08, XCONE08, XLAYER07 |

The first carries its own ceiling: *"Finite exhaustive audit only; Lean remains the proof authority
requested by the user."*

## The exact bounds, and the construction that makes them sharp

For a complete ordered `d`-ary rooted tree (`d ≥ 3`) of height `k` embedded path-induced,
level-stable and type-uniform in a triangle-free graph:

**T06.** For join depth `c` and `n = k − c`, the number of active ordered types is at most
`⌊n²/2⌋`.

**T07.** Across all join depths the total is at most `Σ_{n=1}^{k} ⌊n²/2⌋`, which is

```
k = 2m      ->  m(m+1)(4m−1)/3
k = 2m+1    ->  m(m+1)(4m+5)/3
```

**Both closed forms verified here against direct summation for k = 1..24.**

**T08 (the construction).** On a complete rooted `d`-ary tree, keep every tree edge and join two
incomparable vertices exactly when their depths have **opposite parity**. The result is
triangle-free, and the rooted tree sits inside it path-induced, level-stable and type-uniform.

**T09 (sharpness).** In that host, `A_c(a,b) = 1` exactly when `a` and `b` have opposite parity, so
every slice carries `⌊(k−c)²/2⌋` active types and **T06 and T07 are sharp.** The count is
`2⌊n/2⌋⌈n/2⌉ = ⌊n²/2⌋`, **verified here for n = 1..39.**

That pairing — an upper bound and an explicit host attaining it — is the strongest block in the
bank.

## Exact enumeration

**P05.** For an `n`-vertex induced path in a triangle-free graph, an outside vertex's neighbourhood
signature is a subset with **no two consecutive path vertices**, so at most `F_{n+2}` signatures are
possible.

**P06.** If consecutive contacts must have index gap at least `d ≥ 2`, the signature count obeys

```
a_d(n) = a_d(n−1) + a_d(n−d)
```

**Verified here for d = 2, 3, 4.** At `d = 2` it produces 2, 3, 5, 8, 13, 21, 34, 55 — Fibonacci,
as P05 requires.

## A refutation

**595:T66, marked `REFUTED_ROUTE`.** The assertion *"every edge of a K₄-free graph belongs to at
most a fixed constant number of triangles"* is **false, even for finite graphs** — m-page books
defeat it for arbitrary m.

**X:XCONE10, refuted.** No lower bound on chromatic number, criticality, induced-tree richness or
type-tensor complexity of a single K₄-free vertex link can by itself force `tc(G) > 2`.

## The cross-hierarchy

**X:XLINK03**, the engine of the joint campaign: for every graph `G`,
`tc(G) ≤ sup_{v} χ(G[N(v)])`.

**X:XLAYER10**, marked `UNPROVED_CHECKABLE_TARGET` — the generated conjecture the whole campaign
exists to attack: for every finite tree `T` and integer `m ≥ 1` there is `f(T,m)` such that every
graph with `tc(G) ≤ m` and `χ(G) > f(T,m)` contains an induced `T`. **The case `m = 1` is Erdős
738.** XLAYER11 names `m = 2` as the first frontier.

## What is not claimed

`FINAL-VERIFICATION.json` records `lean_executed: false`, `novelty_claimed: false`,
`flagship_closed: false`, and **all 174 claims carry `novelty_status: UNRUN`**. The Lean names in
`LEAN-MISSIONS.jsonl` are emitted as missions and were **never run**.

`FINITE-MATH-VERIFICATION.json` states its own limit: *"Finite exhaustion supports the exact finite
kernels only; it does not certify the infinite/cardinal flagship claims."* Its scale is 1,032
K₄-free graphs to 5 vertices, 3,220 maximal layers, 6,438 signature-fiber checks, 35,502 assertions.

**One thing not to misread.** `HOSTILE-VERIFICATION.json` lists 16 recursive claims under
`invalidated_by_retraction`. That is the retraction-propagation test **firing correctly on a
synthetic input**, not a live retraction — those claims are `PROVED_IN_PACKET` in the bank.

## Why the verifiers were unrunnable until now

The forge output lived in the repository and the **source banks it verifies against did not** — they
were in a downloads folder. The committed copy of the pipeline therefore failed immediately with a
missing-input error. Both halves are here together for the first time.

The generator itself is not published. The verifiers are.

## License

Apache-2.0.
