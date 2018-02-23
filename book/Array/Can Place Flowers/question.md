## Can Place Flowers  
### 问题描述
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number **n**, return if **n** new flowers can be planted in it without violating the no-adjacent-flowers rule.

**Example 1:**<br />
<pre>
**Input:** flowerbed = [1,0,0,0,1], n = 1
**Output:** True
</pre>


**Example 2:**<br />
<pre>
**Input:** flowerbed = [1,0,0,0,1], n = 2
**Output:** False
</pre>


**Note:**<br>
<ol>
- The input array won't violate no-adjacent-flowers rule.
- The input array size is in the range of [1, 20000].
- **n** is a non-negative integer which won't exceed the input array size.
</ol>

