"""
743. Network Delay Time

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
"""
from collections import defaultdict
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for source, dest, time in times:
            graph[source].append((time, dest))
        dist = {k: 0} # rest float('inf')
        heap = [(0, k)]

        while heap:
            curr_time, curr_node = heapq.heappop(heap)
            if curr_time > dist.get(curr_node, float('inf')):
                continue
            for time, nei in graph[curr_node]:
                new_time = time + curr_time
                if new_time < dist.get(nei, float('inf')):
                    dist[nei] = new_time
                    heapq.heappush(heap, (new_time, nei))
        return max(dist.values()) if len(dist) == n else -1
