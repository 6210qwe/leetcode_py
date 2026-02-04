# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1405
标题: All People Report to the Given Manager
难度: medium
链接: https://leetcode.cn/problems/all-people-report-to-the-given-manager/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1270. 向公司 CEO 汇报工作的所有人 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）来查找所有直接或间接向给定经理汇报的员工。

算法步骤:
1. 初始化一个队列，将给定经理加入队列。
2. 使用一个集合来记录已经访问过的员工，避免重复处理。
3. 开始广度优先搜索：
   - 从队列中取出一个员工。
   - 将该员工的所有直接下属加入队列，并标记为已访问。
4. 返回所有已访问的员工列表。

关键点:
- 使用队列和集合来实现高效的广度优先搜索。
- 确保每个员工只被处理一次，避免重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是员工的数量。每个员工最多只会被处理一次。
空间复杂度: O(n)，最坏情况下，队列和集合中会包含所有员工。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(manager_id: int, manager: List[int]) -> List[int]:
    """
    函数式接口 - 实现最优解法
    """
    from collections import deque
    
    # 初始化队列和访问集合
    queue = deque([manager_id])
    visited = set()
    
    while queue:
        current_manager = queue.popleft()
        if current_manager not in visited:
            visited.add(current_manager)
            for i, m in enumerate(manager):
                if m == current_manager:
                    queue.append(i)
    
    return list(visited)


Solution = create_solution(solution_function_name)