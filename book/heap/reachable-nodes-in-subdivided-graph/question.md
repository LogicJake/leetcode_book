## Reachable Nodes In Subdivided Graph  
### 链接  
https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/description/  
### 问题描述
Starting with an&nbsp;**undirected** graph (the &quot;original graph&quot;) with nodes from `0` to `N-1`, subdivisions are made to some of the edges.

The graph is given as follows: `edges[k]` is a list of integer pairs `(i, j, n)` such that `(i, j)` is an edge of the original graph,

and `n` is the total number of **new** nodes on that edge.&nbsp;

Then, the edge `(i, j)` is deleted from the original graph,&nbsp;`n`&nbsp;new nodes `(x_1, x_2, ..., x_n)` are added to the original graph,

and `n+1` new&nbsp;edges `(i, x_1), (x_1, x_2), (x_2, x_3), ..., (x_{n-1}, x_n), (x_n, j)`&nbsp;are added to the original&nbsp;graph.

Now, you start at node `0`&nbsp;from the original graph, and in each move, you travel along one&nbsp;edge.&nbsp;

Return how many nodes you can reach in at most `M` moves.

&nbsp;

**Example 1:**

**Example 2:**

&nbsp;

**Note:**

	1. `0 &lt;= edges.length &lt;= 10000`
	1. `0 &lt;= edges[i][0] &lt;&nbsp;edges[i][1] &lt; N`
	1. There does not exist any&nbsp;`i != j` for which `edges[i][0] == edges[j][0]` and `edges[i][1] == edges[j][1]`.
	1. The original graph&nbsp;has no parallel edges.
	1. `0 &lt;= edges[i][2] &lt;= 10000`
	1. `0 &lt;= M &lt;= 10^9`
	1. `<font face="monospace">1 &lt;= N &lt;= 3000</font>`
	1. A reachable node is a node that can be travelled to&nbsp;using at most&nbsp;M moves starting from&nbsp;node 0.
