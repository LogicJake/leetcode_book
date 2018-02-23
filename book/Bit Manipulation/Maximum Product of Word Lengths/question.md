

    Given a string array `words`, find the maximum value of `length(word[i]) * length(word[j])` where the two words do not share common letters.
    You may assume that each word will contain only lower case letters.
    If no such two words exist, return 0.



    **Example 1:**<br/>



    Given `["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]`<br/>
    Return `16`<br/>
    The two words can be `"abcw", "xtfn"`.



    **Example 2:**<br/>



    Given `["a", "ab", "abc", "d", "cd", "bcd", "abcd"]`<br/>
    Return `4`<br/>
    The two words can be `"ab", "cd"`.



    **Example 3:**<br/>



    Given `["a", "aa", "aaa", "aaaa"]`<br/>
    Return `0`<br/>
    No such pair of words.    


**Credits:**<br />Special thanks to [@dietpepsi](https://leetcode.com/discuss/user/dietpepsi) for adding this problem and creating all test cases.
