## Clone Graph  
### 问题描述

Clone an undirected graph. Each node in the graph contains a `label` and a list of its `neighbors`.



Nodes are labeled uniquely.



As an example, consider the serialized graph `<font color="red">{<font color="black">0</font>,1,2#</font><font color="blue"><font color="black">1</font>,2#</font><font color="green"><font color="black">2</font>,2}</font>`.



The graph has a total of three nodes, and therefore contains three parts as separated by `#`.
<ol>
- First node is labeled as `<font color="black">0</font>`. Connect node `<font color="black">0</font>` to both nodes `<font color="red">1</font>` and `<font color="red">2</font>`.
- Second node is labeled as `<font color="black">1</font>`. Connect node `<font color="black">1</font>` to node `<font color="blue">2</font>`.
- Third node is labeled as `<font color="black">2</font>`. Connect node `<font color="black">2</font>` to node `<font color="green">2</font>` (itself), thus forming a self-cycle.
</ol>



Visually, the graph looks like the following:
<pre>
       1
      / \
     /   \
    0 --- 2
         / \
         \_/
</pre>

