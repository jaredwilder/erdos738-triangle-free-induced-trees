# Erdős #738 Encirclement Theorem Bank
**Date:** 2026-08-04  
**Mode:** theorem-generation pass from the encirclement/RSI campaign  
**Claim boundary:** every item marked `PROVED_IN_PACKET` has an elementary proof route supplied here, but **historical novelty is unknown** until the user’s novelty checker clears the exact statement. Items marked `UNPROVED_CHECKABLE_TARGET` are finite theorem-search obligations, not results.

## Source boundary
The campaign target is Erdős Problem #738 / the triangle-free case of Gyárfás–Sumner. The literature inputs used to define the frontier are:
- Tung Nguyen, Alex Scott, Paul Seymour, **A note on the Gyárfás–Sumner conjecture**, arXiv:2302.08922 — path-induced, level-stable, type-uniform rooted-tree copies.
- Tung H. Nguyen, **On polynomially high-chromatic pure pairs**, arXiv:2504.21127 — complete/anticomplete pair machinery and the complete-pair formulation.
- The attached Math Encirclement Engine plan supplied the authority split: search proposals remain separate from Court-verified claims.

## Inventory
- **62 proof-backed theorem statements/schemas**
- **12 finite, executable theorem-search targets**
- Two strongest paper-shaped packages: **Extremal Type-Tensor Theory** and **Mixing–Spider Characterization**.

## Highest-value novelty checks
1. **T06 — Sharp Slice Active-Type Bound.** Let d≥3 and let a complete ordered d-ary rooted tree of height k be embedded path-induced, level-stable, and type-uniform in a triangle-free graph. For c<a,b≤k, let A_c(a,b)=1 when incomparable vertices of ordered type (a,b,c) are adjacent. For fixed join depth c and n=k-c, the number of active ordered types satisfies |supp(A_c)|≤⌊n²/2⌋.
2. **T07 — Total Active-Type Bound.** Let d≥3 and let a complete ordered d-ary rooted tree of height k be embedded path-induced, level-stable, and type-uniform in a triangle-free graph. For c<a,b≤k, let A_c(a,b)=1 when incomparable vertices of ordered type (a,b,c) are adjacent. Across all join depths, the total number of active ordered types is at most Σ_{n=1}^k⌊n²/2⌋. If k=2m this equals m(m+1)(4m-1)/3; if k=2m+1 it equals m(m+1)(4m+5)/3.
3. **T08 — Parity-Defect Host Construction.** On a complete rooted d-ary tree, keep all tree edges and add an edge between incomparable vertices exactly when their depths have opposite parity. The resulting graph is triangle-free, the rooted tree is path-induced, level-stable, and type-uniform.
4. **T09 — Sharpness of the Active-Type Bounds.** The parity-defect host T08 has A_c(a,b)=1 exactly when a and b have opposite parity. Hence every slice has ⌊(k-c)²/2⌋ active types and T06–T07 are sharp.
5. **M06 — Exact Reach-Profile Equivalence.** For fixed positive integers r_1,…,r_q, the following are equivalent: (i) there exist pairwise anticomplete connected sets C_i with reach at least r_i from N(v)∩C_i; (ii) G contains an induced spider centered at v with arm lengths at least r_i+1.
6. **N15 — Critical Escape-Boundary Theorem.** Under N13, let C be a component of G-N[S] with χ(C)≥k-|S|. Its external neighborhood B=N(C) lies in N(S)\S, separates C from S, and is not a clique. In particular, B contains two nonadjacent vertices.
7. **P05 — Fibonacci Contact-Signature Count.** For an n-vertex induced path P in a triangle-free graph, the neighborhood signature N(x)∩V(P) of an outside vertex is a subset with no consecutive path vertices. Hence at most F_{n+2} signatures are possible.
8. **P07 — Nonempty Signature Fibers Are Stable.** In a triangle-free graph, for a fixed induced path P and a fixed nonempty signature S⊆V(P), all outside vertices x with N(x)∩V(P)=S form a stable set.
9. **C01 — Clean-Child or Large Fan Dichotomy.** Let G be triangle-free, u∈V(G), X⊆V(G)\N[u] finite and nonempty, and B⊆N(u). Then either some b∈B is anticomplete to X, or some x∈X has at least ⌈|B|/|X|⌉ neighbors in B; in the latter case {u,x} with those neighbors induces K_{2,m}.
10. **T10 — Type-Profile Determines the Defect Graph.** In a type-uniform copy, two target embeddings with identical ordered type for every incomparable target-vertex pair induce identical extra-edge patterns.
11. **T11 — Sibling-Selection Sterility.** Changing only the identities of selected sibling branches, while preserving every target pair’s ordered depth/join type, cannot turn a non-induced target copy into an induced one.
12. **N03 — Isolate-Sharp Closed-Neighborhood Bound.** Let I be the set of vertices isolated in G[S]. Then χ(G[N[S]]) ≤ |S| if I is empty, and χ(G[N[S]]) ≤ |S|+1 otherwise.
13. **N07 — Sequential Protected Deletion Ledger.** Let G0=G. For i=1,…,m, let S_i⊆V(G_{i-1}) induce no isolated vertices in G_{i-1}, and put G_i=G_{i-1}-N_{G_{i-1}}[S_i]. Then χ(G_m) ≥ χ(G)-Σ_i |S_i|.

