## Guess the Word  
### 链接  
https://leetcode.com/problems/guess-the-word/description/  
### 问题描述
This problem is an&nbsp;****interactive problem****&nbsp;new to the LeetCode platform.

We are given a word list of unique words, each word is 6 letters long, and one word in this list is chosen as **secret**.

You may call `master.guess(word)`&nbsp;to guess a word.&nbsp; The guessed word should have&nbsp;type `string`&nbsp;and must be from the original list&nbsp;with 6 lowercase letters.

This function returns an&nbsp;`integer`&nbsp;type, representing&nbsp;the number of exact matches (value and position) of your guess to the **secret word**.&nbsp; Also, if your guess is not in the given wordlist, it will return `-1` instead.

For each test case, you have 10 guesses to guess the word. At the end of any number of calls, if you have made 10 or less calls to `master.guess`&nbsp;and at least one of these guesses was the **secret**, you pass the testcase.

Besides the example test case below, there will be 5&nbsp;additional test cases, each with 100 words in the word list.&nbsp; The letters of each word in those testcases were chosen&nbsp;independently at random from `&#39;a&#39;` to `&#39;z&#39;`, such that every word in the given word lists is unique.

**Note:**&nbsp; Any solutions that attempt to circumvent the judge&nbsp;will result in disqualification.
