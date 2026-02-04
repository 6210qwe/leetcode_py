# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2205
标题: Find Good Days to Rob the Bank
难度: medium
链接: https://leetcode.cn/problems/find-good-days-to-rob-the-bank/
题目类型: 数组、动态规划、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2100. 适合野炊的日子 - 你和朋友们准备去野炊。给你一个下标从 0 开始的整数数组 security ，其中 security[i] 是第 i 天的建议出行指数。日子从 0 开始编号。同时给你一个整数 time 。 如果第 i 天满足以下所有条件，我们称它为一个适合野炊的日子： * 第 i 天前和后都分别至少有 time 天。 * 第 i 天前连续 time 天建议出行指数都是非递增的。 * 第 i 天后连续 time 天建议出行指数都是非递减的。 更正式的，第 i 天是一个适合野炊的日子当且仅当：security[i - time] >= security[i - time + 1] >= ... >= security[i] <= ... <= security[i + time - 1] <= security[i + time]. 请你返回一个数组，包含 所有 适合野炊的日子（下标从 0 开始）。返回的日子可以 任意 顺序排列。 示例 1： 输入：security = [5,3,3,3,5,6,2], time = 2 输出：[2,3] 解释： 第 2 天，我们有 security[0] >= security[1] >= security[2] <= security[3] <= security[4] 。 第 3 天，我们有 security[1] >= security[2] >= security[3] <= security[4] <= security[5] 。 没有其他日子符合这个条件，所以日子 2 和 3 是适合野炊的日子。 示例 2： 输入：security = [1,1,1,1,1], time = 0 输出：[0,1,2,3,4] 解释： 因为 time 等于 0 ，所以每一天都是适合野炊的日子，所以返回每一天。 示例 3： 输入：security = [1,2,3,4,5,6], time = 2 输出：[] 解释： 没有任何一天的前 2 天建议出行指数是非递增的。 所以没有适合野炊的日子，返回空数组。 提示： * 1 <= security.length <= 105 * 0 <= security[i], time <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划预处理出每个位置的前缀非递增天数和后缀非递减天数。

算法步骤:
1. 初始化两个数组 `non_increasing` 和 `non_decreasing`，分别记录每个位置的前缀非递增天数和后缀非递减天数。
2. 从左到右遍历数组，计算每个位置的前缀非递增天数。
3. 从右到左遍历数组，计算每个位置的后缀非递减天数。
4. 遍历数组，找到满足条件的位置，即 `non_increasing[i] >= time` 且 `non_decreasing[i] >= time` 的位置。

关键点:
- 使用动态规划预处理前缀和后缀数组，避免重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 security 的长度。需要遍历数组三次。
空间复杂度: O(n)，需要额外的两个数组来存储前缀和后缀信息。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_good_days_to_rob_bank(security: List[int], time: int) -> List[int]:
    """
    函数式接口 - 找到所有适合野炊的日子
    """
    n = len(security)
    if n < 2 * time + 1:
        return []

    non_increasing = [0] * n
    non_decreasing = [0] * n

    # 计算前缀非递增天数
    for i in range(1, n):
        if security[i] <= security[i - 1]:
            non_increasing[i] = non_increasing[i - 1] + 1

    # 计算后缀非递减天数
    for i in range(n - 2, -1, -1):
        if security[i] <= security[i + 1]:
            non_decreasing[i] = non_decreasing[i + 1] + 1

    # 找到满足条件的位置
    good_days = []
    for i in range(time, n - time):
        if non_increasing[i] >= time and non_decreasing[i] >= time:
            good_days.append(i)

    return good_days


Solution = create_solution(find_good_days_to_rob_bank)