## Suggested paper packages
### Package A — Extremal defect tensors in triangle-free type-uniform tree copies
Combine T01–T12. The headline is the sharp slice bound `⌊n²/2⌋`, the exact total-height formula, and the parity-defect host attaining equality. This is the most novel-looking, finite, self-contained cluster.

### Package B — Mixing profiles and induced spiders
Combine M01–M07. The headline is the exact equivalence between anticomplete connected regions with prescribed reach profile and induced spiders with the corresponding arm lengths.

### Package C — Chromatic escape from finite induced structures
Combine N03–N07 and N13–N16. The headline is a quantitative high-chromatic escape component outside a connected finite structure, together with a nonclique attachment boundary in a critical graph.

### Package D — Induced-path contact codes
Combine P01–P12. The headline is the exact cycle dictionary for consecutive contacts, Fibonacci/d-separated signature counts, and stable nonempty signature fibers.

### Package E — Contamination-fan calculus
Combine C01–C06. The headline is a clean-child/large-fan dichotomy, its weighted form, and the exact conversion of the first legal cross-branch contamination into an induced cycle.

## Lean formalization order
1. N01, N09, C07, C08 — basic triangle/clique facts.
2. M01, P01, C05 — shortest-path / induced-cycle extraction.
3. N02–N07 — finite colorings and deletion inequalities.
4. M02–M06 — pairwise anticomplete region extraction.
5. C01–C03 — finite pigeonhole and weighted averaging.
6. N14–N16 — critical graph gluing arguments.
7. T01–T12 — ordered rooted trees, types, tensor support, parity host.

## Exact theorem packets

### Triangle-Free Budget

#### N01 — Neighborhood Stability
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `C`  
**Lean difficulty:** `1/5`

**Statement.** In every finite simple triangle-free graph G and every vertex v, the open neighborhood N(v) is a stable set.

**Proof route.** If two vertices of N(v) were adjacent, they and v would form a triangle.

**Novelty query.** `Neighborhood Stability`

#### N02 — Union-of-Neighborhoods Coloring Bound
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `B`  
**Lean difficulty:** `2/5`

**Statement.** For every finite S subset V(G) in a triangle-free graph, χ(G[⋃_{s∈S} N(s)]) ≤ |S|.

**Proof route.** Order S. Assign each vertex in the union to its first neighboring s. Each color class lies inside one stable neighborhood N(s).

**Dependencies.** N01

**Novelty query.** `Union-of-Neighborhoods Coloring Bound`

#### N03 — Isolate-Sharp Closed-Neighborhood Bound
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `3/5`

**Statement.** Let I be the set of vertices isolated in G[S]. Then χ(G[N[S]]) ≤ |S| if I is empty, and χ(G[N[S]]) ≤ |S|+1 otherwise.

**Proof route.** Every non-isolated vertex of S already lies in ⋃_{s∈S}N(s). Color that union with |S| colors by N02. The isolated vertices I form a stable set and require at most one additional color.

**Dependencies.** N02

**Novelty query.** `triangle-free closed neighborhood chromatic bound isolated vertices`

#### N04 — Connected Closed-Neighborhood Bound
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `B`  
**Lean difficulty:** `1/5`

**Statement.** If G is triangle-free and G[S] is connected with |S|≥2, then χ(G[N[S]]) ≤ |S|.

**Proof route.** A connected graph with at least two vertices has no isolated vertices; apply N03.

**Dependencies.** N03

**Novelty query.** `Connected Closed-Neighborhood Bound`

#### N05 — Protected Chromatic Remainder Bound
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `2/5`

**Statement.** If G is triangle-free and G[S] has no isolated vertices, then χ(G-N[S]) ≥ χ(G)-|S|.

**Proof route.** Color G[N[S]] using at most |S| colors by N03 and color the remainder separately. Since χ(G) is at most the sum, rearrange.

**Dependencies.** N03

**Novelty query.** `triangle-free chromatic number after deleting closed neighborhood connected set`

#### N06 — Finite-Set Survival in Infinite Chromatic Graphs
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `B`  
**Lean difficulty:** `2/5`

**Statement.** If G is triangle-free with infinite chromatic number and S is finite with G[S] having no isolated vertices, then G-N[S] still has infinite chromatic number.

**Proof route.** Otherwise G[N[S]] and G-N[S] would both have finite chromatic number; N03 gives the first, contradicting χ(G)=∞.

**Dependencies.** N03

**Novelty query.** `Finite-Set Survival in Infinite Chromatic Graphs`

#### N07 — Sequential Protected Deletion Ledger
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `3/5`

**Statement.** Let G0=G. For i=1,…,m, let S_i⊆V(G_{i-1}) induce no isolated vertices in G_{i-1}, and put G_i=G_{i-1}-N_{G_{i-1}}[S_i]. Then χ(G_m) ≥ χ(G)-Σ_i |S_i|.

**Proof route.** Apply N05 inside each current graph and telescope the inequalities.

**Dependencies.** N05

**Novelty query.** `sequential closed neighborhood deletion chromatic budget triangle-free`

#### N08 — Edge Closed-Neighborhood Bipartiteness
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `B`  
**Lean difficulty:** `2/5`

