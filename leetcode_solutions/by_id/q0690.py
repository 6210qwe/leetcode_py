# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 690
标题: Employee Importance
难度: medium
链接: https://leetcode.cn/problems/employee-importance/
题目类型: 树、深度优先搜索、广度优先搜索、数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
690. 员工的重要性 - 你有一个保存员工信息的数据结构，它包含了员工唯一的 id ，重要度和直系下属的 id 。 给定一个员工数组 employees，其中： * employees[i].id 是第 i 个员工的 ID。 * employees[i].importance 是第 i 个员工的重要度。 * employees[i].subordinates 是第 i 名员工的直接下属的 ID 列表。 给定一个整数 id 表示一个员工的 ID，返回这个员工和他所有下属的重要度的 总和。 示例 1： [https://pic.leetcode.cn/1716170448-dKZffb-image.png] 输入：employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1 输出：11 解释： 员工 1 自身的重要度是 5 ，他有两个直系下属 2 和 3 ，而且 2 和 3 的重要度均为 3 。因此员工 1 的总重要度是 5 + 3 + 3 = 11 。 示例 2： [https://pic.leetcode.cn/1716170929-dkWpra-image.png] 输入：employees = [[1,2,[5]],[5,-3,[]]], id = 5 输出：-3 解释：员工 5 的重要度为 -3 并且没有直接下属。 因此，员工 5 的总重要度为 -3。 提示： * 1 <= employees.length <= 2000 * 1 <= employees[i].id <= 2000 * 所有的 employees[i].id 互不相同。 * -100 <= employees[i].importance <= 100 * 一名员工最多有一名直接领导，并可能有多名下属。 * employees[i].subordinates 中的 ID 都有效。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）来遍历员工及其下属，计算总重要度。

算法步骤:
1. 将员工列表转换为以ID为键的字典，以便快速查找。
2. 定义一个递归函数 `dfs` 来计算某个员工及其所有下属的总重要度。
3. 在 `dfs` 函数中，累加当前员工的重要度，并递归地处理其所有下属。
4. 返回给定ID员工的总重要度。

关键点:
- 使用字典存储员工信息，以便快速查找。
- 通过递归DFS遍历所有下属，确保每个员工的重要度都被计算一次。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是员工的数量。每个员工及其下属只被访问一次。
空间复杂度: O(n)，用于存储员工字典和递归调用栈。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

def get_total_importance(employees: List[Employee], id: int) -> int:
    """
    计算给定ID员工及其所有下属的总重要度。
    """
    # 将员工列表转换为以ID为键的字典
    employee_dict = {emp.id: emp for emp in employees}
    
    def dfs(emp_id: int) -> int:
        """
        递归函数，计算某个员工及其所有下属的总重要度。
        """
        emp = employee_dict[emp_id]
        total_importance = emp.importance
        for subordinate in emp.subordinates:
            total_importance += dfs(subordinate)
        return total_importance
    
    return dfs(id)

Solution = create_solution(get_total_importance)