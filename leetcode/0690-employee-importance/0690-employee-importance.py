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
        mp = {}

        # Store employees by id
        for emp in employees:
            mp[emp.id] = emp

        def dfs(emp_id):
            emp = mp[emp_id]
            total = emp.importance

            for sub_id in emp.subordinates:
                total += dfs(sub_id)

            return total

        return dfs(id)