**Statement.** If uv is an edge of a triangle-free graph, then G[N[{u,v}]] is bipartite with parts N(u) and N(v), and therefore has chromatic number at most 2.

**Proof route.** N(u) and N(v) are stable. They are disjoint because a common neighbor would make a triangle; u∈N(v) and v∈N(u), so their union is exactly the closed neighborhood of {u,v}.

**Dependencies.** N01

**Novelty query.** `Edge Closed-Neighborhood Bipartiteness`

#### N09 — Common-Neighborhood Stability
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `C`  
**Lean difficulty:** `1/5`

**Statement.** For any two vertices u,v in a triangle-free graph, N(u)∩N(v) is stable.

**Proof route.** An edge inside the common neighborhood together with u would form a triangle.

**Dependencies.** N01

**Novelty query.** `Common-Neighborhood Stability`

#### N10 — Induced Two-Pole Fan
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `B`  
**Lean difficulty:** `1/5`

**Statement.** If u and v are nonadjacent in a triangle-free graph and |N(u)∩N(v)|≥m, then G contains an induced K_{2,m} with poles u,v.

**Proof route.** Choose m common neighbors. They are stable by N09, the poles are nonadjacent, and all pole-to-leaf edges are present.

**Dependencies.** N09

**Novelty query.** `Induced Two-Pole Fan`

#### N11 — One-Sided Attachment to an Induced Biclique
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `B`  
**Lean difficulty:** `1/5`

**Statement.** If (A,B) induces a nonempty complete bipartite graph in a triangle-free graph and x∉A∪B, then x has neighbors in at most one of A and B.

**Proof route.** A neighbor a∈A and b∈B would satisfy ab∈E and create triangle xab.

**Novelty query.** `One-Sided Attachment to an Induced Biclique`

#### N12 — Connected Dominator Chromatic Bound
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `B`  
**Lean difficulty:** `1/5`

**Statement.** If S is a connected dominating vertex set with |S|≥2 in a triangle-free graph G, then χ(G)≤|S|.

**Proof route.** Dominating means N[S]=V(G); apply N04.

**Dependencies.** N04

**Novelty query.** `Connected Dominator Chromatic Bound`

### Critical Cores

#### N13 — Quantitative Critical Escape Component
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `2/5`

**Statement.** Let G be a finite k-vertex-critical triangle-free graph. If H=G[S] is connected, 2≤|S|<k, then some component C of G-N[S] satisfies χ(C)≥k-|S|.

**Proof route.** N05 gives χ(G-N[S])≥k-|S|. The chromatic number of a disjoint union is the maximum over components.

**Dependencies.** N05

**Novelty query.** `critical triangle-free graph component outside closed neighborhood chromatic number`

#### N14 — Vertex-Critical Graphs Have No Clique Cutset
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `C`  
**Lean difficulty:** `3/5`

**Statement.** A finite vertex-critical graph has no clique cutset.

**Proof route.** If a clique K separates two sides, color each side together with K using fewer colors. Because K receives pairwise distinct colors, permute the color names on each side so the colorings agree on K, then combine them—contradicting criticality.

**Novelty query.** `Vertex-Critical Graphs Have No Clique Cutset`

#### N15 — Critical Escape-Boundary Theorem
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `3/5`

**Statement.** Under N13, let C be a component of G-N[S] with χ(C)≥k-|S|. Its external neighborhood B=N(C) lies in N(S)\S, separates C from S, and is not a clique. In particular, B contains two nonadjacent vertices.

**Proof route.** C is anticomplete to S and has no edges to other components of G-N[S], so B⊆N(S)\S. Removing B separates nonempty C from nonempty S. N14 forbids B from being a clique.

**Dependencies.** N13, N14

**Novelty query.** `critical graph high chromatic escape component nonclique boundary`

#### N16 — Independent Two-Cut in Triangle-Free Critical Graphs
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `B`  
**Lean difficulty:** `1/5`

**Statement.** Every two-vertex cutset in a finite triangle-free vertex-critical graph is a stable pair.

**Proof route.** A two-vertex clique cutset is forbidden by N14; hence the two vertices cannot be adjacent.

**Dependencies.** N14

**Novelty query.** `Independent Two-Cut in Triangle-Free Critical Graphs`

### Path Contacts

#### P01 — Consecutive Path Contacts Form an Induced Cycle
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `2/5`

**Statement.** Let P=v_0…v_{n-1} be an induced path and x∉V(P). If i<j are consecutive indices among the neighbors of x on P, then G[{x,v_i,…,v_j}] is an induced cycle C_{j-i+2}.

**Proof route.** The path segment is induced. By consecutive choice, x has no neighbor among its internal vertices, while xv_i and xv_j are edges.

**Novelty query.** `consecutive neighbors on induced path induce hole cycle lemma`

#### P02 — Triangle-Free Contact Gap
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `C`  
**Lean difficulty:** `1/5`

**Statement.** In a triangle-free graph, consecutive neighbor indices of an outside vertex on an induced path differ by at least 2.

**Proof route.** P01 would otherwise produce a 3-cycle.

**Dependencies.** P01

**Novelty query.** `Triangle-Free Contact Gap`

#### P03 — Square-Free Contact Gap
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `B`  
**Lean difficulty:** `1/5`

**Statement.** In a {C3,C4}-free graph, consecutive neighbor indices of an outside vertex on an induced path differ by at least 3.

