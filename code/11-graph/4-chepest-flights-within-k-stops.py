"""
787. Cheapest Flights Within K Stops
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

Example 1:
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

Example 2:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

Example 3:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
"""
from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Dijkstra's algorithm
        Time Complexity: O(E log V)
        Space Complexity: O(E + V)
        where E is the number of edges and V is the number of vertices.
        """
        graph = defaultdict(list)
        for source, dest, price in flights:
            graph[source].append((dest, price))
        heap = [(0, src, 0)] # price, city, flight_used
        best = {} # (city, flight_used) -> min_price
        while heap:
            curr_price, curr_loc, flight_used = heapq.heappop(heap)
            if curr_loc == dst:
                return curr_price
            if flight_used == k + 1:
                continue
            for neightbour, price in graph[curr_loc]:
                new_price = price + curr_price
                new_flight_used = flight_used + 1
                if new_price < best.get((neightbour, new_flight_used), float('inf')):
                    best[(neightbour, new_flight_used)] = new_price
                    heapq.heappush(heap, ((new_price, neightbour, new_flight_used)))
        return -1
            
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Bellman-Ford algorithm
        Time Complexity: O(E * V)
        Space Complexity: O(V + E)
        where E is the number of edges and V is the number of vertices.
        """
        prices = [float('inf')] * n
        prices[src] = 0
        for i in range(k+1):
            temp_prices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue
                if prices[s] + p < temp_prices[d]:
                    temp_prices[d] = prices[s] + p
            prices = temp_prices
        return -1 if prices[dst] == float('inf') else prices[dst]

            
        

        

