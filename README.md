# Erdős #738 — triangle-free induced-tree structure

A collection of structural results around induced trees in triangle-free graphs, including a sharp type-count theorem, an attaining construction, exact path-signature enumeration, and links to triangle-cover number.

## Sharp type-count theorem

Consider a complete ordered `d`-ary rooted tree (`d>=3`) of height `k`, embedded path-induced, level-stable, and type-uniform in a triangle-free graph. Let `c` be a join depth and put `n=k-c`.

The number of active ordered types at depth `c` is at most

\[
\boxed{\left\lfloor n^2/2\right\rfloor}.
\]

Summing over all join depths gives

\[
\sum_{n=1}^k\left\lfloor n^2/2\right\rfloor.
\]

Equivalently,

\[
k=2m:\quad \frac{m(m+1)(4m-1)}3,
\]

and

\[
k=2m+1:\quad \frac{m(m+1)(4m+5)}3.
\]

The proof comes from exact row restrictions forced by triangle-freeness and the diagonal/parent exclusions.

## Sharpness

Start with the complete rooted `d`-ary tree, keep all tree edges, and join two incomparable vertices exactly when their depths have opposite parity.

The resulting graph is triangle-free, and the original rooted tree remains path-induced, level-stable, and type-uniform. At each slice, the active ordered types are exactly the opposite-parity pairs, giving

\[
2\left\lfloor\frac n2\right\rfloor
\left\lceil\frac n2\right\rceil
=
\left\lfloor\frac{n^2}{2}\right\rfloor.
\]

Thus the bound is attained exactly at every slice by this construction.

## Path signatures

For an induced path on `n` vertices in a triangle-free graph, the neighborhood of any outside vertex meets the path in a set containing no two consecutive positions. Therefore the number of possible signatures is at most

\[
F_{n+2}.
\]

More generally, if successive contacts must be separated by at least `d>=2`, the signature count satisfies

\[
a_d(n)=a_d(n-1)+a_d(n-d).
\]

The verifier checks this recurrence for the packaged finite cases.

## Triangle-cover connection

For a graph `G`, let `tc(G)` be the least number of triangle-free graphs whose union is `G`. One useful general inequality in the program is

\[
\boxed{tc(G)\le \sup_v \chi(G[N(v)])}.
\]

This motivates a broader finite-threshold question: for a fixed finite tree `T` and integer `m`, does bounded `tc(G)<=m` together with sufficiently large chromatic number force an induced copy of `T`?

At `m=1`, this is the finite-threshold form of Erdős #738. The first genuinely new extension is `m=2`.

## Negative results

Two tempting routes are ruled out explicitly:

- there is no universal constant bounding the number of triangles containing an edge of a `K4`-free graph; page-book graphs give arbitrarily large examples;
- strong structure inside a single `K4`-free vertex link does not by itself force `tc(G)>2`.

## Verification

```bash
python verifiers/verify_erdos738_theorem_bank.py
python verifiers/verify_erdos738_x_595_cross_forge.py
```

The second verifier checks 11,347 assertions across all 1,099 graphs on at most five vertices in the packaged cross-result tests. A separate historical audit covers 1,032 `K4`-free graphs and 35,502 assertions.

The finite checks support the stated finite lemmas and formulas; the full Erdős #738 problem remains open.

Author: Jared Wilder. License: Apache-2.0.
