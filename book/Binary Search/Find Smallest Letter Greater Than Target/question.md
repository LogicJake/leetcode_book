## Find Smallest Letter Greater Than Target  
### 链接  
https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/  
### 问题描述

Given a list of sorted characters `letters` containing only lowercase letters, and given a target letter `target`, find the smallest element in the list that is larger than the given target.



Letters also wrap around.  For example, if the target is `target = 'z'` and `letters = ['a', 'b']`, the answer is `'a'`.


**Examples:**<br />
<pre>
**Input:**
letters = ["c", "f", "j"]
target = "a"
**Output:** "c"

**Input:**
letters = ["c", "f", "j"]
target = "c"
**Output:** "f"

**Input:**
letters = ["c", "f", "j"]
target = "d"
**Output:** "f"

**Input:**
letters = ["c", "f", "j"]
target = "g"
**Output:** "j"

**Input:**
letters = ["c", "f", "j"]
target = "j"
**Output:** "c"

**Input:**
letters = ["c", "f", "j"]
target = "k"
**Output:** "c"
</pre>


**Note:**<br>
<ol>
- `letters` has a length in range `[2, 10000]`.
- `letters` consists of lowercase letters, and contains at least 2 unique letters.
- `target` is a lowercase letter.
</ol>

