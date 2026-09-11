# Erdős #738 × Erdős #595 Cross-Encirclement Theorem Forge
## Ordered links, cone transfer, layer-defect descent, transversal absorption, and dual migration

**Date:** 2026-08-04  
**Mode:** Cross-campaign RSI / theorem-mining pass  
**Source campaigns:** Erdős #738 triangle-free induced-tree campaign and Erdős #595 K₄-free triangle-cover campaign  
**Novelty status:** **UNRUN** — all historical novelty labels belong to the local novelty checker  
**Lean status:** **UNRUN** — Lean names are formalization missions, not receipts  

---

## 0. Claim boundary

This artifact does not claim either flagship is solved. It cross-compiles the two
campaigns under the Encirclement constitution:

- exact statements rather than thematic analogies;
- Search/Court separation;
- proof routes and falsifiers for every promoted claim;
- conditional labels whenever Erdős #738 is used;
- explicit negative theorems when a tempting bridge is sterile;
- executable finite targets and forced-close programs.

The central collision is:

> Erdős #595 forces an uncountably chromatic triangle-free **vertex link** inside
> every hypothetical witness, while Erdős #738 is precisely a theory of induced
> finite trees and chromatic escape inside triangle-free graphs.

This makes every #595 witness contain a live #738 campaign inside one neighborhood.
But the cone over that neighborhood is always two-layer coverable, so the true
#595 obstruction must migrate into interactions among uncountably many links.

---

## 1. Source-bound notation

- \(tc(G)\): least cardinality of a cover of \(E(G)\) by triangle-free subgraphs.
- \(N_\prec^+(v)\): neighbors of \(v\) later than \(v\) in a well-order \(\prec\).
- \(K_1\vee H\): the cone over \(H\).
- \(itc_T(G)\): least size of a cover by layers that are triangle-free and induced-\(T\)-free.
- A **layer-induced** tree is induced inside one cover layer; its **ambient defect graph**
  consists of extra edges among its vertices in the union graph.
- A **critical bouquet** is a cone over pairwise anticomplete finite
  triangle-free critical blocks of unbounded chromatic number.

---

## 2. Highest-value cross-campaign results

1. **Ordered forward-link coloring:** \(tc(G)\) is bounded by the largest chromatic
   number of a forward neighborhood.
2. **Witness link theorem:** every #595 witness contains an uncountably chromatic
   triangle-free forward link under every vertex well-order.
3. **Cone transfer:** a χ-bound for triangle-free induced-\(T\)-free graphs converts
   directly into a triangle-cover bound for K₄-free induced-cone-\(T\)-free graphs.
4. **Conditional cone universality:** #738(T) would force every #595 witness to
   contain an induced cone over \(T\).
5. **Critical bouquet:** every #595 witness contains an induced cone over
   pairwise anticomplete finite critical triangle-free graphs of unbounded chromatic number.
6. **Dual migration:** that entire bouquet still has \(tc=2\); the #595 obstruction
   must live in cross-link interactions outside the obvious high-chromatic core.
7. **Layer-defect descent:** a tree induced in one of \(m\) triangle-free layers
   has ambient defects covered by only \(m-1\) layers.
8. **Maximal-layer interface:** #595 is equivalent to the failure of every
   countable family of maximal triangle-free spanning subgraphs to cover the edges.
9. **Transversal absorption:** under #738(T), every high-chromatic triangle-free
   residual after a triangle transversal contains a copy of \(T\) whose ambient
   chords are absorbed by that transversal.

---


## A — Ordered links


                ### XLINK01 — Ordered Forward-Link Coloring Theorem

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `100/100`  
                **Claim hash:** `50db7ddc38bfe249bac0c9ba4dd907ce4cd6bc2cc06a46853091ebc2ab69f9c1`

                **Statement.** Let \(G\) be a graph and \(\prec\) a well-order of \(V(G)\). For each vertex \(v\), put
\(N_\prec^+(v)=\{w\in N(v):v\prec w\}\). If
\(\chi(G[N_\prec^+(v)])\le \kappa\) for every \(v\), then \(tc(G)\le\kappa\).

                **Proof route.** Choose a proper \(\kappa\)-coloring \(\varphi_v\) of every forward neighborhood.
For an edge \(vw\) with \(v\prec w\), color \(vw\) by \(\varphi_v(w)\).
In a triangle \(v\prec w\prec x\), the vertices \(w,x\) are adjacent in
\(G[N_\prec^+(v)]\), so \(vw\) and \(vx\) receive different colors.

                **Falsifier.** A graph/order with all forward links κ-colorable but no κ-color nonmonochromatic triangle edge-coloring.

                **Lean mission.** `triangleCover_le_forwardLinkChromatic`

                **Novelty query.** `"forward neighborhood" chromatic number edge coloring no monochromatic triangle`


                ### XLINK02 — Ordered Link Parameter Upper Bound

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `92/100`  
                **Claim hash:** `c45168c0b6a69e13ee2bb143ac604972ca87d081e8340cfcd466951c9e62b53c`

                **Statement.** Define
\[
\lambda_\triangle(G)=\min_{\prec}\sup_{v\in V(G)}
\chi(G[N_\prec^+(v)]),
\]
where the minimum ranges over well-orders of \(V(G)\). Then
\(tc(G)\le\lambda_\triangle(G)\).

                **Proof route.** Apply XLINK01 to every well-order and minimize.

                **Falsifier.** A graph with triangle-cover number larger than the defined ordered-link parameter.

                **Lean mission.** `triangleCover_le_orderedLinkParameter`

                **Novelty query.** `"ordered local chromatic number" triangle cover parameter`


                ### XLINK03 — Full-Neighborhood Chromatic Bound

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `100/100`  
                **Claim hash:** `7a3b497449a607e2cd559289e751d83c06ede53f8518889c2973d9a8a2f9e0e9`

                **Statement.** For every graph \(G\),
\[
tc(G)\le \sup_{v\in V(G)}\chi(G[N(v)]).
\]

                **Proof route.** Every forward neighborhood is an induced subgraph of the full neighborhood; combine with XLINK01.

                **Falsifier.** A graph whose triangle-cover number exceeds the chromatic number of every neighborhood.

                **Lean mission.** `triangleCover_le_iSup_neighborhoodChromatic`

                **Novelty query.** `"triangle cover number" neighborhood chromatic number`


                ### XLINK04 — High-Cover Forward-Link Obstruction

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `100/100`  
                **Claim hash:** `83044473fe689f5b85822bfc3f4533912883f56dadbcb046fe84f25afb5211c9`

                **Statement.** If \(tc(G)>\kappa\), then for every well-order \(\prec\) of \(V(G)\) there is
