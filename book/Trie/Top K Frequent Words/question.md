## Top K Frequent Words  
### 链接  
https://leetcode.com/problems/top-k-frequent-words/description/  
### 问题描述
Given a non-empty list of words, return the *k* most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

**Example 1:**<br />
<pre>
**Input:** ["i", "love", "leetcode", "i", "love", "coding"], k = 2
**Output:** ["i", "love"]
**Explanation:** "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
</pre>


**Example 2:**<br />
<pre>
**Input:** ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
**Output:** ["the", "is", "sunny", "day"]
**Explanation:** "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
</pre>


**Note:**<br>
<ol>
- You may assume *k* is always valid, 1 &le; *k* &le; number of unique elements.
- Input words contain only lowercase letters.
</ol>


**Follow up:**<br />
<ol>
- Try to solve it in *O*(*n* log *k*) time and *O*(*n*) extra space.
</ol>

