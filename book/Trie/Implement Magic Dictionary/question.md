

Implement a magic directory with `buildDict`, and `search` methods.



For the method `buildDict`, you'll be given a list of non-repetitive words to build a dictionary.



For the method `search`, you'll be given a word, and judge whether if you modify **exactly** one character into **another** character in this word, the modified word is in the dictionary you just built.


**Example 1:**<br />
<pre>
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
</pre>


**Note:**<br>
<ol>
- You may assume that all the inputs are consist of lowercase letters `a-z`.
- For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
- Please remember to **RESET** your class variables declared in class MagicDictionary, as static/class variables are **persisted across multiple test cases**. Please see [here](https://leetcode.com/faq/#different-output) for more details.
</ol>

