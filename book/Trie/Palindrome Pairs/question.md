## Palindrome Pairs  
### 链接  
https://leetcode.com/problems/palindrome-pairs/description/  
### 问题描述

    Given a list of **unique** words, find all pairs of ***distinct*** indices `(i, j)` in the given list, so that the concatenation of the two words, i.e. `words[i] + words[j]` is a palindrome.



    **Example 1:**<br/>
    Given `words` = `["bat", "tab", "cat"]`<br/>
    Return `[[0, 1], [1, 0]]`<br/>
    The palindromes are `["battab", "tabbat"]`<br/>



    **Example 2:**<br/>
    Given `words` = `["abcd", "dcba", "lls", "s", "sssll"]`<br/>
    Return `[[0, 1], [1, 0], [3, 2], [2, 4]]`<br/>
    The palindromes are `["dcbaabcd", "abcddcba", "slls", "llssssll"]`<br/>


**Credits:**<br />Special thanks to [@dietpepsi](https://leetcode.com/discuss/user/dietpepsi) for adding this problem and creating all test cases.