**Proof route.** Use P01: gaps 1 and 2 produce induced C3 and C4 respectively.

**Dependencies.** P01

**Novelty query.** `Square-Free Contact Gap`

#### P04 — Forbidden-Hole Gap Dictionary
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `1/5`

**Statement.** If G has no induced cycle C_{d+2}, then no outside vertex has two consecutive contacts on an induced path at index gap d.

**Proof route.** This is exactly the contrapositive of P01.

**Dependencies.** P01

**Novelty query.** `induced path contact gap forbidden hole dictionary`

#### P05 — Fibonacci Contact-Signature Count
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `3/5`

**Statement.** For an n-vertex induced path P in a triangle-free graph, the neighborhood signature N(x)∩V(P) of an outside vertex is a subset with no consecutive path vertices. Hence at most F_{n+2} signatures are possible.

**Proof route.** P02 gives the no-consecutive condition. The number of independent sets of the n-vertex path satisfies a_n=a_{n-1}+a_{n-2}, a_0=1,a_1=2, hence a_n=F_{n+2}.

**Dependencies.** P02

**Novelty query.** `Fibonacci number attachment signatures induced path triangle-free graph`

#### P06 — d-Separated Contact-Code Recurrence
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `3/5`

**Statement.** If every consecutive pair of contacts must have index gap at least d≥2, then the number a_d(n) of possible signatures on an n-vertex path satisfies a_d(n)=a_d(n-1)+a_d(n-d), with the natural initial conditions.

**Proof route.** Partition signatures by whether the last path vertex is absent or present. If present, the preceding d-1 vertices are absent.

**Dependencies.** P04

**Novelty query.** `d separated binary contact signatures induced path recurrence`

#### P07 — Nonempty Signature Fibers Are Stable
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `1/5`

**Statement.** In a triangle-free graph, for a fixed induced path P and a fixed nonempty signature S⊆V(P), all outside vertices x with N(x)∩V(P)=S form a stable set.

**Proof route.** Any two such vertices share every vertex of S as a common neighbor; if adjacent, they form a triangle with one shared contact.

**Novelty query.** `contact signature fiber stable triangle-free graph`

#### P08 — Common-Contact Families Are Stable
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `C`  
**Lean difficulty:** `1/5`

**Statement.** For any fixed path vertex p, all outside vertices whose contact signature contains p form a stable set.

**Proof route.** They are all in N(p), which is stable by N01.

**Dependencies.** N01

**Novelty query.** `Common-Contact Families Are Stable`

#### P09 — Chromatic Bound for the Path-Contact Zone
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `B`  
**Lean difficulty:** `1/5`

**Statement.** If P has n vertices in a triangle-free graph, then the induced subgraph on all vertices having at least one neighbor in P has chromatic number at most n.

**Proof route.** Assign each contacting vertex to its first neighbor on P; each class lies in one stable neighborhood.

**Dependencies.** N02

**Novelty query.** `Chromatic Bound for the Path-Contact Zone`

#### P10 — Path-Anticomplete Chromatic Reserve
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `1/5`

**Statement.** If P is an induced path on n≥2 vertices in a triangle-free graph, then χ(G-N[P])≥χ(G)-n.

**Proof route.** P is connected and has no isolated vertices; apply N05.

**Dependencies.** N05

**Novelty query.** `Path-Anticomplete Chromatic Reserve`

#### P11 — Dominating Induced Path Bound
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `B`  
**Lean difficulty:** `1/5`

**Statement.** A triangle-free graph with a dominating induced path on n≥2 vertices has chromatic number at most n.

**Proof route.** Apply P10 with empty remainder, or N12.

**Dependencies.** P10

**Novelty query.** `Dominating Induced Path Bound`

#### P12 — Critical Path Escape Component
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `1/5`

**Statement.** If G is k-vertex-critical and triangle-free and P is an induced n-vertex path with 2≤n<k, then some component of G-N[P] has chromatic number at least k-n.

**Proof route.** This is N13 with H=P.

**Dependencies.** N13

**Novelty query.** `Critical Path Escape Component`

### Mixing And Spiders

#### M01 — First-Transition Arm Lemma
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `2/5`

**Statement.** If v is mixed on a connected vertex set C, then C contains adjacent vertices a,b such that va∈E and vb∉E. Consequently G[{v,a,b}] is an induced P3.

**Proof route.** Along a path in C from a neighbor of v to a nonneighbor, take the first edge crossing from N(v) to its complement.

**Novelty query.** `First-Transition Arm Lemma`

#### M02 — Mixed-Region Subdivided-Star Lemma
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `2/5`

**Statement.** If v is mixed on q pairwise anticomplete connected sets C_1,…,C_q, then G contains an induced once-subdivided K_{1,q} centered at v.

**Proof route.** Apply M01 in each C_i. Anticompleteness removes every cross-arm edge.

**Dependencies.** M01

**Novelty query.** `vertex mixed on anticomplete connected sets induced subdivided star`

#### M03 — Exact Mixing-Number Characterization
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `2/5`

**Statement.** Define μ_1(v) as the maximum q for which v is mixed on q pairwise anticomplete connected sets. Then μ_1(v) equals the maximum number of arms in an induced once-subdivided star centered at v.

