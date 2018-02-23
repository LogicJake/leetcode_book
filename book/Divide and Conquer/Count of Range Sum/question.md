## Count of Range Sum  
### 问题描述

    Given an integer array `nums`, return the number of range sums that lie in `[lower, upper]` inclusive.<br/>

    Range sum `S(i, j)` is defined as the sum of the elements in `nums` between indices `i` and 
    `j` (`i` &le; `j`), inclusive.



    **Note:**<br/>
    A naive algorithm of *O*(*n*<sup>2</sup>) is trivial. You MUST do better than that.



    **Example:**<br/>
    Given *nums* = `[-2, 5, -1]`, *lower* = `-2`, *upper* = `2`,<br/>
    Return `3`.<br/>
    The three ranges are : `[0, 0]`, `[2, 2]`, `[0, 2]` and their respective sums are: `-2, -1, 2`.


**Credits:**<br />Special thanks to [@dietpepsi](https://leetcode.com/discuss/user/dietpepsi) for adding this problem and creating all test cases.
