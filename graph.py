'''
그래프의 연결관계 표현 방식 2가지.

graph ex)
    0
 (7) (5)
1       2


- 인접 행렬(Adjacency Matrix) # 데이터에 비용만이 존재, 노드 관계는 인덱스가 나타낸다.
                             # 모든 연결관계를 표현하므로 메모리 낭비가 크다. 하지만 어떤 연결관계에 대한 정보를 얻는 속도가 빠르다.

INF = 999999999 # 연결 안된 노드끼리는 무한의 비용으로 정의, 자기자신과의 관계는 0.

graph = [[0, 7, 5], [7, 0, INF], [5, INF, 0]] # 노드의 모든 연결관계 2차원 리스트(배열)로 표현. 



- 인접 리스트(Adjacency List) # 데이터에 (목표 노드, 비용)이 존재.
                             # 연결되어 있는 관계만을 표현하므로 메모리 낭비가 없다. 하지만 어떤 연결관계에 대해 정보를 얻는 속도가 느리다
                             # 특정한 노드와 연결된 모든 인접 노드를 순회해야 하는 경우 유리하다. (인접 리스트 방식은 어차피 순회해야 하므로)

graph = [[] for _ in range(3)] # 노드의 연결관계 2차원 리스트(연결 리스트)로 표현.

graph[0].append((1, 7)) # 노드 0에 연결된 연결관계 삽입
graph[0].append((2, 5))
graph[1].append((0, 7)) # 노드 1에
graph[2].append((0, 5)) # 노드 2에

'''

