## Freedom Trail  
### 链接  
https://leetcode.com/problems/freedom-trail/description/  
### 问题描述

In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring", and use the dial to spell a specific keyword in order to open the door. 



Given a string **ring**, which represents the code engraved on the outer ring and another string **key**, which represents the keyword needs to be spelled. You need to find the **minimum** number of steps in order to spell all the characters in the keyword.


<li>You can rotate the **ring** clockwise or anticlockwise **one place**, which counts as 1 step. The final purpose of the rotation is to align one of the string **ring's** characters at the 12:00 direction, where this character must equal to the character **key[i]**.

1. If the character **key[i]** has been aligned at the 12:00 direction, you need to press the center button to spell, which also counts as 1 step. After the pressing, you could begin to spell the next character in the key (next stage), otherwise, you've finished all the spelling.

**Example:**<br />
<center>
<img src="/static/images/problemset/ring.jpg" width = "26%" />
</center>
</br>
<pre>
**Input:** ring = "godding", key = "gd"
**Output:** 4
**Explanation:**</br> For the first key character 'g', since it is already in place, we just need 1 step to spell this character. </br> For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".</br> Also, we need 1 more step for spelling.</br> So the final output is 4.
</pre>


**Note:**<br>
<ol>
- Length of both ring and **key** will be in range 1 to 100.
- There are only lowercase letters in both strings and might be some duplcate characters in both strings.
- It's guaranteed that string **key** could always be spelled by rotating the string **ring**.
</ol>