a vertex \(v\) with
\[
\chi(G[N_\prec^+(v)])>\kappa.
\]

                **Proof route.** Contrapositive of XLINK01.

                **Falsifier.** A well-order of a \(tc>\kappa\) graph whose every forward link is κ-colorable.

                **Lean mission.** `triangleCover_gt_forces_highChromatic_forwardLink`

                **Novelty query.** `"uncountable triangle cover" high chromatic forward neighborhood`


                ### XLINK05 — K4-Free Links Are Triangle-Free

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `95/100`  
                **Claim hash:** `1dda15a9d87b8a3274083b3098e88d1a8ebfe44b0911cee8e63c815be4d3939e`

                **Statement.** If \(G\) is \(K_4\)-free, then \(G[N(v)]\) is triangle-free for every vertex \(v\).
The same holds for every forward link \(G[N_\prec^+(v)]\).

                **Proof route.** A triangle inside \(N(v)\), together with \(v\), is a \(K_4\).

                **Falsifier.** A K4-free graph with a triangle in a vertex neighborhood.

                **Lean mission.** `K4free_neighborhood_triangleFree`

                **Novelty query.** `"K4-free" neighborhood triangle-free`


                ### XLINK06 — Erdős #595 Link Theorem

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `100/100`  
                **Claim hash:** `ef5be9b0724642cd4193437e57095abe8bea2b9a069d32650786a2d4bd3f5e29`

                **Statement.** Every \(K_4\)-free graph \(G\) with \(tc(G)>\aleph_0\) has the following property:
for every well-order of \(V(G)\), some forward neighborhood is an
uncountably chromatic triangle-free induced subgraph.

                **Proof route.** Combine XLINK04 with κ=ℵ₀ and XLINK05.

                **Falsifier.** A #595 witness and a well-order with no uncountably chromatic forward link.

                **Lean mission.** `erdos595_everyOrder_has_uncountablyChromatic_triangleFreeLink`

                **Novelty query.** `"Erdos 595" uncountably chromatic neighborhood triangle-free`


                ### XLINK07 — Finite High-Cover Link Extraction

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `97/100`  
                **Claim hash:** `a8f81d7346d1697526741e26cab25c8f07c788d941700b99637b06a8e8393870`

                **Statement.** If \(G\) is finite, \(K_4\)-free, and \(tc(G)>k\), then some vertex \(v\) has a
triangle-free neighborhood with chromatic number greater than \(k\).
The neighborhood may be replaced by a forward neighborhood for any prescribed vertex order.

                **Proof route.** Use XLINK04 with the prescribed order and XLINK05.

                **Falsifier.** A finite K4-free graph with tc>k but every neighborhood k-colorable.

                **Lean mission.** `finite_highTriangleCover_extracts_highChromatic_link`

                **Novelty query.** `"finite K4-free" triangle cover high chromatic neighborhood`


                ### XLINK08 — Closed-Neighborhood Two-Layer Theorem

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `91/100`  
                **Claim hash:** `d40e6f9f3f3af7a083d353aa722edc2d0ec026d1a2bb42e04903098ff0b216d6`

                **Statement.** For every \(K_4\)-free graph \(G\) and vertex \(v\),
\[
tc(G[N[v]])\le 2.
\]
It equals \(2\) exactly when \(G[N(v)]\) contains an edge, and is at most \(1\) otherwise.

                **Proof route.** Split the closed-neighborhood edges into the star at v and the triangle-free link G[N(v)].

                **Falsifier.** A K4-free closed neighborhood requiring three triangle-free layers.

                **Lean mission.** `K4free_closedNeighborhood_triangleCover_le_two`

                **Novelty query.** `"K4-free" closed neighborhood two triangle-free layers`


                ### XLINK09 — Closed-Neighborhood Edge-Cover Bound

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `90/100`  
                **Claim hash:** `621cc3e0bcfd954595518ea8a88a6c930cdeb2f8904ee60d9d26a185433559a8`

                **Statement.** Let \(\ell(G)\) be the least cardinality of a set \(S\subseteq V(G)\) such that
\[
E(G)=\bigcup_{s\in S}E(G[N[s]]).
\]
If \(G\) is \(K_4\)-free, then \(tc(G)\le 2\ell(G)\) in cardinal arithmetic.

                **Proof route.** Apply XLINK08 to each closed-neighborhood piece and union subadditivity.

                **Falsifier.** A K4-free graph violating the inherited 2·ℓ layer cover.

                **Lean mission.** `triangleCover_le_two_mul_closedNeighborhoodEdgeCover`

                **Novelty query.** `"closed neighborhood cover number" K4-free triangle cover`


                ### XLINK10 — Vertex-Cover Bound for K4-Free Graphs

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `84/100`  
                **Claim hash:** `1ba5dd03998c074cc3b89673a44c65f68c09a2217eeef817a7ccbf855d3c2f21`

                **Statement.** If \(S\) is a vertex cover of a \(K_4\)-free graph \(G\), then
\[
tc(G)\le 2|S|.
\]
Consequently, a \(K_4\)-free graph with a countable vertex cover is countably
triangle-decomposable.

                **Proof route.** Every edge has an endpoint s in S and therefore lies in G[N[s]]; apply XLINK09.

                **Falsifier.** A K4-free graph with a vertex cover S but triangle-cover number above 2|S|.

                **Lean mission.** `K4free_triangleCover_le_two_mul_vertexCover`

                **Novelty query.** `"vertex cover" K4-free triangle-free edge decomposition`


                ### XLINK11 — Witness Link-Cover Dispersion

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `91/100`  
                **Claim hash:** `d7b194bb846b69cef699c4597c39d48416180dab63cf9628a631254f0bf494ff`

                **Statement.** Every Erdős #595 witness has uncountable closed-neighborhood edge-cover number
\(\ell(G)\), and in particular has no countable vertex cover.

                **Proof route.** Contrapositive of XLINK09 and XLINK10.

                **Falsifier.** A #595 witness whose edges are covered by countably many closed neighborhoods.

                **Lean mission.** `erdos595_closedNeighborhoodCover_uncountable`

                **Novelty query.** `"Erdos 595" countable vertex cover obstruction`


                ### XLINK12 — Localization–Dispersion Dichotomy

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `98/100`  
                **Claim hash:** `6792eb8338ca7fc47ee1037b56627210ecc1a6576524857f4767273a413ce49c`

                **Statement.** Every Erdős #595 witness simultaneously has:
