#!/usr/bin/env python3
"""Finite hostile checks for the Erdős #738 × #595 cross-forge kernel."""

from __future__ import annotations
import itertools
import json
import sys
from pathlib import Path


def norm_edge(u, v):
    return (u, v) if u < v else (v, u)


def all_edges(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def graph_from_mask(n, mask):
    edges = all_edges(n)
    adj = [set() for _ in range(n)]
    present = []
    for bit, (u, v) in enumerate(edges):
        if (mask >> bit) & 1:
            adj[u].add(v)
            adj[v].add(u)
            present.append((u, v))
    return adj, present


def induced_edges(vertices, present):
    s = set(vertices)
    return [norm_edge(u, v) for u, v in present if u in s and v in s]


def triangles(n, present):
    es = {norm_edge(*e) for e in present}
    out = []
    for a, b, c in itertools.combinations(range(n), 3):
        tri = [norm_edge(a, b), norm_edge(a, c), norm_edge(b, c)]
        if all(e in es for e in tri):
            out.append(tuple(tri))
    return out


def is_k4_free(n, present):
    es = {norm_edge(*e) for e in present}
    for vs in itertools.combinations(range(n), 4):
        if all(norm_edge(*e) in es for e in itertools.combinations(vs, 2)):
            return False
    return True


def is_triangle_free(n, present):
    return not triangles(n, present)


def chromatic_number(vertices, present):
    vertices = list(vertices)
    if not vertices:
        return 0
    index = {v: i for i, v in enumerate(vertices)}
    local_edges = [
        (index[u], index[v])
        for u, v in (norm_edge(*e) for e in present)
        if u in index and v in index
    ]
    m = len(vertices)
    neighbors = [set() for _ in range(m)]
    for u, v in local_edges:
        neighbors[u].add(v)
        neighbors[v].add(u)
    order = sorted(range(m), key=lambda x: len(neighbors[x]), reverse=True)

    def can_color(k):
        colors = [-1] * m

        def rec(pos):
            if pos == m:
                return True
            v = order[pos]
            forbidden = {colors[w] for w in neighbors[v] if colors[w] >= 0}
            for c in range(k):
                if c not in forbidden:
                    colors[v] = c
                    if rec(pos + 1):
                        return True
                    colors[v] = -1
            return False

        return rec(0)

    for k in range(1, m + 1):
        if can_color(k):
            return k
    raise AssertionError("unreachable")


def triangle_cover_number(n, present):
    edges = sorted({norm_edge(*e) for e in present})
    tris = triangles(n, edges)
    if not edges:
        return 0
    if not tris:
        return 1

    edge_index = {e: i for i, e in enumerate(edges)}
    tri_indices = [[edge_index[e] for e in tri] for tri in tris]

    for k in (2, 3):
        colors = [-1] * len(edges)
        memberships = [[] for _ in edges]
        for ti, tri in enumerate(tri_indices):
            for ei in tri:
                memberships[ei].append(ti)
        order = sorted(range(len(edges)), key=lambda e: len(memberships[e]), reverse=True)

        def valid_partial(ti):
            vals = [colors[e] for e in tri_indices[ti]]
            return not (all(x >= 0 for x in vals) and vals[0] == vals[1] == vals[2])

        def rec(pos):
            if pos == len(order):
                return True
            e = order[pos]
            for c in range(k):
                colors[e] = c
                if all(valid_partial(ti) for ti in memberships[e]) and rec(pos + 1):
                    return True
                colors[e] = -1
            return False

        if rec(0):
            return k
    raise AssertionError("tc > 3 on <=5 vertices")


def verify():
    assertions = 0
    graphs = 0

    for n in range(1, 6):
        for mask in range(1 << len(all_edges(n))):
            adj, present = graph_from_mask(n, mask)
            graphs += 1
            tc = triangle_cover_number(n, present)

            max_link_chi = 0
            for v in range(n):
                nv = sorted(adj[v])
                max_link_chi = max(max_link_chi, chromatic_number(nv, present))
            if present:
                assert tc <= max(1, max_link_chi)
            else:
                assert tc == 0
            assertions += 1

            if is_k4_free(n, present):
                for v in range(n):
                    nv = sorted(adj[v])
                    nv_edges = induced_edges(nv, present)
                    assert is_triangle_free(n, nv_edges)
                    assertions += 1

                    closed = [v] + nv
                    closed_edges = induced_edges(closed, present)
                    assert triangle_cover_number(n, closed_edges) <= 2
                    assertions += 1

    cone_cases = 0
    for n in range(1, 5):
        for mask in range(1 << len(all_edges(n))):
            _, base_edges = graph_from_mask(n, mask)
            if not is_triangle_free(n, base_edges):
                continue
            apex = n
            cone_edges = list(base_edges) + [norm_edge(apex, v) for v in range(n)]
            assert is_k4_free(n + 1, cone_edges)
            expected = 2 if base_edges else 1
            assert triangle_cover_number(n + 1, cone_edges) == expected
            cone_cases += 1
            assertions += 2

    # XLAYER07 explicit hostile witness.
    c4 = [norm_edge(0, 1), norm_edge(1, 2), norm_edge(2, 3), norm_edge(3, 0)]
    assert is_triangle_free(4, c4)
    assert len(c4) == 4
    p4 = c4[:-1]
    deg = [0] * 4
    for u, v in p4:
        deg[u] += 1
        deg[v] += 1
    assert sorted(deg) == [1, 1, 2, 2]
    assertions += 4

    return {
        "schema": "oracle.erdos738x595.cross-verification.v1",
        "graphs_exhausted": graphs,
        "max_vertices": 5,
        "cone_cases": cone_cases,
        "assertions": assertions,
        "passed": True,
        "checked_claims": [
            "XLINK01/XLINK03 finite consequence",
            "XLINK05",
            "XLINK08",
            "XCONE08",
            "XLAYER07",
        ],
    }


if __name__ == "__main__":
    result = verify()
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if len(sys.argv) > 1:
        Path(sys.argv[1]).write_text(encoded, encoding="utf-8")
    print(encoded, end="")
