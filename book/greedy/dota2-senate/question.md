## Dota2 Senate  
### 链接  
https://leetcode.com/problems/dota2-senate/description/  
### 问题描述

In the world of Dota2, there are two parties: the `Radiant` and the `Dire`.



The Dota2 senate consists of senators coming from two parties. Now the senate wants to make a decision about a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise `one` of the two rights:
<ol>
- `Ban one senator's right`: <br/>A senator can make another senator lose **all his rights** in this and all the following rounds.
- `Announce the victory`: <br/>If this senator found the senators who still have rights to vote are all from **the same party**, he can announce the victory and make the decision about the change in the game.
</ol>



Given a string representing each senator's party belonging. The character 'R' and 'D' represent the `Radiant` party and the `Dire` party respectively. Then if there are `n` senators, the size of the given string will be `n`.



The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.



Suppose every senator is smart enough and will play the best strategy for his own party, you need to predict which party will finally announce the victory and make the change in the Dota2 game. The output should be `Radiant` or `Dire`.


**Example 1:**<br />
<pre>
**Input:** "RD"
**Output:** "Radiant"
**Explanation:** The first senator comes from Radiant and he can just ban the next senator's right in the round 1. <br/>And the second senator can't exercise any rights any more since his right has been banned. <br/>And in the round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
</pre>


**Example 2:**<br />
<pre>
**Input:** "RDD"
**Output:** "Dire"
**Explanation:** 
The first senator comes from Radiant and he can just ban the next senator's right in the round 1. <br/>And the second senator can't exercise any rights anymore since his right has been banned. <br/>And the third senator comes from Dire and he can ban the first senator's right in the round 1. <br/>And in the round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
</pre>


**Note:**<br>
<ol>
- The length of the given string will in the range [1, 10,000].
</ol>

