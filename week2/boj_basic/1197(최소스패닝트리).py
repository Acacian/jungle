import sys
input = sys.stdin.readline
V, E = map(int, input().split())
edges = []  # 간선 정보를 담을 공간

for i in range(E):
    a, b, w = map(int, input().split())
    edges.append((w, a, b))  # '간선 비용' 기준으로 정렬을 위해 (비용, 정점, 정점) 형태로 저장

def find_parent(x):  # 특정 원소가 속한 집합을 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):  # 두 원소가 속한 집합을 합치기
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(V+1)]  # 자기 자신을 부모로 갖는 서로소 집합
edges.sort()  # 간선 비용 기준 올림차순으로 정렬
result = 0

for w, a, b in edges: 
    if find_parent(a) != find_parent(b):  # 사이클이 생기지 않는다면
        union_parent(a, b)  # 간선 연결
        result += w  # 비용 계산

print(result)