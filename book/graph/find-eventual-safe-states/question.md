## Find Eventual Safe States  
### 链接  
https://leetcode.com/problems/find-eventual-safe-states/description/  
### 问题描述
In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.&nbsp; If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

Now, say our starting node is **eventually safe&nbsp;**if and only if we must eventually walk to a terminal node.&nbsp; More specifically, there exists a natural number `K` so that for any choice of where to walk, we must have stopped at a terminal node in less than `K` steps.

Which nodes are eventually safe?&nbsp; Return them as an array in sorted order.

The directed graph has `N` nodes with labels `0, 1, ..., N-1`, where `N` is the length of `graph`.&nbsp; The&nbsp;graph is given in the following form: `graph[i]` is a list of labels `j` such that `(i, j)` is a directed edge of the graph.

<img alt="Illustration of graph" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/03/17/picture1.png" style="height:86px; width:300px" />

**Note:**

	- `graph` will have length at most `10000`.
	- The number of edges in the graph will not exceed `32000`.
	- Each `graph[i]` will be a sorted list of different integers, chosen within the range `[0, graph.length - 1]`.