**Proof route.** M02 proves one direction. For the converse, take each two-vertex arm of an induced subdivided star as one connected region.

**Dependencies.** M02

**Novelty query.** `mixing number equals maximum induced subdivided star arms`

#### M04 — Reach Arm Lemma
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `2/5`

**Statement.** Let C be connected and meet N(v). If z∈C has distance r≥1 in G[C] from N(v)∩C, then G contains an induced path v-a_0-a_1-…-a_r with all a_i∈C.

**Proof route.** Take a shortest path in C from N(v)∩C to z. It is induced; any edge from v to a later a_i would shorten the distance to N(v)∩C.

**Novelty query.** `Reach Arm Lemma`

#### M05 — Reach-Profile Spider Extraction
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `3/5`

**Statement.** Let C_1,…,C_q be pairwise anticomplete connected sets. If C_i contains a vertex at distance at least r_i≥1 from N(v)∩C_i, then G contains an induced spider centered at v with arm i of length r_i+1.

**Proof route.** Use M04 in each C_i and truncate to the prescribed reach. Pairwise anticompleteness removes cross-arm edges.

**Dependencies.** M04

**Novelty query.** `reach profile connected anticomplete regions induced spider characterization`

#### M06 — Exact Reach-Profile Equivalence
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `2/5`

**Statement.** For fixed positive integers r_1,…,r_q, the following are equivalent: (i) there exist pairwise anticomplete connected sets C_i with reach at least r_i from N(v)∩C_i; (ii) G contains an induced spider centered at v with arm lengths at least r_i+1.

**Proof route.** M05 gives (i)⇒(ii). For (ii)⇒(i), take each arm without the center as C_i.

**Dependencies.** M05

**Novelty query.** `exact equivalence induced spider reach profile mixed regions`

#### M07 — Excluded-Spider Mixing Bound
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `B`  
**Lean difficulty:** `1/5`

**Statement.** If G has no induced spider centered at v with q arms of lengths at least r_1+1,…,r_q+1, then no q pairwise anticomplete connected regions around v can have the corresponding reach profile.

**Proof route.** Contrapositive of M05.

**Dependencies.** M05

**Novelty query.** `Excluded-Spider Mixing Bound`

#### M08 — Shielded One-Step Extension
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `2/5`

**Statement.** Let H be an induced subgraph and u∈V(H). Let C be connected, disjoint from H, anticomplete to H\{u}, and suppose u is mixed on C. Then H can be extended by an induced two-edge arm u-a-b with a,b∈C.

**Proof route.** Use M01 inside C. Shielding removes chords to H\{u}.

**Dependencies.** M01

**Novelty query.** `Shielded One-Step Extension`

#### M09 — Shielded Reach-Profile Extension
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `3/5`

**Statement.** Let H be induced. For attachment vertices u_i∈V(H), let C_i be pairwise anticomplete connected sets, with C_i anticomplete to H\{u_i}, and with reach r_i from N(u_i)∩C_i. Then adjoining the extracted arms produces an induced extension of H by the prescribed pendant paths.

**Proof route.** Apply M04 independently. Shielding and pairwise anticompleteness eliminate all unwanted edges.

**Dependencies.** M04

**Novelty query.** `shielded connected region induced pendant path extension lemma`

#### M10 — Minimal-Separator Star Application
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `B`  
**Lean difficulty:** `1/5`

**Statement.** If a separator vertex s is mixed on q pairwise anticomplete connected components of G-S, then G contains an induced once-subdivided K_{1,q} centered at s.

**Proof route.** This is M02 applied to those components.

**Dependencies.** M02

**Novelty query.** `Minimal-Separator Star Application`

#### M11 — Two-Region Mixing Forces P5
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `B`  
**Lean difficulty:** `1/5`

**Statement.** If a vertex is mixed on two anticomplete connected sets, then G contains an induced P5.

**Proof route.** M02 with q=2 gives the path b_1-a_1-v-a_2-b_2.

**Dependencies.** M02

**Novelty query.** `Two-Region Mixing Forces P5`

#### M12 — Recursive Shielded Extension Theorem
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `4/5`

**Statement.** Let T be a rooted tree and H an induced copy of a rooted subtree T_0. Suppose every missing child-subtree is assigned a connected region that is shielded from H and from all other assigned regions, and recursively satisfies the same condition. Then G contains an induced copy of T extending H.

**Proof route.** Induct on the number of missing vertices, using M09 at the current frontier and preserving shielding for the recursive regions.

**Dependencies.** M09

**Novelty query.** `recursive shielded mixing induced tree extension theorem`

### Contamination Fans

#### C01 — Clean-Child or Large Fan Dichotomy
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `2/5`

**Statement.** Let G be triangle-free, u∈V(G), X⊆V(G)\N[u] finite and nonempty, and B⊆N(u). Then either some b∈B is anticomplete to X, or some x∈X has at least ⌈|B|/|X|⌉ neighbors in B; in the latter case {u,x} with those neighbors induces K_{2,m}.

**Proof route.** If no b is clean, assign each b one neighbor in X and pigeonhole. Use N10 for the induced fan.

**Dependencies.** N10

**Novelty query.** `clean child or K2m contamination fan pigeonhole lemma`

#### C02 — Fan-Free Dirty-Candidate Bound
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `1/5`