(i) an uncountably chromatic triangle-free forward link under every well-order; and
(ii) no countable family of closed neighborhoods covering all its edges.
Thus high vertex-chromatic complexity localizes in a link, while triangle-cover
complexity is necessarily dispersed across uncountably many links.

                **Proof route.** Combine XLINK06 and XLINK11.

                **Falsifier.** A witness failing either exact component.

                **Lean mission.** `erdos595_localization_dispersion_dichotomy`

                **Novelty query.** `"local chromatic complexity" "triangle cover" dispersion K4-free`


                ### XLINK13 — Finite Critical Link Extraction

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `94/100`  
                **Claim hash:** `a3b79bb45384f8b262a0fdede88dc8c70580a33d23ac85d4d2c226b34edeefbc`

                **Statement.** If \(G\) is finite, \(K_4\)-free, and \(tc(G)>k\), then \(G\) contains an induced
cone over a finite triangle-free vertex-critical graph \(Q\) with \(\chi(Q)>k\).

                **Proof route.** Use XLINK07 to obtain a triangle-free link of chromatic number >k, then choose an induced vertex-minimal subgraph Q retaining chromatic number >k; add the apex.

                **Falsifier.** A high-cover finite K4-free graph with no such critical link cone.

                **Lean mission.** `finite_highCover_contains_cone_criticalTriangleFree`

                **Novelty query.** `"K4-free Folkman graph" critical neighborhood cone`


                ### XLINK14 — Critical Bouquet Theorem

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `99/100`  
                **Claim hash:** `76daab2bb7dd4eac4be064fad4f585bf87a2575dcbb6c1a2778d5f2a9ef42a75`

                **Statement.** Every Erdős #595 witness contains an induced subgraph
\[
K_1\vee\Bigl(\bigsqcup_{n<\omega}Q_n\Bigr),
\]
where the \(Q_n\) are pairwise anticomplete finite triangle-free vertex-critical
graphs and \(\chi(Q_n)>n\).

                **Proof route.** Use XLINK06 to obtain an infinite-chromatic triangle-free link H at an apex v.
Choose a finite critical Q_0 of chromatic number >0. After choosing Q_n, delete
its closed neighborhood inside the current triangle-free residual. The protected
deletion lemma from the #738 bank preserves infinite chromatic number. Repeat.
Later blocks are anticomplete to earlier blocks; add v.

                **Falsifier.** A witness in which the protected recursive extraction fails at a finite stage.

                **Lean mission.** `erdos595_contains_induced_criticalBouquet`

                **Novelty query.** `"critical bouquet" uncountably chromatic neighborhood K4-free`


                ### XLINK15 — Critical Bouquet Sterility

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `88/100`  
                **Claim hash:** `f85d38be6497f4ca537dfce05432e6de2aa25d8bcb286f37c911c36ab150c652`

                **Statement.** For any family of pairwise anticomplete triangle-free graphs \(Q_i\), the cone
\[
K_1\vee\bigsqcup_i Q_i
\]
has triangle-cover number at most \(2\), and equals \(2\) when some \(Q_i\) has an edge.

                **Proof route.** Put all apex edges in one layer and all internal block edges in the other.

                **Falsifier.** A cone bouquet requiring more than two triangle-free layers.

                **Lean mission.** `cone_disjointTriangleFreeBlocks_triangleCover_two`

                **Novelty query.** `"cone over disjoint triangle-free graphs" triangle cover two`


## B — Cone transfer


                ### XCONE01 — Induced Cone Lift

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `89/100`  
                **Claim hash:** `d442503b45cd06f4df29e231d847d67b8ff43caedc97114b0f50ae57dc9b534c`

                **Statement.** If \(F\) is an induced subgraph of \(G[N(v)]\), then \(G[\{v\}\cup V(F)]\)
is the induced cone \(K_1\vee F\).

                **Proof route.** The apex v is adjacent to every vertex of its neighborhood, and the edges inside F are unchanged.

                **Falsifier.** An induced link copy whose apex lift has a missing apex edge or an extra internal edge.

                **Lean mission.** `inducedSubgraph_link_lifts_to_cone`

                **Novelty query.** `"induced cone" neighborhood graph`


                ### XCONE02 — χ-Bounded Cone-Transfer Principle

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `100/100`  
                **Claim hash:** `2e4f6802ec4f6fe8fc2ddcba447f8e813895ddf76e7657c39fd51b1ded69342d`

                **Statement.** Let \(\mathcal F\) be a family of triangle-free graphs. Suppose every
triangle-free graph containing no induced member of \(\mathcal F\) has chromatic
number at most \(\kappa\). Then every \(K_4\)-free graph containing no induced
cone \(K_1\vee F\) with \(F\in\mathcal F\) satisfies \(tc(G)\le\kappa\).

                **Proof route.** Every neighborhood is triangle-free and F-free by XCONE01; apply XLINK03.

                **Falsifier.** A cone-F-free K4-free graph with tc>κ despite the assumed χ-bound.

                **Lean mission.** `chiBounded_family_coneTransfer_triangleCover`

                **Novelty query.** `"chi-bounded" triangle-free class induced cone triangle cover`


                ### XCONE03 — Erdős #738-to-#595 Tree-Cone Transfer

                **Status:** `CONDITIONAL_ON_738_T`  
                **Structural leverage:** `100/100`  
                **Claim hash:** `71d0baaf07fa2af622757d5176f20bd8160ad20958097287508d26345e87a46c`

                **Statement.** Fix a finite tree \(T\). If every triangle-free induced-\(T\)-free graph is
\(c(T)\)-colorable, then every \(K_4\)-free induced-\((K_1\vee T)\)-free graph
has \(tc(G)\le c(T)\).

                **Proof route.** Specialize XCONE02 to the one-element family {T}.

                **Falsifier.** A verified #738 bound together with a K4-free cone-T-free graph of larger triangle-cover number.

                **Lean mission.** `gyarfasSumner_triangleFree_implies_coneTriangleCoverBound`

                **Novelty query.** `"induced tree" cone K4-free triangle cover number`


                ### XCONE04 — Cone-Free High-Cover Counterexample Extractor

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `100/100`  
                **Claim hash:** `7c533ff700a3a54891a62d20594d4631a292f565074a4264a6f02e79e87c1fbb`

                **Statement.** If a finite \(K_4\)-free induced-\((K_1\vee T)\)-free graph has \(tc(G)>k\),
then it contains a triangle-free induced-\(T\)-free neighborhood of chromatic
number greater than \(k\).

                **Proof route.** Use XLINK07. Cone-freeness forces every extracted neighborhood to be T-free.

                **Falsifier.** A high-cover cone-T-free graph whose every link is k-colorable or contains T.

                **Lean mission.** `coneFree_highCover_extracts_treeFree_highChromatic_link`

                **Novelty query.** `"cone-free K4-free" high triangle cover induced tree-free neighborhood`


                ### XCONE05 — Conditional Cone Universality of #595 Witnesses

                **Status:** `CONDITIONAL_ON_738_T`  
                **Structural leverage:** `100/100`  
                **Claim hash:** `48ed181299d6a22347c5e58b8cfb01b2ef817c6a0b35237eeae9b0b0eb0aad72`

                **Statement.** If the triangle-free Gyárfás–Sumner statement holds for a finite tree \(T\),
