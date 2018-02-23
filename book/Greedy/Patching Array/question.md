
Given a sorted positive integer array *nums* and an integer *n*, add/patch elements to the array such that any number in range `[1, n]` inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.


**Example 1:**<br>
*nums* = `[1, 3]`, *n* = `6`<br>
Return `1`.

Combinations of *nums* are `[1], [3], [1,3]`, which form possible sums of: `1, 3, 4`.<br>
Now if we add/patch `2` to *nums*, the combinations are: `[1], [2], [3], [1,3], [2,3], [1,2,3]`.<br>
Possible sums are `1, 2, 3, 4, 5, 6`, which now covers the range `[1, 6]`.<br>
So we only need `1` patch.

**Example 2:**<br>
*nums* = `[1, 5, 10]`, *n* = `20`<br>
Return `2`.<br>
The two patches can be `[2, 4]`.

**Example 3:**<br>
*nums* = `[1, 2, 2]`, *n* = `5`<br>
Return `0`.<br>

<p>**Credits:**<br />Special thanks to [@dietpepsi](https://leetcode.com/discuss/user/dietpepsi) for adding this problem and creating all test cases.
