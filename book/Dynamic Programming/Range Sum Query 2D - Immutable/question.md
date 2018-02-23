## Range Sum Query 2D - Immutable  
### 问题描述
Given a 2D matrix *matrix*, find the sum of the elements inside the rectangle defined by its upper left corner (*row*1, *col*1) and lower right corner (*row*2, *col*2).


<img src="/static/images/courses/range_sum_query_2d.png" border="0" alt="Range Sum Query 2D" /><br />
<small>The above rectangle (with the red border) is defined by (row1, col1) = **(2, 1)** and (row2, col2) = **(4, 3)**, which contains sum = **8**.</small>


**Example:**<br>
<pre>
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
</pre>


**Note:**<br>
<ol>
- You may assume that the matrix does not change.
- There are many calls to *sumRegion* function.
- You may assume that *row*1 &le; *row*2 and *col*1 &le; *col*2.
</ol>

