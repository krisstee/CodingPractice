import collections
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        if employees == []:
            return 0

        # Map employees
        emap = {}
        for employee in employees:
            emap[employee.id] = (employee.importance, employee.subordinates)

        equeue = collections.deque()

        if(id in emap):
            equeue.append(emap[id])
        else:
            return 0

        ans = 0

        while(len(equeue) != 0):
            emp = equeue.popleft()
            ans += emp[0]
            for sub in emp[1]:
                equeue.appendleft(emap[sub])

        return(ans)
"""
Initial thoughts:
- Ways to represent relationship could be: hash map
{int: (int, List[int])}
{1: (5, [2, 3]), 2: (3, [3]), 3: (3, [])}

Approach:
- Map employees
- Create a queue for subordinates
- Start at id given and queue up subordinates
- For a employee at the start of the queue, queue up their subordinates in the front
- Add importance value

Things I'll need:
A variable to track the importance value


Possible input:
[[1, 5, [2, 3]], [2, 3, [3]], [3, 3, []]]
[[2, 3, []], [3, 3, []], [1, 5, [2, 3]]]
[]
[1, 4, []]
"""
