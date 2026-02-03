# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 473
标题: Matchsticks to Square
难度: medium
链接: https://leetcode.cn/problems/matchsticks-to-square/
题目类型: 位运算、数组、动态规划、回溯、状态压缩
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
473. 火柴拼正方形 - 你将得到一个整数数组 matchsticks ，其中 matchsticks[i] 是第 i 个火柴棒的长度。你要用 所有的火柴棍 拼成一个正方形。你 不能折断 任何一根火柴棒，但你可以把它们连在一起，而且每根火柴棒必须 使用一次 。 如果你能使这个正方形，则返回 true ，否则返回 false 。 示例 1: [https://assets.leetcode.com/uploads/2021/04/09/matchsticks1-grid.jpg] 输入: matchsticks = [1,1,2,2,2] 输出: true 解释: 能拼成一个边长为2的正方形，每边两根火柴。 示例 2: 输入: matchsticks = [3,3,3,3,4] 输出: false 解释: 不能用所有火柴拼成一个正方形。 提示: * 1 <= matchsticks.length <= 15 * 1 <= matchsticks[i] <= 108
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 回溯算法，将火柴分配到四条边

算法步骤:
1. 计算总长度，判断是否能组成正方形
2. 使用回溯，尝试将每根火柴分配到四条边
3. 剪枝：如果某条边超过目标长度，跳过

关键点:
- 回溯+剪枝
- 时间复杂度O(4^n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(4^n) - 每根火柴有4种选择
空间复杂度: O(n) - 递归栈空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def matchsticks_to_square(matchsticks: List[int]) -> bool:
    """
    函数式接口 - 火柴拼正方形
    
    实现思路:
    回溯算法：将火柴分配到四条边。
    
    Args:
        matchsticks: 火柴长度数组
        
    Returns:
        是否能拼成正方形
        
    Example:
        >>> matchsticks_to_square([1,1,2,2,2])
        True
    """
    total = sum(matchsticks)
    if total % 4 != 0:
        return False
    
    target = total // 4
    matchsticks.sort(reverse=True)  # 从大到小排序，加速剪枝
    
    sides = [0] * 4
    
    def backtrack(index: int) -> bool:
        """回溯函数"""
        if index == len(matchsticks):
            return all(side == target for side in sides)
        
        for i in range(4):
            if sides[i] + matchsticks[index] <= target:
                sides[i] += matchsticks[index]
                if backtrack(index + 1):
                    return True
                sides[i] -= matchsticks[index]
                # 剪枝：如果当前边为0，说明这是第一次尝试，如果失败，后续尝试也会失败
                if sides[i] == 0:
                    break
        
        return False
    
    return backtrack(0)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(matchsticks_to_square)