then every Erdős #595 witness contains an induced \(K_1\vee T\).

                **Proof route.** A witness has tc>ℵ₀, hence exceeds the finite bound c(T); apply the contrapositive of XCONE03.

                **Falsifier.** A #595 witness avoiding the cone despite a verified finite #738 bound.

                **Lean mission.** `erdos595_witness_contains_cone_of_tree`

                **Novelty query.** `"Erdos 595 witness" induced cone over every finite tree`


                ### XCONE06 — Conditional Forest-Bouquet Universality

                **Status:** `CONDITIONAL_ON_738_SEQUENCE`  
                **Structural leverage:** `97/100`  
                **Claim hash:** `1c149e39fff2cc24f65a6d384bcda878fcb286b042e919b29051c5e035a953a1`

                **Statement.** Assume the triangle-free Gyárfás–Sumner statement for each tree in a sequence
\(T_0,T_1,\dots\), where every \(T_i\) has at least two vertices. Then every
#595 witness contains an induced
\[
K_1\vee\bigsqcup_{i<\omega}T_i.
\]

                **Proof route.** Inside the infinite-chromatic triangle-free link from XLINK06, recursively find T_i and delete its closed neighborhood. The #738 protected-deletion lemma keeps the residual infinitely chromatic and makes the copies pairwise anticomplete.

                **Falsifier.** A witness or sequence for which the recursive protected extraction fails.

                **Lean mission.** `erdos595_contains_cone_over_tree_sequence`

                **Novelty query.** `"cone over countable forest" K4-free witness induced`


                ### XCONE07 — All-Finite-Trees Bouquet Consequence

                **Status:** `CONDITIONAL_ON_FULL_738`  
                **Structural leverage:** `96/100`  
                **Claim hash:** `c35ccc2b5ec9416834eb8ebc3e23be8d59a73fdc8a6c1e1e7094a478151616d3`

                **Statement.** If Erdős #738 holds for every finite tree, then every #595 witness contains an
induced cone over a countable forest containing one component isomorphic to
every finite tree.

                **Proof route.** Enumerate the finite trees and apply XCONE06.

                **Falsifier.** A full #738 proof and a #595 witness lacking the enumerating bouquet.

                **Lean mission.** `full738_implies_595_universalTreeBouquet`

                **Novelty query.** `"all finite trees" induced cone bouquet Erdős 595`


                ### XCONE08 — Cone Sterility Theorem

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `94/100`  
                **Claim hash:** `b028f729e2dcc487528215f61d799319187b9d9476e7166fe56571a916d71eb5`

                **Statement.** For every triangle-free graph \(H\) with at least one edge,
\(K_1\vee H\) is \(K_4\)-free and has \(tc=2\), regardless of \(\chi(H)\)
or the induced-tree complexity of \(H\).

                **Proof route.** K4-freeness follows because H has no triangle. Two layers are the apex star and H; a triangle forces the lower bound two.

                **Falsifier.** A triangle-free H whose cone contains K4 or needs more than two layers.

                **Lean mission.** `cone_triangleFree_K4free_triangleCover_eq_two`

                **Novelty query.** `"cone of high chromatic triangle-free graph" triangle cover two`


                ### XCONE09 — Type-Tensor Extremality Is Triangle-Cover Sterile

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `87/100`  
                **Claim hash:** `43abcff75dc7f3c6f0a10d286e773b708b6e3fb668d461925de57bfd2ef1f839`

                **Statement.** Coning the parity-defect hosts from the #738 type-tensor package produces
\(K_4\)-free graphs with sharp/extremal type-defect tensors in their links but
triangle-cover number exactly \(2\).

                **Proof route.** The parity-defect host is triangle-free by the #738 bank; apply XCONE08.

                **Falsifier.** A parity-host cone whose cover number exceeds two.

                **Lean mission.** `parityTensor_cone_triangleCover_two`

                **Novelty query.** `"parity defect host" cone triangle cover`


                ### XCONE10 — Local-Complexity Non-Sufficiency

                **Status:** `REFUTED_ROUTE`  
                **Structural leverage:** `93/100`  
                **Claim hash:** `7dd65d9ef017adb55ec432740280b96830f6ca14ff6f1573317e9b0ede25a116`

                **Statement.** No lower bound on the chromatic number, criticality, induced-tree richness, or
type-tensor complexity of a single \(K_4\)-free vertex link can by itself imply
\(tc(G)>2\).

                **Proof route.** XCONE08 realizes arbitrary triangle-free link complexity inside a two-layer cone.

                **Falsifier.** A proposed single-link invariant that excludes all cone examples and still claims universality.

                **Lean mission.** `singleLinkComplexity_not_sufficient_for_highTriangleCover`

                **Novelty query.** `"local link complexity" insufficient triangle cover cone counterexample`


## C — Layer hierarchy


                ### XLAYER01 — Tree-Rich Layer Product Theorem

                **Status:** `CONDITIONAL_ON_738_T`  
                **Structural leverage:** `96/100`  
                **Claim hash:** `e79779ab3472952c72c429a665e6afb545972ce066f81e910fd152099552e2c6`

                **Statement.** Fix a finite tree \(T\) and suppose every triangle-free induced-\(T\)-free graph
is \(c\)-colorable. If
\(E(G)=\bigcup_{i<m}E(H_i)\) with every \(H_i\) triangle-free and induced-\(T\)-free,
then \(\chi(G)\le c^m\).

                **Proof route.** Properly c-color each H_i and take the product coloring of their vertex colorings.

                **Falsifier.** An m-layer cover violating the product coloring.

                **Lean mission.** `treeFree_triangleLayerCover_chromatic_pow_bound`

                **Novelty query.** `"induced T-free triangle-free layers" product chromatic bound`


                ### XLAYER02 — Finite-Layer Forced-Tree Corollary

                **Status:** `CONDITIONAL_ON_738_T`  
                **Structural leverage:** `98/100`  
                **Claim hash:** `2bae11e04ea67c19aaaa48e817a4183f722f984f14240a30331dd3882d7ac05f`

                **Statement.** Under the same #738(T) hypothesis, if \(G\) has a cover by \(m\) triangle-free
