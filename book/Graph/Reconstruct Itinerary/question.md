
Given a list of airline tickets represented by pairs of departure and arrival airports `[from, to]`, reconstruct the itinerary in order. All of the tickets belong to a man who departs from `JFK`. Thus, the itinerary must begin with `JFK`.



**Note:**<br />
<ol>
- If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary `["JFK", "LGA"]` has a smaller lexical order than `["JFK", "LGB"]`.
- All airports are represented by three capital letters (IATA code).
- You may assume all tickets form at least one valid itinerary.
</ol>



    **Example 1:**<br/>
    `tickets` = `[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]`<br/>
    Return `["JFK", "MUC", "LHR", "SFO", "SJC"]`.<br/>



    **Example 2:**<br/>
    `tickets` = `[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]`<br/>
    Return `["JFK","ATL","JFK","SFO","ATL","SFO"]`.<br/>
    Another possible reconstruction is `["JFK","SFO","ATL","JFK","ATL","SFO"]`. But it is larger in lexical order.


**Credits:**<br />Special thanks to [@dietpepsi](https://leetcode.com/discuss/user/dietpepsi) for adding this problem and creating all test cases.
