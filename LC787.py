class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        INF = float("inf")
        # Distance array for current and previous iteration
        dist = [INF] * n
        dist[src] = 0

        # Relax edges up to k+1 times (because k stops = k+1 edges)
        for _ in range(k + 1):
            new_dist = dist[:]  # copy from previous state
            for u, v, w in flights:
                if dist[u] != INF and dist[u] + w < new_dist[v]:
                    new_dist[v] = dist[u] + w
            dist = new_dist

        return -1 if dist[dst] == INF else dist[dst]
