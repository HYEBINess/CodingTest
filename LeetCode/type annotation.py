# 리스트의 모든 값 합하는 함수

# Version_1
from typing import List

def getSum(edges: List[List[int]]) -> int:
    for i in range(len(edges)):
        return [sum(edges[i]) for edges[i] in edges]

print(getSum([[1,2],[2,3],[4,2]]))

# Version_2 : 3.9   이상부터 import 안해줘도 됨.

def getSum(edges: list[list[int]]) -> int:
    for i in range(len(edges)):
        return [sum(edges[i]) for edges[i] in edges]

print(getSum([[1,2],[2,3],[4,2]]))