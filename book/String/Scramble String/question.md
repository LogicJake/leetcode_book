## Scramble String  
### 问题描述

Given a string *s1*, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.



Below is one possible representation of *s1* = `"great"`:



To scramble the string, we may choose any non-leaf node and swap its two children.



For example, if we choose the node `"gr"` and swap its two children, it produces a scrambled string `"rgeat"`.



We say that `"rgeat"` is a scrambled string of `"great"`.



Similarly, if we continue to swap the children of nodes `"eat"` and `"at"`, it produces a scrambled string `"rgtae"`.



We say that `"rgtae"` is a scrambled string of `"great"`.



Given two strings *s1* and *s2* of the same length, determine if *s2* is a scrambled string of *s1*.

