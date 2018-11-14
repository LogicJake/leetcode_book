## Course Schedule II  
### 链接  
https://leetcode.com/problems/course-schedule-ii/description/  
### 问题描述
There are a total of **n** courses you have to take, labeled from `0` to `n-1`.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: `[0,1]`

Given the total number of courses and a list of prerequisite **pairs**, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

**Example 1:**

```
[0,1]</code>
**Explanation:**&nbsp;There are a total of 2 courses to take. To take course 1 you should have finished   
&nbsp;            course 0. So the correct course order is <code>[0,1] .
```

**Example 2:**

```
[0,1,2,3] or [0,2,1,3]</code>
**Explanation:**&nbsp;There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
&nbsp;            So one correct course order is `[0,1,2,3]`. Another correct ordering is <code>[0,2,1,3] .
```

**Note:**

	1. The input prerequisites is a graph represented by **a list of edges**, not adjacency matrices. Read more about [how a graph is represented](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs).
	1. You may assume that there are no duplicate edges in the input prerequisites.
