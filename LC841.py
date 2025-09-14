from collections import deque

class Solution(object):
    def canVisitAllRooms(self, rooms):
        visited = set([0])
        queue = deque([0])
        
        while queue:
            room = queue.popleft()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)
        
        return len(visited) == len(rooms)