**Statement.** Under C01, if |N(u)∩N(x)∩B|≤m-1 for every x∈X, then at most (m-1)|X| vertices of B have a neighbor in X.

**Proof route.** Count incidences after assigning each dirty b to one contaminating x.

**Dependencies.** C01

**Novelty query.** `Fan-Free Dirty-Candidate Bound`

#### C03 — Weighted Contamination Fan Dichotomy
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `2/5`

**Statement.** Give each b∈B a nonnegative weight. If every positive-weight b has a neighbor in X, then some x∈X is adjacent to assigned candidates of total weight at least total_weight(B)/|X|.

**Proof route.** Assign each positive-weight candidate one contaminator and average the assigned weights.

**Novelty query.** `weighted contamination fan averaging lemma graph`

#### C04 — Depth-One Branch Immunity
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `C`  
**Lean difficulty:** `1/5`

**Statement.** In a triangle-free graph, two candidate children of the same vertex u are nonadjacent. Therefore a selected depth-one child cannot contaminate another depth-one child.

**Proof route.** Both candidates lie in the stable neighborhood N(u).

**Dependencies.** N01

**Novelty query.** `Depth-One Branch Immunity`

#### C05 — First Legal Contamination Is an Induced C4
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `1/5`

**Statement.** If u-a-x is an induced path and b∉{u,a,x} is adjacent to both u and x, then in a triangle-free graph the four vertices u,a,x,b induce C4.

**Proof route.** The cycle edges are present. The diagonals ux and ab are absent: ux by inducedness, ab because a,b∈N(u) and N(u) is stable.

**Dependencies.** N01

**Novelty query.** `first cross branch contamination induced C4 lemma`

#### C06 — Contamination-Cycle Generalization
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `1/5`

**Statement.** Let P=u=v_0-v_1-…-v_r=x be induced. If b∉V(P) is adjacent to u and x and has no neighbors among v_1,…,v_{r-1}, then V(P)∪{b} induces C_{r+2}.

**Proof route.** The path plus the two b-edges is a cycle, and the stated conditions remove every chord.

**Dependencies.** P01

**Novelty query.** `Contamination-Cycle Generalization`

### Pure Pairs

#### C07 — Complete-Pair Collapse in Triangle-Free Graphs
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `B`  
**Lean difficulty:** `1/5`

**Statement.** If nonempty disjoint sets A,B are complete to one another in a triangle-free graph, then both A and B are stable.

**Proof route.** An edge inside A together with any b∈B creates a triangle; similarly for B.

**Novelty query.** `Complete-Pair Collapse in Triangle-Free Graphs`

#### C08 — Clique-Sum Bound for Complete Pairs
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `C`  
**Lean difficulty:** `1/5`

**Statement.** In every graph, if A is complete to B, then ω(G[A])+ω(G[B])≤ω(G).

**Proof route.** A maximum clique in A and a maximum clique in B unite to a clique because the pair is complete.

**Novelty query.** `Clique-Sum Bound for Complete Pairs`

#### C09 — Clique-Sum Bound for Complete Blockades
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `B`  
**Lean difficulty:** `1/5`

**Statement.** If nonempty blocks B_1,…,B_r are pairwise complete, then Σ_i ω(G[B_i])≤ω(G).

**Proof route.** Choose a maximum clique from each block; their union is a clique.

**Dependencies.** C08

**Novelty query.** `Clique-Sum Bound for Complete Blockades`

#### C10 — Chromatic Thickness Ceiling
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `B`  
**Lean difficulty:** `1/5`

**Statement.** For every nonempty complete pair (A,B) in a triangle-free graph, min{χ(A),χ(B)}=1.

**Proof route.** C07 makes both sides stable and nonempty.

**Dependencies.** C07

**Novelty query.** `Chromatic Thickness Ceiling`

### Type-Uniform Tensor

#### T01 — Type-Tensor Diagonal Vanishing
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `3/5`

**Statement.** Let d≥3 and let a complete ordered d-ary rooted tree of height k be embedded path-induced, level-stable, and type-uniform in a triangle-free graph. For c<a,b≤k, let A_c(a,b)=1 when incomparable vertices of ordered type (a,b,c) are adjacent. Then A_c(a,a)=0 for every c<a≤k.

**Proof route.** Choose same-depth descendants in three distinct ordered child branches of a join at depth c. If A_c(a,a)=1, all three pairwise edges are present by type-uniformity, forming a triangle.

**Novelty query.** `type-uniform path-induced tree triangle-free diagonal type tensor zero`

#### T02 — First-Coordinate Parent Exclusion
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `3/5`

**Statement.** Let d≥3 and let a complete ordered d-ary rooted tree of height k be embedded path-induced, level-stable, and type-uniform in a triangle-free graph. For c<a,b≤k, let A_c(a,b)=1 when incomparable vertices of ordered type (a,b,c) are adjacent. If A_c(a,b)=1 and a-1>c, then A_c(a-1,b)=0.

**Proof route.** Take an adjacent parent-child pair at depths a-1,a in the earlier branch and a depth-b vertex in the later branch. If both type entries were active, these three vertices would form a triangle.

**Dependencies.** T01

**Novelty query.** `First-Coordinate Parent Exclusion`

#### T03 — Second-Coordinate Parent Exclusion
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `3/5`

