## Is Graph Bipartite?  
### 链接  
https://leetcode.com/problems/is-graph-bipartite/description/  
### 问题描述
Given an undirected&nbsp;`graph`, return `true` if and only if it is bipartite.

Recall that a graph is **bipartite** if we can split it&#39;s set of nodes into two independent&nbsp;subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: `graph[i]` is a list of indexes `j` for which the edge between nodes `i` and `j` exists.&nbsp; Each node is an integer between `0` and `graph.length - 1`.&nbsp; There are no self edges or parallel edges: `graph[i]` does not contain `i`, and it doesn&#39;t contain any element twice.

&nbsp;

**Note:**

	- `graph` will have length in range `[1, 100]`.
	- `graph[i]` will contain integers in range `[0, graph.length - 1]`.
	- `graph[i]` will not contain `i` or duplicate values.
	- The graph is undirected: if any element `j` is in `graph[i]`, then `i` will be in `graph[j]`.
