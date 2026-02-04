# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3746
标题: Find Circular Gift Exchange Chains
难度: hard
链接: https://leetcode.cn/problems/find-circular-gift-exchange-chains/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3401. 寻找环形礼物交换链 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）来查找环形礼物交换链。

算法步骤:
1. 使用一个字典 `gifts` 来记录每个礼物的接收者。
2. 对于每个礼物，使用 DFS 进行搜索，同时使用一个集合 `visited` 来记录当前路径上的节点。
3. 如果在 DFS 过程中遇到已经访问过的节点，则说明找到了一个环。
4. 返回所有找到的环。

关键点:
- 使用 DFS 进行环检测。
- 使用集合 `visited` 来记录当前路径上的节点，以避免重复访问。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是礼物的数量。每个节点和边最多访问一次。
空间复杂度: O(n)，递归调用栈和 `visited` 集合的空间开销。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(gifts: List[List[int]]) -> List[List[int]]:
    """
    函数式接口 - 找到所有的环形礼物交换链
    """
    # 构建礼物接收者的字典
    gift_dict = {giver: receiver for giver, receiver in gifts}
    
    def dfs(node: int, path: List[int], visited: set) -> None:
        if node in visited:
            # 找到环
            cycle_start = path.index(node)
            result.append(path[cycle_start:])
            return
        if node in path or node not in gift_dict:
            return
        visited.add(node)
        path.append(node)
        dfs(gift_dict[node], path, visited)
        path.pop()
        visited.remove(node)
    
    result = []
    visited = set()
    for giver in gift_dict:
        if giver not in visited:
            dfs(giver, [], visited)
    
    return result


Solution = create_solution(solution_function_name)