**Statement.** Let d≥3 and let a complete ordered d-ary rooted tree of height k be embedded path-induced, level-stable, and type-uniform in a triangle-free graph. For c<a,b≤k, let A_c(a,b)=1 when incomparable vertices of ordered type (a,b,c) are adjacent. If A_c(a,b)=1 and b-1>c, then A_c(a,b-1)=0.

**Proof route.** Symmetric parent-child triangle argument in the later branch.

**Dependencies.** T01

**Novelty query.** `Second-Coordinate Parent Exclusion`

#### T04 — Grid-Independence of Active Types
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `2/5`

**Statement.** Let d≥3 and let a complete ordered d-ary rooted tree of height k be embedded path-induced, level-stable, and type-uniform in a triangle-free graph. For c<a,b≤k, let A_c(a,b)=1 when incomparable vertices of ordered type (a,b,c) are adjacent. For fixed c, the support {(a,b):A_c(a,b)=1} is an independent set in the Cartesian grid on depth pairs, where cells at Manhattan distance one are adjacent.

**Proof route.** T02 forbids vertically adjacent active cells and T03 forbids horizontally adjacent active cells.

**Dependencies.** T02, T03

**Novelty query.** `active type tensor support independent set grid triangle-free`

#### T05 — Exact Row Bound with Forced Diagonal Zero
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `3/5`

**Statement.** Let d≥3 and let a complete ordered d-ary rooted tree of height k be embedded path-induced, level-stable, and type-uniform in a triangle-free graph. For c<a,b≤k, let A_c(a,b)=1 when incomparable vertices of ordered type (a,b,c) are adjacent. Put n=k-c and index a,b by 1,…,n above c. In row a=i, the number of active entries is at most n/2 when n is even; when n is odd it is at most (n-1)/2 for odd i and (n+1)/2 for even i.

**Proof route.** The row is a binary string with no consecutive ones by T03 and with the diagonal position i forced to zero by T01. The stated bounds are the elementary maxima for such strings.

**Dependencies.** T01, T03

**Novelty query.** `Exact Row Bound with Forced Diagonal Zero`

#### T06 — Sharp Slice Active-Type Bound
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `3/5`

**Statement.** Let d≥3 and let a complete ordered d-ary rooted tree of height k be embedded path-induced, level-stable, and type-uniform in a triangle-free graph. For c<a,b≤k, let A_c(a,b)=1 when incomparable vertices of ordered type (a,b,c) are adjacent. For fixed join depth c and n=k-c, the number of active ordered types satisfies |supp(A_c)|≤⌊n²/2⌋.

**Proof route.** Sum the exact row bounds in T05. For even n the total is n²/2. For odd n, there are (n+1)/2 odd rows and (n-1)/2 even rows, giving (n²-1)/2.

**Dependencies.** T05

**Novelty query.** `sharp active type count type-uniform rooted tree triangle-free floor n squared over 2`

#### T07 — Total Active-Type Bound
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `3/5`

**Statement.** Let d≥3 and let a complete ordered d-ary rooted tree of height k be embedded path-induced, level-stable, and type-uniform in a triangle-free graph. For c<a,b≤k, let A_c(a,b)=1 when incomparable vertices of ordered type (a,b,c) are adjacent. Across all join depths, the total number of active ordered types is at most Σ_{n=1}^k⌊n²/2⌋. If k=2m this equals m(m+1)(4m-1)/3; if k=2m+1 it equals m(m+1)(4m+5)/3.

**Proof route.** Apply T06 to each c, where n=k-c, and evaluate the even/odd square sums.

**Dependencies.** T06

**Novelty query.** `total active type tensor bound rooted tree height formula`

#### T08 — Parity-Defect Host Construction
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `4/5`

**Statement.** On a complete rooted d-ary tree, keep all tree edges and add an edge between incomparable vertices exactly when their depths have opposite parity. The resulting graph is triangle-free, the rooted tree is path-induced, level-stable, and type-uniform.

**Proof route.** Root paths receive no added edges. Three incomparable vertices cannot be pairwise joined by the parity rule. A triangle containing a tree edge is impossible because the endpoints have opposite parity, so any third incomparable vertex is adjacent to exactly one endpoint.

**Novelty query.** `parity depth construction triangle-free type-uniform path-induced tree`

#### T09 — Sharpness of the Active-Type Bounds
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `2/5`

**Statement.** The parity-defect host T08 has A_c(a,b)=1 exactly when a and b have opposite parity. Hence every slice has ⌊(k-c)²/2⌋ active types and T06–T07 are sharp.

**Proof route.** Count opposite-parity ordered pairs among n depths: 2⌊n/2⌋⌈n/2⌉=⌊n²/2⌋.

**Dependencies.** T08

**Novelty query.** `sharpness active type tensor parity construction`

#### T10 — Type-Profile Determines the Defect Graph
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `2/5`

**Statement.** In a type-uniform copy, two target embeddings with identical ordered type for every incomparable target-vertex pair induce identical extra-edge patterns.

**Proof route.** Comparable target pairs are controlled by path-inducedness; incomparable adjacency is, by definition, a function only of ordered type.

**Novelty query.** `Type-Profile Determines the Defect Graph`

#### T11 — Sibling-Selection Sterility
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `1/5`

**Statement.** Changing only the identities of selected sibling branches, while preserving every target pair’s ordered depth/join type, cannot turn a non-induced target copy into an induced one.

