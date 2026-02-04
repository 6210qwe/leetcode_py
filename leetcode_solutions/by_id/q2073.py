# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2073
标题: Minimum Time For K Virus Variants to Spread
难度: hard
链接: https://leetcode.cn/problems/minimum-time-for-k-virus-variants-to-spread/
题目类型: 几何、数组、数学、二分查找、枚举
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1956. 感染 K 种病毒所需的最短时间 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找和广度优先搜索（BFS）来确定最小时间。

算法步骤:
1. 初始化二分查找的左右边界，左边界为0，右边界为网格的最大值。
2. 在二分查找的过程中，使用BFS来检查在当前时间t内是否可以感染至少k个位置。
3. 如果可以，则尝试更小的时间；否则，尝试更大的时间。
4. 最终返回最小的时间。

关键点:
- 使用二分查找来缩小时间范围。
- 使用BFS来模拟病毒的传播过程。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m * log(max_time))，其中n和m是网格的行数和列数，max_time是网格中的最大值。
空间复杂度: O(n * m)，用于存储BFS的队列和访问标记。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def minTimeToSpread(grid: List[List[int]], k: int) -> int:
    """
    函数式接口 - 计算感染K种病毒所需的最短时间
    """
    n, m = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def can_infect(t: int) -> bool:
        infected = set()
        queue = []
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] <= t:
                    infected.add((i, j))
                    queue.append((i, j))
        
        while queue:
            x, y = queue.pop(0)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in infected and grid[nx][ny] <= t + 1:
                    infected.add((nx, ny))
                    queue.append((nx, ny))
        
        return len(infected) >= k
    
    left, right = 0, max(max(row) for row in grid)
    while left < right:
        mid = (left + right) // 2
        if can_infect(mid):
            right = mid
        else:
            left = mid + 1
    
    return left


Solution = create_solution(minTimeToSpread)