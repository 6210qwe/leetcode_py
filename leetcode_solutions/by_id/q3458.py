# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3458
标题: Maximum Number of Upgradable Servers
难度: medium
链接: https://leetcode.cn/problems/maximum-number-of-upgradable-servers/
题目类型: 数组、数学、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3155. 可升级服务器的最大数量 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和二分查找来最大化可升级的服务器数量。

算法步骤:
1. 计算每个服务器的升级成本。
2. 对服务器按升级成本进行排序。
3. 使用二分查找确定最大可升级的服务器数量。

关键点:
- 通过贪心算法选择升级成本最低的服务器。
- 使用二分查找优化时间复杂度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(servers: List[int], upgrade_cost: int, budget: int) -> int:
    """
    函数式接口 - 实现最优解法
    """
    # 计算每个服务器的升级成本
    costs = [upgrade_cost - server for server in servers]
    
    # 按升级成本进行排序
    costs.sort()
    
    # 使用二分查找确定最大可升级的服务器数量
    left, right = 0, len(servers)
    while left < right:
        mid = (left + right) // 2
        if sum(costs[:mid]) <= budget:
            left = mid + 1
        else:
            right = mid
    
    return left - 1


Solution = create_solution(solution_function_name)