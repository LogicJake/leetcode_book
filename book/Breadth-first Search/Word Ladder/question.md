

Given two words (*beginWord* and *endWord*), and a dictionary's word list, find the length of shortest transformation sequence from *beginWord* to *endWord*, such that:


1. Only one letter can be changed at a time.
1. Each transformed word must exist in the word list. Note that *beginWord* is *not* a transformed word.


For example,



Given:<br />
*beginWord* = `"hit"`<br />
*endWord* = `"cog"`<br />
*wordList* = `["hot","dot","dog","lot","log","cog"]`<br />



As one shortest transformation is `"hit" -> "hot" -> "dot" -> "dog" -> "cog"`,<br />
return its length `5`.



**Note:**<br />
<ul>
- Return 0 if there is no such transformation sequence.
- All words have the same length.
- All words contain only lowercase alphabetic characters.
- You may assume no duplicates in the word list.
- You may assume *beginWord* and *endWord* are non-empty and are not the same.
</ul>



**<font color="red">UPDATE (2017/1/20):</font>**<br />
The *wordList* parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

