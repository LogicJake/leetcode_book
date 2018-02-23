## Unique Substrings in Wraparound String  
### 问题描述
Consider the string `s` to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so `s` will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string `p`. Your job is to find out how many unique non-empty substrings of `p` are present in `s`. In particular, your input is the string `p` and you need to output the number of different non-empty substrings of `p` in the string `s`.

**Note:** `p` consists of only lowercase English letters and the size of p might be over 10000.

**Example 1:**<br />
<pre>
**Input:** "a"
**Output:** 1

**Explanation:** Only the substring "a" of string "a" is in the string s.
</pre>


**Example 2:**<br />
<pre>
**Input:** "cac"
**Output:** 2
**Explanation:** There are two substrings "a", "c" of string "cac" in the string s.
</pre>


**Example 3:**<br />
<pre>
**Input:** "zab"
**Output:** 6
**Explanation:** There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.
</pre>