subgraphs and \(\chi(G)>c(T)^m\), then every such cover has at least one layer
containing an induced \(T\).

                **Proof route.** Contrapositive of XLAYER01.

                **Falsifier.** A high-chromatic m-cover whose every layer is induced-T-free.

                **Lean mission.** `highChromatic_finiteTriangleCover_forces_treeInLayer`

                **Novelty query.** `"finite triangle-free edge cover" layer contains induced tree`


                ### XLAYER03 — Countable-Layer Forced-Tree Corollary

                **Status:** `CONDITIONAL_ON_738_T`  
                **Structural leverage:** `91/100`  
                **Claim hash:** `694543d0056f1f24197ba4c68ca4baada8cd307452bf38ec7014f4fce9419477`

                **Statement.** Under #738(T), if \(G\) is countably covered by triangle-free subgraphs and
\(\chi(G)>c(T)^{\aleph_0}\), then every countable cover has a layer containing
an induced \(T\).

                **Proof route.** Countable product version of XLAYER01.

                **Falsifier.** A countable cover of a graph above the product bound with every layer T-free.

                **Lean mission.** `countableTriangleCover_highChromatic_forces_treeLayer`

                **Novelty query.** `"countable triangle-free cover" induced tree layer product`


                ### XLAYER04 — Ambient Defect-Layer Inheritance

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `100/100`  
                **Claim hash:** `7dd6976d75ff71e6ab204d3757b7700ee43b7c3b30fdfe04ad657d623dc5b238`

                **Statement.** Suppose \(G=\bigcup_{i<m}H_i\), each \(H_i\) is triangle-free, and
\(H_j[X]\) is an induced copy of a tree \(T\). Then every ambient extra edge in
\(G[X]\setminus E(T)\) is covered by the other \(m-1\) layers. Hence the ambient
defect graph on \(X\) has triangle-cover number at most \(m-1\).

                **Proof route.** An extra edge is absent from H_j by inducedness, so it must occur in another covering layer.

                **Falsifier.** An ambient defect edge belonging only to the tree layer.

                **Lean mission.** `layerInducedTree_defectCover_descends`

                **Novelty query.** `"induced tree in one layer" ambient defect graph remaining layers`


                ### XLAYER05 — Defect-Depth Descent

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `97/100`  
                **Claim hash:** `8ecd80666a008c7e021b7c8c6a429b587094cabc045467392a4f416c1b6b4e94`

                **Statement.** In an \(m\)-layer triangle-free cover, every tree induced in one layer has an
ambient defect graph of cover depth at most \(m-1\). Therefore ambient
purification can be organized as an induction on layer depth, with \(m=1\)
as the exact induced base case.

                **Proof route.** Repackage XLAYER04 as an inductive invariant.

                **Falsifier.** A layer-induced tree whose ambient defect graph requires m or more layers.

                **Lean mission.** `ambientTreeDefect_depth_lt_coverDepth`

                **Novelty query.** `"layer depth induction" induced tree purification defects`


                ### XLAYER06 — Induced-Tree-Free Layer-Cover Bound

                **Status:** `CONDITIONAL_ON_738_T`  
                **Structural leverage:** `90/100`  
                **Claim hash:** `80ddf577559ebb577e3cd8dbda5060fdbb04b6cd4b475a870531c1d782d14486`

                **Statement.** Let \(itc_T(G)\) be the least cardinality of a cover of \(E(G)\) by subgraphs
that are both triangle-free and induced-\(T\)-free. Under #738(T) with bound c,
\[
\chi(G)\le c^{\,itc_T(G)}.
\]

                **Proof route.** Apply the product-coloring lemma to a minimum such cover.

                **Falsifier.** A cover by induced-T-free triangle-free layers violating the product bound.

                **Lean mission.** `inducedTreeFreeTriangleCover_productBound`

                **Novelty query.** `"induced-tree-free layer cover number" chromatic`


                ### XLAYER07 — Induced-Free Refinement Failure

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `85/100`  
                **Claim hash:** `456f3e6056860d0afb6fed00df2704ff4d4d526caf1b59f70af74bd9d442335b`

                **Statement.** The cover-to-partition refinement used for ordinary triangle-free layers does
not extend to induced-tree-free layers in general. Specifically, \(C_4\) is
triangle-free and induced-\(P_4\)-free, while deleting one edge produces an
induced \(P_4\).

                **Proof route.** The displayed four-vertex example is an explicit counterexample to downward closure under edge deletion.

                **Falsifier.** A claim that every subgraph of an induced-P4-free triangle-free graph remains induced-P4-free.

                **Lean mission.** `inducedTreeFree_cover_refinement_failure_P4`

                **Novelty query.** `"induced P4-free" edge deletion creates P4 C4`


                ### XLAYER08 — No Automatic Blocker Duality for \(itc_T\)

                **Status:** `REFUTED_ROUTE`  
                **Structural leverage:** `82/100`  
                **Claim hash:** `ae41b5ae5c353f950e726139a01722a5a03aefb4902faa9de6c275f45f3445d0`

                **Statement.** Because induced-\(T\)-freeness is not generally preserved by deleting edges,
the blocker-centeredness duality and least-layer partition refinement for
\(tc(G)\) cannot be imported unchanged to \(itc_T(G)\).

                **Proof route.** XLAYER07 kills the required downward-closure step.

                **Falsifier.** A valid general refinement theorem overcoming the explicit C4/P4 obstruction.

                **Lean mission.** `no_naive_blockerDuality_inducedTreeFreeLayers`

                **Novelty query.** `"blocker duality" induced subgraph forbidden layer cover refinement`


                ### XLAYER09 — Hereditary Edge-Deletion Layer Refinement

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `76/100`  
                **Claim hash:** `82d878650cb34ed5db5064803fbf529a225e37f6a1298b0fdb6f3fa557ba40db`

                **Statement.** For any class of edge sets closed under taking subsets, every cover by
\(\kappa\) members of the class refines to a partition by \(\kappa\) members.
In particular, covers by triangle-free and non-induced-\(T\)-subgraph-free
layers refine to partitions.

                **Proof route.** Assign each edge to its least covering layer; subset closure preserves membership.

                **Falsifier.** A subset-closed class for which least-layer refinement leaves the class.

                **Lean mission.** `subsetClosed_layerCover_refines_partition`

                **Novelty query.** `"subset closed graph property" edge cover partition refinement`


                ### XLAYER10 — Finite-Layer Gyárfás Hierarchy

                **Status:** `UNPROVED_CHECKABLE_TARGET`  
                **Structural leverage:** `100/100`  
                **Claim hash:** `a27352650a03fc43a637ed3fd5e31a191d47acb66eb7a2f7be1434e99fab5dc6`

                **Statement.** Conjectural target: for every finite tree \(T\) and integer \(m\ge1\), there is
