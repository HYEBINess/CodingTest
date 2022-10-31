def findCenter(edges: list[list[int]]) -> int: # -> int는 반환값을 int로 한다는 힌트
    f=edges[0][0]
    s=edges[0][1]
    if(f in edges[1]):
        return f
    else:
        return s

print(findCenter([[1,2],[2,3],[4,2]]))
