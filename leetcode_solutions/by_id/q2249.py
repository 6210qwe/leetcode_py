# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2249
标题: Count the Hidden Sequences
难度: medium
链接: https://leetcode.cn/problems/count-the-hidden-sequences/
题目类型: 数组、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2145. 统计隐藏数组数目 - 给你一个下标从 0 开始且长度为 n 的整数数组 differences ，它表示一个长度为 n + 1 的 隐藏 数组 相邻 元素之间的 差值 。更正式的表述为：我们将隐藏数组记作 hidden ，那么 differences[i] = hidden[i + 1] - hidden[i] 。 同时给你两个整数 lower 和 upper ，它们表示隐藏数组中所有数字的值都在 闭 区间 [lower, upper] 之间。 * 比方说，differences = [1, -3, 4] ，lower = 1 ，upper = 6 ，那么隐藏数组是一个长度为 4 且所有值都在 1 和 6 （包含两者）之间的数组。 * [3, 4, 1, 5] 和 [4, 5, 2, 6] 都是符合要求的隐藏数组。 * [5, 6, 3, 7] 不符合要求，因为它包含大于 6 的元素。 * [1, 2, 3, 4] 不符合要求，因为相邻元素的差值不符合给定数据。 请你返回 符合 要求的隐藏数组的数目。如果没有符合要求的隐藏数组，请返回 0 。 示例 1： 输入：differences = [1,-3,4], lower = 1, upper = 6 输出：2 解释：符合要求的隐藏数组为： - [3, 4, 1, 5] - [4, 5, 2, 6] 所以返回 2 。 示例 2： 输入：differences = [3,-4,5,1,-2], lower = -4, upper = 5 输出：4 解释：符合要求的隐藏数组为： - [-3, 0, -4, 1, 2, 0] - [-2, 1, -3, 2, 3, 1] - [-1, 2, -2, 3, 4, 2] - [0, 3, -1, 4, 5, 3] 所以返回 4 。 示例 3： 输入：differences = [4,-7,2], lower = 3, upper = 6 输出：0 解释：没有符合要求的隐藏数组，所以返回 0 。 提示： * n == differences.length * 1 <= n <= 105 * -105 <= differences[i] <= 105 * -105 <= lower <= upper <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
- 通过前缀和计算隐藏数组的变化范围。
- 确定初始值的范围，使得整个隐藏数组的值都在 [lower, upper] 之间。

算法步骤:
1. 计算前缀和数组 `prefix_sum`，其中 `prefix_sum[i]` 表示从 `hidden[0]` 到 `hidden[i]` 的累积差值。
2. 找到 `prefix_sum` 中的最大值 `max_prefix` 和最小值 `min_prefix`。
3. 计算初始值 `hidden[0]` 的有效范围，使得 `hidden[0] + min_prefix >= lower` 且 `hidden[0] + max_prefix <= upper`。
4. 返回满足条件的 `hidden[0]` 的数量。

关键点:
- 通过前缀和来确定隐藏数组的变化范围。
- 通过计算初始值的有效范围来确定符合条件的隐藏数组的数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 differences 的长度。我们需要遍历一次 differences 来计算前缀和。
空间复杂度: O(1)，除了输入和输出外，我们只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_hidden_sequences(differences: List[int], lower: int, upper: int) -> int:
    """
    计算符合要求的隐藏数组的数目。

    :param differences: 整数数组，表示隐藏数组相邻元素之间的差值。
    :param lower: 隐藏数组中所有数字的最小值。
    :param upper: 隐藏数组中所有数字的最大值。
    :return: 符合要求的隐藏数组的数目。
    """
    current_sum = 0
    min_prefix = 0
    max_prefix = 0
    
    for diff in differences:
        current_sum += diff
        min_prefix = min(min_prefix, current_sum)
        max_prefix = max(max_prefix, current_sum)
    
    # 计算初始值 hidden[0] 的有效范围
    min_start = lower - min_prefix
    max_start = upper - max_prefix
    
    # 返回满足条件的 hidden[0] 的数量
    return max(0, max_start - min_start + 1)


Solution = create_solution(count_hidden_sequences)