\(f(T,m)\) such that every graph with \(tc(G)\le m\) and
\(\chi(G)>f(T,m)\) contains an induced \(T\). The case \(m=1\) is Erdős #738.

                **Proof route.** Use XLAYER04–XLAYER05 to attack the ambient defect graph inductively.

                **Falsifier.** A fixed m and tree T with unbounded-chromatic induced-T-free graphs of tc≤m.

                **Lean mission.** `finiteLayer_gyarfasHierarchy`

                **Novelty query.** `"triangle cover number m" Gyárfás Sumner induced tree`


                ### XLAYER11 — Two-Layer Purification Target

                **Status:** `UNPROVED_CHECKABLE_TARGET`  
                **Structural leverage:** `100/100`  
                **Claim hash:** `d0b3d71e1e9e4649867b88c85ac1720588f4b81091978f83b7ddb3eaf6f8d31c`

                **Statement.** The first hybrid frontier is \(m=2\): classify when a tree induced in one
triangle-free layer can have its entire ambient defect graph contained in one
triangle-free layer without admitting an induced copy after reselection.

                **Proof route.** Encode the second-layer defect graph with the #738 contact-signature and type-tensor machinery.

                **Falsifier.** A complete classification, or a smallest counterexample to the proposed purification mechanisms.

                **Lean mission.** `twoLayer_treePurification`

                **Novelty query.** `"two triangle-free layers" induced tree defect purification`


                ### XLAYER12 — Layer-Colored Defect Tensor Target

                **Status:** `UNPROVED_CHECKABLE_TARGET`  
                **Structural leverage:** `98/100`  
                **Claim hash:** `d6cd847f5302303f2a804dd4c9097e8e86b44de589a48541a3e8c3a307d7901d`

                **Statement.** For type-uniform path-induced tree copies inside one layer, refine the #738
Boolean defect tensor to an \((m-1)\)-colored tensor recording the first other
cover layer containing each ambient defect edge. Determine sharp support bounds,
realizability, and induced-subtree criteria.

                **Proof route.** SAT/ILP enumerate colored tensors under triangle-free constraints in each color and K4-freeness in the union.

                **Falsifier.** A smallest colored tensor violating any proposed bound or failing realizability.

                **Lean mission.** `layerColored_typeDefectTensor`

                **Novelty query.** `"colored defect tensor" triangle-free layer cover rooted tree`


## D — Transversals


                ### XTRANS01 — Transversal-Absorbed Tree Theorem

                **Status:** `CONDITIONAL_ON_738_T`  
                **Structural leverage:** `96/100`  
                **Claim hash:** `44f596a2ac146b7e138034c494a1d80572de724c70018688a91b3ed157b93517`

                **Statement.** Assume #738(T) with chromatic bound \(c(T)\). If \(D\) is a triangle transversal
of a graph \(G\) and \(\chi(G-D)>c(T)\), then there is a vertex set \(X\) such
that \((G-D)[X]\cong T\), and every ambient chord of that copy lies in \(D\).

                **Proof route.** G-D is triangle-free; apply #738(T). Any edge of G[X] absent from the induced copy in G-D belongs to D.

                **Falsifier.** A high-chromatic transversal residual with no defect-absorbed induced T.

                **Lean mission.** `transversalResidual_contains_defectAbsorbedTree`

                **Novelty query.** `"triangle transversal deletion" induced tree chords absorbed`


                ### XTRANS02 — Exact Tree-Absorption Dictionary

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `86/100`  
                **Claim hash:** `4f006646abe494128c3591940809a66c283807e018a10ef605bfb3a6ad8a7024`

                **Statement.** For a triangle transversal \(D\), a vertex set \(X\) induces \(T\) in \(G-D\)
if and only if the designated tree edges on \(X\) avoid \(D\) and every other
edge of \(G[X]\) belongs to \(D\).

                **Proof route.** Unpack inducedness in the spanning edge-deleted graph.

                **Falsifier.** A set X satisfying one side but not the exact edge-membership conditions.

                **Lean mission.** `treeInduced_afterDeletion_iff_defects_absorbed`

                **Novelty query.** `"induced tree after edge deletion" chord set transversal`


                ### XTRANS03 — Maximal Triangle-Free / Minimal Transversal Duality

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `93/100`  
                **Claim hash:** `8520810ebe9bb6dc9767e8684fe61cd4dc93640d9f42ffcb38d68f985c783858`

                **Statement.** A spanning triangle-free subgraph \(H\subseteq G\) is maximal under edge
inclusion if and only if \(E(G)\setminus E(H)\) is an inclusion-minimal
triangle transversal.

                **Proof route.** Adding a deleted edge to H creates a triangle exactly when removing that edge from the complement leaves some triangle unhit.

                **Falsifier.** A maximal triangle-free subgraph whose complement is not minimal, or conversely.

                **Lean mission.** `maximalTriangleFree_iff_minimalTriangleTransversal`

                **Novelty query.** `"maximal triangle-free subgraph" minimal triangle transversal`


                ### XTRANS04 — Minimal-Transversal Centeredness Suffices

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `99/100`  
                **Claim hash:** `fb95ab2dd39460eae8115791123b10e9077a69736838bebf6c583c6cf19e49b2`

                **Statement.** For a graph \(G\), \(tc(G)>\aleph_0\) if and only if every countable family of
inclusion-minimal triangle transversals has nonempty intersection.

                **Proof route.** One direction is immediate from centeredness of all transversals. Conversely,
every transversal contains an inclusion-minimal transversal: use Zorn on
descending transversals; finite triangle edge sets ensure intersections of
chains remain transversals. Replace each member of an arbitrary countable
family by a minimal subtransversal.

                **Falsifier.** A transversal with no minimal subtransversal, or a countable minimal family violating the equivalence.

                **Lean mission.** `triangleCover_gt_omega_iff_minimalTransversals_countablyCentered`

                **Novelty query.** `"minimal triangle transversals" countably centered`


                ### XTRANS05 — Maximal-Layer Form of Erdős #595

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `100/100`  
                **Claim hash:** `35fa37125859a724d438b1a5d3e1e9c915b0bc9033cc002092cb8a6b97325be8`

                **Statement.** A graph has \(tc(G)>\aleph_0\) if and only if no countable family of maximal
spanning triangle-free subgraphs covers \(E(G)\).

                **Proof route.** Translate XTRANS04 through XTRANS03, or extend every triangle-free layer to a maximal one by Zorn.

                **Falsifier.** A countable maximal-layer cover of a tc>ℵ₀ graph, or the converse.

                **Lean mission.** `erdos595_iff_no_countable_maximalTriangleFreeCover`

                **Novelty query.** `"maximal triangle-free subgraphs" countable edge cover`


                ### XTRANS06 — Tree-Rich Maximal-Layer Interface

                **Status:** `CONDITIONAL_ON_738_T`  
                **Structural leverage:** `92/100`  
                **Claim hash:** `f0bc11c9e48ed4a9d55eb2bc545118539035b33c8d3b2d43ad4d59cab1680187`

                **Statement.** Conditional on #738(T): every maximal triangle-free spanning subgraph \(H\) of
