




# A graph G is an ordered triple (V(G), E(G), ø) consisting of a
# nonempty set V( G) of vert~ces, a set E(G), disjoint from V(G), of edges,
# and an incidence function ø that associates with each edge of G an
# unordered pair of (not necessarily distinct) vertices of G. If e is an edge and
# u and t' are vertices such that ø(e) = UV, then e is said to join u and v; the
# vertices u and 'v 'are called the ends of e.



# ---- Planar  ----
# Those graphs that have a diagram
# whose edges intersect only at their ends are called
# plartar,

# Exercise :
# * write an algorithm that detects planar and non-planar
#   graphs

# ---- Distinct Graph -------
# Two graphs G and H are identical (written G =H) if V(G) =V(H),
# E(G) = E(H), and  ø(G) = ø(H). If two graphs are identical then they can clearly
# be represented by identical diagrams.


# ------ Complete Graph ------
# A simple graph in which each pair of distinct vertices is joined by an edge is
# called a complete graph.


# ------ Bipartite Graphs -----

# An empty graph,on the other hand, is one with no edges. A bipartite
# graph is one whose vertex set can be partitioned into two subsets X and Y,
# so that each edge has one end in X and one end in Y; such a partition
# (X, Y) is called a bipartition of the graph


# ------ Complete Bipartite Graph --------

# A complete bipartite graph is a
# simple bipartite graph with bipartition (X, Y) in which each vertex of X is
# joined to each vertex of Y