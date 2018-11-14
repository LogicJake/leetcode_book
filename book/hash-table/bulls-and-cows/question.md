## Bulls and Cows  
### 链接  
https://leetcode.com/problems/bulls-and-cows/description/  
### 问题描述
You are playing the following [Bulls and Cows](https://en.wikipedia.org/wiki/Bulls_and_Cows) game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called &quot;bulls&quot;) and how many digits match the secret number but locate in the wrong position (called &quot;cows&quot;). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend&#39;s guess, use `A` to indicate the bulls and `B` to indicate the cows.&nbsp;

Please note that both secret number and friend&#39;s guess may contain duplicate digits.

**Example 1:**

```
3</code> cows. The bull is `8`, the cows are `0`, `1` and <code>7<font face="sans-serif, Arial, Verdana, Trebuchet MS">.</font>
```

**Example 2:**

**Note: **You may assume that the secret number and your friend&#39;s guess only contain digits, and their lengths are always equal.
