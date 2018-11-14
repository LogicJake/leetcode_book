## Decoded String at Index  
### 链接  
https://leetcode.com/problems/decoded-string-at-index/description/  
### 问题描述
An encoded string `S` is given.&nbsp; To find and write the **decoded** string to a tape, the encoded string is read **one character at a time**&nbsp;and the following steps are taken:

	- If the character read is a letter, that letter is written onto the tape.
	- If the character read is a digit (say `d`), the entire current tape is repeatedly written&nbsp;`d-1`&nbsp;more times in total.

Now for some encoded string `S`, and an index `K`, find and return the `K`-th letter (1 indexed) in the decoded string.

&nbsp;

**Example 1:**

**Example 2:**

**Example 3:**

&nbsp;

**Note:**

	1. `2 &lt;= S.length &lt;= 100`
	1. `S`&nbsp;will only contain lowercase letters and digits `2` through `9`.
	1. `S`&nbsp;starts with a letter.
	1. `1 &lt;= K &lt;= 10^9`
	1. The decoded string is guaranteed to have less than `2^63` letters.