\(G\) with \(\chi(H)>c(T)\) contains an induced \(T\), whose ambient defects are
exactly edges of the corresponding minimal transversal.

                **Proof route.** Apply #738(T) to H and XTRANS02 to its complement.

                **Falsifier.** A high-chromatic maximal layer lacking T or with a defect outside its complement.

                **Lean mission.** `maximalTriangleFreeLayer_tree_and_defectTransversal`

                **Novelty query.** `"maximal triangle-free layer" induced tree minimal transversal`


## E — Migration


                ### XMIG01 — Arbitrarily High Link Chromatic Number with \(tc=2\)

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `92/100`  
                **Claim hash:** `cabf6f15f6fa9e94c28187556f1c5ef00df212b7ffa1f22e23b25e21b268b5d2`

                **Statement.** For every cardinal \(\kappa\) realized as the chromatic number of a
triangle-free graph \(H\), there is a \(K_4\)-free graph \(G\) with
\(tc(G)=2\) and a vertex whose neighborhood has chromatic number \(\kappa\).

                **Proof route.** Take G=K1∨H and apply XCONE08.

                **Falsifier.** A triangle-free H whose cone fails the stated parameters.

                **Lean mission.** `highChromaticLink_coexists_triangleCover_two`

                **Novelty query.** `"high chromatic neighborhood" K4-free triangle cover two`


                ### XMIG02 — Local \(#738\) Richness Does Not Carry \(#595\) Complexity

                **Status:** `REFUTED_ROUTE`  
                **Structural leverage:** `95/100`  
                **Claim hash:** `154d534b5ce982a4f00399d57496b604181e78f93aaa85e97ebd3529412439f1`

                **Statement.** A \(K_4\)-free graph may contain in one link every finite configuration,
critical block, contact-code pattern, or type-tensor pattern available in a
triangle-free graph, while the entire graph still has triangle-cover number two.

                **Proof route.** Cone the chosen triangle-free host; use XCONE08.

                **Falsifier.** A proposed theorem deriving high tc solely from one link's 738 invariants.

                **Lean mission.** `local738_richness_not_imply_595_complexity`

                **Novelty query.** `"Gyárfás Sumner structures" triangle cover sterility cone`


                ### XMIG03 — Critical-Bouquet Complexity Is Still Two-Layer

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `97/100`  
                **Claim hash:** `35e6be54cff508f490d1171d6063c69fb015185da7e7c67075ceccfcee065007`

                **Statement.** The exact critical bouquet forced inside every #595 witness by XLINK14 is itself
two-layer coverable. Therefore the flagship obstruction is not contained in the
bouquet alone but in its interaction with the rest of the witness.

                **Proof route.** Combine XLINK14 with XLINK15.

                **Falsifier.** A critical bouquet whose induced subgraph itself has uncountable triangle-cover number.

                **Lean mission.** `criticalBouquet_obstruction_migrates_outside`

                **Novelty query.** `"critical bouquet" triangle cover migration`


                ### XMIG04 — Inter-Link Obstruction Principle

                **Status:** `PROVED_IN_PACKET`  
                **Structural leverage:** `100/100`  
                **Claim hash:** `088ed7a7a6f30d90bea6cd2b8a0ed751d766f088e94e935b264f84d3c9f19f3b`

                **Statement.** In a #595 witness, no single closed neighborhood and no countable family of
closed neighborhoods carries all edges. Hence any complete proof or
construction must control interactions among uncountably many vertex links.

                **Proof route.** Single links have tc≤2 by XLINK08; countable link covers are ruled out by XLINK11.

                **Falsifier.** A witness covered by countably many closed neighborhoods.

                **Lean mission.** `erdos595_obstruction_requires_uncountablyMany_links`

                **Novelty query.** `"uncountably many links" K4-free triangle cover obstruction`


## F. Cross-campaign finite and computational targets

### X01 — Ordered-link bound equality census
Enumerate finite graphs through a chosen order \(n\), compute \(tc(G)\),
\(\lambda_\triangle(G)\), and the full-neighborhood bound. Classify equality,
large-gap, and K₄-free extremizers.

### X02 — Cone-free Folkman search
For each small tree \(T\), search finite K₄-free induced-\((K_1\vee T)\)-free
graphs maximizing \(tc(G)\). Every record immediately extracts a
triangle-free induced-\(T\)-free neighborhood of comparable chromatic number
by XCONE04.

### X03 — Cross-attack on #738 lower bounds
Use edge-cover SAT rather than direct vertex-color SAT: find a K₄-free
cone-\(T\)-free graph with \(tc>k\), then extract a \(T\)-free triangle-free
link of chromatic number \(>k\).

### X04 — Two-layer purification census
Enumerate pairs of triangle-free layers \(H_0,H_1\), find trees induced in
\(H_0\), and classify the possible triangle-free ambient defect graphs in
\(H_1\).

### X05 — Layer-colored type tensors
Implement XLAYER12 for heights \(k\le 8\), layer counts \(m\le4\), and ordered
branching \(d=3\). Determine sharp active-cell bounds and smallest
nonrealizable tensors.

### X06 — Contact-signature edge coloring
Given a long path or type-uniform tree in a high-chromatic link, assign each
ambient edge a finite/contact signature and test whether signature fibers are
automatically triangle-free under K₄-freeness.

### X07 — Minimal refinement failures
For every tree on at most ten vertices, find the smallest triangle-free
induced-\(T\)-free graph having an edge-deleted subgraph that contains induced \(T\).

### X08 — Link-cover number
Compute the closed-neighborhood edge-cover parameter \(\ell(G)\), compare it
with vertex-cover number and \(tc(G)\), and classify K₄-free equality cases for
\(tc(G)\le2\ell(G)\).

### X09 — Critical bouquet finite approximants
Find the smallest K₄-free graphs containing an apex over pairwise anticomplete
critical triangle-free blocks of chromatic numbers \(3,4,\dots,r\), then
measure how few additional cross-link edges are needed to raise \(tc\) above 2.

### X10 — Migration threshold
Starting from a two-layer critical bouquet, add K₄-safe edges outside the apex
link and determine the first exact increase of triangle-cover number.

### X11 — Maximal-layer signature families
Enumerate maximal triangle-free spanning subgraphs of finite K₄-free graphs,
encode each by #738 path/tree contact signatures, and test whether a small
signature basis covers all edges.