**Proof route.** Immediate from T10: the defect graph is unchanged.

**Dependencies.** T10

**Novelty query.** `type-uniform sibling branch selection cannot remove defects`

#### T12 — Parity-Host Induced-Subtree Criterion
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `A`  
**Lean difficulty:** `2/5`

**Statement.** Inside the parity-defect host T08, a rooted subtree selected from the underlying tree is induced if and only if every pair of incomparable selected vertices has depths of the same parity.

**Proof route.** The only added edges join incomparable vertices of opposite depth parity, so the selected subtree has no defect exactly under the stated condition.

**Dependencies.** T08

**Novelty query.** `induced subtree criterion parity depth defect host`

## Finite theorem-search queue

### X01 — Extremizer Classification for T06
**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Priority:** `HIGH`

**Target.** Classify all type slices attaining ⌊n²/2⌋ active cells under diagonal-zero and parent-exclusion constraints; then impose the three-branch triangle constraints.

**Execution route.** SAT/ILP enumerate n≤10; infer and prove a structural classification.

### X02 — Local Constraints versus Global Tensor Realizability
**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Priority:** `HIGH`

**Target.** Determine whether every finite Boolean tensor satisfying T01–T03 and all three-branch triangle inequalities is realizable by a triangle-free type-uniform path-induced host.

**Execution route.** SAT graph realization with certificate; smallest counterexample if false.

### X03 — Minimum Defect-Free Depth Profile
**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Priority:** `HIGH`

**Target.** For each admissible tensor of height k, compute the largest set D of depths for which A_c(a,b)=0 on every ordered pair used by a specified target profile.

**Execution route.** MaxSAT, then exact small-k table and conjectured bound.

### X04 — Mixing Depth Census for Small Trees
**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Priority:** `MEDIUM`

**Target.** Define shielded mixing depth recursively and compute it for every unlabeled tree on at most 12 vertices.

**Execution route.** Enumerate trees and witness/counterwitness certificates.

### X05 — Reach-Profile Obstruction Basis
**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Priority:** `MEDIUM`

**Target.** For bounded arm lengths, find the minimal induced subgraphs that force μ_r(v) below q.

**Execution route.** Finite induced-subgraph enumeration.

### X06 — Depth-Two Path-Contact Signature Classification
**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Priority:** `HIGH`

**Target.** For a fixed first induced path P and candidate connected regions, classify uniform nonempty contact signatures that necessarily create a chosen two-branching tree.

**Execution route.** SAT over adjacency templates; certificate each forced tree.

### X07 — Fan Continuation Dichotomy
**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Priority:** `HIGH`

**Target.** For the smallest unresolved radius-three tree T*, find the least m,q such that every triangle-free graph with a K_{2,m} contamination fan and q-certified continuations contains T* or a bounded deletion certificate.

**Execution route.** SAT/CP-SAT finite schema search.

### X08 — Escape-Boundary Size Theorem
**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Priority:** `HIGH`

**Target.** In k-critical triangle-free graphs, experimentally minimize |N(C)| for the high-chromatic escape components from N15 as a function of k-|S|.

**Execution route.** Enumerate critical graphs / MILP; conjecture lower bound.

### X09 — Optimal Neighborhood Budget for Induced Trees
**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Priority:** `HIGH`

**Target.** For each finite tree H, determine the maximum χ(G[N[V(H)]]) over triangle-free hosts containing H induced.

**Execution route.** SAT coloring search; N04 gives upper bound |H|. Seek sharper tree-dependent values.

### X10 — Contact-Code Chromatic Compression
**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Priority:** `MEDIUM`

**Target.** Determine the maximum chromatic number of the union of selected nonempty path-signature fibers under forbidden-hole constraints.

**Execution route.** Finite signature conflict graph coloring.

### X11 — Parity-Host Obstruction Catalogue
**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Priority:** `HIGH`

**Target.** Classify rooted trees T that occur induced in every sufficiently large parity-defect host T08.

**Execution route.** Dynamic programming on depth-parity assignments.

### X12 — New Tree-Family Separator Purity
**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Priority:** `HIGH`

**Target.** Use M09/M12 and finite path-contact signatures to identify the first tree family beyond known subdivided-star/multibroom cases for which separator mixing forces an induced member.

**Execution route.** Enumerate tree shapes; novelty filter; formal proof from signature cases.

## Promotion contract
A claim moves from this bank to a theorem receipt only after: (1) exact statement hash frozen; (2) Lean or an independent finite certificate passes; (3) novelty checker is run on the exact statement and nearest equivalent formulations; (4) known/novel status is recorded separately from mathematical truth; and (5) any theorem using the type-uniform framework explicitly states that framework as a hypothesis rather than silently importing the open conjecture.

## Accompanying executable receipts
- `verify_erdos738_theorem_bank.py` independently exhausts selected local claims on all triangle-free graphs through five vertices, checks the no-clique-cutset theorem on all graphs through six vertices, and verifies the parity-defect host for ternary trees through height four.
- `ERDOS-738-THEOREM-BANK-VERIFICATION.json` records the passing assertion counts and parameters.
- `ERDOS-738-THEOREM-BANK-MANIFEST.json` binds the artifact hashes and preserves the claim boundary.
