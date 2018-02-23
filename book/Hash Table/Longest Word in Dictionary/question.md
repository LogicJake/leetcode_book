## Longest Word in Dictionary  
### 问题描述
Given a list of strings `words` representing an English Dictionary, find the longest word in `words` that can be built one character at a time by other words in `words`.  If there is more than one possible answer, return the longest word with the smallest lexicographical order.

**Example 1:**<br />
<pre>
**Input:** 
words = ["w","wo","wor","worl", "world"]
**Output:** "world"
**Explanation:** 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
</pre>


**Example 2:**<br />
<pre>
**Input:** 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
**Output:** "apple"
**Explanation:** 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
</pre>


**Note:**
- All the strings in the input will only contain lowercase letters.
- The length of `words` will be in the range `[1, 1000]`.
- The length of `words[i]` will be in the range `[1, 30]`.