### X12 — Minimal-transversal contact profiles
Enumerate inclusion-minimal triangle transversals and record the induced-tree
defect profiles they absorb. Search for finite analogues of countable
centeredness.

### X13 — Finite-layer Gyárfás hierarchy
For small \(T,m,n\), maximize \(\chi(G)\) over induced-\(T\)-free graphs with
\(tc(G)\le m\). Infer candidate functions \(f(T,m)\).

### X14 — Cone-universality stress test
For finite K₄-free graphs with large \(tc\), catalogue which cones over small
trees are forced and compare the threshold with known or conjectured #738 bounds.

### X15 — Inter-link incidence complex
Build a hypergraph whose vertices are closed neighborhoods and whose elements
are graph edges contained in them. Study the minimum number of links needed to
cover the edge set and its relation to triangle transversals.

### X16 — Proof-mining transfer benchmark
Run all #738 theorem-mining operators on the extracted high-chromatic link from
XLINK06 and measure how many statements lift to ambient K₄-free cone theorems,
how many are sterile by XCONE08, and how many generate cross-link obligations.

---

## G. Forced close programs

### P01 — Ordered-link signature close for #595
Construct a countable signature coloring of every forward link and compile it
through XLINK01. Exact missing step: a uniform countable signature language for
all links of the proposed K₄-free graph.

### P02 — #738 cone-transfer close
Prove #738(T), apply XCONE03, and attack finite K₄-free cone-\(T\)-free graphs
with high \(tc\). A violation either refutes the proposed #738 bound or exposes
a semantic/implementation error.

### P03 — Two-layer purification close
Prove the \(m=2\) case of XLAYER10 by classifying one-layer ambient defect
graphs with #738 contact codes and type tensors. Then attempt induction using
XLAYER05.

### P04 — Maximal-layer basis close for #595
Use XTRANS05. Construct countably many maximal triangle-free spanning subgraphs
from countably many #738-style contact/type signatures and prove they cover
every edge.

### P05 — Minimal-transversal tree-absorption close
Use XTRANS04 and XTRANS06. Show that minimal transversals fall into countably
many tree-defect profiles, then choose one representative from each profile
whose intersection is empty.

### P06 — Critical-bouquet interaction close
Start with XLINK14. Since the bouquet itself has \(tc=2\), classify the first
K₄-safe cross-link edges outside it that can force \(tc>2,3,\dots\). Turn each
failed increase into a sterility theorem.

### P07 — Inter-link dispersion construction
Construct a K₄-free graph with uncountably many links, each locally two-layer,
whose overlap incidence prevents every countable global layer family. Verify
the exact obstruction through triangle transversals.

### P08 — Hybrid finite-obstruction ladder
For each k, build finite K₄-free \(F_k\) with \(tc(F_k)>k\), extract a
high-chromatic triangle-free link by XLINK07, mine an induced tree and its
ambient cross-link defect, and force the defects to nest coherently across k.

---

## H. Lean formalization order

1. XLINK01–XLINK05 — the ordered-link kernel.
2. XLINK08–XLINK11 — closed-neighborhood and link-cover bounds.
3. XCONE01–XCONE04, XCONE08 — cone transfer and sterility.
4. XLAYER01–XLAYER09 — product bounds, defect descent, refinement failure.
5. XTRANS02–XTRANS05 — deletion, maximal/minimal duality, centeredness.
6. XLINK13–XLINK15 — finite critical extraction and bouquet construction.
7. Conditional statements only after the exact #738 theorem/bound is separately bound.

Suggested first signatures:

```lean
theorem triangleCover_le_forwardLinkChromatic ...
theorem K4free_neighborhood_triangleFree ...
theorem erdos595_everyOrder_has_uncountablyChromatic_triangleFreeLink ...
theorem chiBounded_family_coneTransfer_triangleCover ...
theorem layerInducedTree_defectCover_descends ...
theorem maximalTriangleFree_iff_minimalTriangleTransversal ...
```

---

## I. Novelty-checker ingestion order

**Tier 1 — strongest exact cross results**

1. XLINK01 — ordered forward-link coloring.
2. XLINK06 — #595 witness link theorem.
3. XLINK14 — critical bouquet theorem.
4. XCONE02 / XCONE03 — χ-bounded cone transfer.
5. XLAYER04 / XLAYER05 — layer-defect descent.
6. XTRANS04 / XTRANS05 — minimal-transversal and maximal-layer forms.

**Tier 2 — parameters and negative theorems**

7. XLINK09 / XLINK11 — closed-neighborhood link-cover parameter.
8. XLAYER07 / XLAYER08 — induced-free refinement failure.
9. XCONE09 / XMIG02 / XMIG03 — type/critical richness sterility.
10. XLAYER10–XLAYER12 — finite-layer hierarchy and colored defect tensor.

Search exact statements, then synonyms in:

- local chromatic number / coloring number / forward neighborhoods;
- hypergraph weak coloring;
- edge Folkman and Ramsey arrow notation;
- Gyárfás–Sumner and cone-forbidden χ-boundedness;
- maximal triangle-free subgraphs / minimal triangle transversals;
- graph covers by hereditary and nonhereditary classes;
- line graphs, neighborhood complexes, and link hypergraphs.

---

## J. Court / Search inventory

### Court-ready elementary package

- XLINK01–XLINK15
- XCONE01–XCONE02, XCONE04, XCONE08–XCONE10
- XLAYER04–XLAYER05, XLAYER07–XLAYER09
- XTRANS02–XTRANS05
- XMIG01–XMIG04

These have direct proof routes in this artifact, though historical novelty remains unrun.

### Conditional package

- XCONE03, XCONE05–XCONE07
- XLAYER01–XLAYER03, XLAYER06
- XTRANS01, XTRANS06

These become Court edges only after the exact #738 statement and bound are independently supplied.

### Search-only frontier

- XLAYER10–XLAYER12
- X01–X16
- P01–P08

---

## K. Final cross-campaign compression

The mash is not merely:

```text
#738 studies triangle-free graphs
+
#595 covers by triangle-free graphs
```

It is:

```text
#595 witness
    ↓  ordered-link theorem
uncountably chromatic triangle-free link
    ↓  #738 machinery
trees, critical escape, contact codes, type tensors
    ↓  cone lift
rich local K4-free structure
    ↓  sterility theorem
local structure still has tc = 2
    ↓
the true obstruction migrates to interactions among uncountably many links
    ↓
new flagship:
classify inter-link defects/transversals well enough to force or forbid
a countable maximal triangle-free layer basis
```

That is a new research object, not a loose analogy.

**Recommended next attack:** formalize XLINK01 first. If it survives Lean and
novelty review, use XCONE04 as a new computational rail for #738 and use
XLINK14/XMIG03 to launch the critical-bouquet interaction campaign for #595.
