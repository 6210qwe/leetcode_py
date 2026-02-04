# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3469
标题: Maximum Height of a Triangle
难度: easy
链接: https://leetcode.cn/problems/maximum-height-of-a-triangle/
题目类型: 数组、枚举
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3200. 三角形的最大高度 - 给你两个整数 red 和 blue，分别表示红色球和蓝色球的数量。你需要使用这些球来组成一个三角形，满足第 1 行有 1 个球，第 2 行有 2 个球，第 3 行有 3 个球，依此类推。 每一行的球必须是 相同 颜色，且相邻行的颜色必须 不同。 返回可以实现的三角形的 最大 高度。 示例 1： 输入： red = 2, blue = 4 输出： 3 解释： [https://assets.leetcode.com/uploads/2024/06/16/brb.png] 上图显示了唯一可能的排列方式。 示例 2： 输入： red = 2, blue = 1 输出： 2 解释： [https://assets.leetcode.com/uploads/2024/06/16/br.png] 上图显示了唯一可能的排列方式。 示例 3： 输入： red = 1, blue = 1 输出： 1 示例 4： 输入： red = 10, blue = 1 输出： 2 解释： [https://assets.leetcode.com/uploads/2024/06/16/br.png] 上图显示了唯一可能的排列方式。 提示： * 1 <= red, blue <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过二分查找确定最大高度，并检查是否可以构造出该高度的三角形。

算法步骤:
1. 使用二分查找确定最大高度。
2. 对于每个高度，检查是否可以用给定的红球和蓝球构造出该高度的三角形。
3. 如果可以构造，则更新最大高度；否则，减少高度。

关键点:
- 使用二分查找优化时间复杂度。
- 检查每一层所需球数是否满足条件。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log(max(red, blue)) * (log(max(red, blue))))
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(red: int, blue: int) -> int:
    """
    函数式接口 - 计算可以实现的三角形的最大高度
    """
    def can_form_triangle(height: int, red: int, blue: int) -> bool:
        total_balls = (height * (height + 1)) // 2
        if total_balls > red + blue:
            return False
        # 检查奇数行和偶数行
        for i in range(1, height + 1):
            if i % 2 == 1:
                if red < i:
                    return False
                red -= i
            else:
                if blue < i:
                    return False
                blue -= i
        return True

    low, high = 1, 100
    while low <= high:
        mid = (low + high) // 2
        if can_form_triangle(mid, red, blue):
            low = mid + 1
        else:
            high = mid - 1
    return high


Solution = create_solution(solution_function_name)