# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1511
标题: Count Number of Teams
难度: medium
链接: https://leetcode.cn/problems/count-number-of-teams/
题目类型: 树状数组、线段树、数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1395. 统计作战单位数 - n 名士兵站成一排。每个士兵都有一个 独一无二 的评分 rating 。 从中选出 3 个士兵组成一个作战单位，规则如下： * 从队伍中选出下标分别为 i、j、k 的 3 名士兵，他们的评分分别为 rating[i]、rating[j]、rating[k] * 作战单位需满足： rating[i] < rating[j] < rating[k] 或者 rating[i] > rating[j] > rating[k] ，其中 0 <= i < j < k < n 请你返回按上述条件组建的作战单位的方案数。 示例 1： 输入：rating = [2,5,3,4,1] 输出：3 解释：我们可以组建三个作战单位 (2,3,4)、(5,4,1)、(5,3,1) 。 示例 2： 输入：rating = [2,1,3] 输出：0 解释：根据题目条件，我们无法组建作战单位。 示例 3： 输入：rating = [1,2,3,4] 输出：4 提示： * n == rating.length * 3 <= n <= 1000 * 1 <= rating[i] <= 10^5 * rating 中的元素都是唯一的
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双重循环和前缀和来统计满足条件的三元组。

算法步骤:
1. 初始化两个数组 `left` 和 `right`，分别记录每个位置左侧和右侧比当前值小和大的数量。
2. 计算 `left` 数组：遍历 `rating` 数组，对于每个位置 `i`，计算其左侧比 `rating[i]` 小和大的数量。
3. 计算 `right` 数组：遍历 `rating` 数组，对于每个位置 `i`，计算其右侧比 `rating[i]` 小和大的数量。
4. 遍历 `rating` 数组，对于每个位置 `i`，使用 `left` 和 `right` 数组计算满足条件的三元组数量。

关键点:
- 使用前缀和优化计算过程，减少重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(rating: List[int]) -> int:
    """
    函数式接口 - 统计满足条件的三元组数量
    """
    n = len(rating)
    if n < 3:
        return 0

    # 初始化 left 和 right 数组
    left_less = [0] * n
    left_greater = [0] * n
    right_less = [0] * n
    right_greater = [0] * n

    # 计算 left 数组
    for i in range(n):
        for j in range(i):
            if rating[j] < rating[i]:
                left_less[i] += 1
            else:
                left_greater[i] += 1

    # 计算 right 数组
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if rating[j] < rating[i]:
                right_less[i] += 1
            else:
                right_greater[i] += 1

    # 计算满足条件的三元组数量
    count = 0
    for i in range(n):
        count += left_less[i] * right_greater[i]
        count += left_greater[i] * right_less[i]

    return count


Solution = create_solution(solution_function_name)