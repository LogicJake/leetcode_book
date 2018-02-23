## Stickers to Spell Word  
### 问题描述

We are given N different types of stickers.  Each sticker has a lowercase English word on it.



You would like to spell out the given `target` string by cutting individual letters from your collection of stickers and rearranging them.



You can use each sticker more than once if you want, and you have infinite quantities of each sticker.



What is the minimum number of stickers that you need to spell out the `target`?  If the task is impossible, return -1.


**Example 1:**

Input:<pre>
["with", "example", "science"], "thehat"
</pre>

Output:<pre>
3
</pre>

Explanation:<pre>
We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.
</pre>

**Example 2:**

Input:<pre>
["notice", "possible"], "basicbasic"
</pre>

Output:<pre>
-1
</pre>

Explanation:<pre>
We can't form the target "basicbasic" from cutting letters from the given stickers.
</pre>

**Note:**
- `stickers` has length in the range `[1, 50]`.
- `stickers` consists of lowercase English words (without apostrophes).
- `target` has length in the range `[1, 15]`, and consists of lowercase English letters.
- In all test cases, all words were chosen <u>randomly</u> from the 1000 most common US English words, and the target was chosen as a concatenation of two random words.
- The time limit may be more challenging than usual.  It is expected that a 50 sticker test case can be solved within 35ms on average.

