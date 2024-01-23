import heapq

memo = {}
def fibo(n):
    if n == 1 or n == 2:
        return 1
    if n not in memo:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

# 가중치가 있을 때 > 다익스트라 (우선순위 큐) + 가중치 그래프

def dijkstra(graph, start, final, n):
    costs = {}
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_cost, cur_v = heapq.heappop(pq)
        if cur_v not in costs:
            costs[cur_v] = cur_cost
            for cost, next_v in graph[cur_v]:
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_v))
    return costs[final]

graph = {...}
dijkstra(graph, 1, 8)
