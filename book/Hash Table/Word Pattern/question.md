## Word Pattern  
### 问题描述
Given a `pattern` and a string `str`, find if `str` follows the same pattern.

 Here **follow** means a full match, such that there is a bijection between a letter in `pattern` and a **non-empty** word in `str`.


**Examples:**<br>
<ol>
- pattern = `"abba"`, str = `"dog cat cat dog"` should return true.
- pattern = `"abba"`, str = `"dog cat cat fish"` should return false.
- pattern = `"aaaa"`, str = `"dog cat cat dog"` should return false.
- pattern = `"abba"`, str = `"dog dog dog dog"` should return false.
</ol>



**Notes:**<br>
You may assume `pattern` contains only lowercase letters, and `str` contains lowercase letters separated by a single space.


**Credits:**<br />Special thanks to [@minglotus6](https://leetcode.com/discuss/user/minglotus6) for adding this problem and creating all test cases.
