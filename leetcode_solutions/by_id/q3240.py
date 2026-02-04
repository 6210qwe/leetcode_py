# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3240
标题: Maximum Number That Sum of the Prices Is Less Than or Equal to K
难度: medium
链接: https://leetcode.cn/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/
题目类型: 位运算、数学、二分查找、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3007. 价值和小于等于 K 的最大数字 - 给你一个整数 k 和一个整数 x 。整数 num 的价值是它的二进制表示中在 x，2x，3x 等位置处 设置位 的数目（从最低有效位开始）。下面的表格包含了如何计算价值的例子。 x num Binary Representation Price 1 13 000001101 3 2 13 000001101 1 2 233 011101001 3 3 13 000001101 1 3 362 101101010 2 num 的 累加价值 是从 1 到 num 的数字的 总 价值。如果 num 的累加价值小于或等于 k 则被认为是 廉价 的。 请你返回 最大 的廉价数字。 示例 1： 输入：k = 9, x = 1 输出：6 解释：由下表所示，6 是最大的廉价数字。 x num Binary Representation Price Accumulated Price 1 1 001 1 1 1 2 010 1 2 1 3 011 2 4 1 4 100 1 5 1 5 101 2 7 1 6 110 2 9 1 7 111 3 12 示例 2： 输入：k = 7, x = 2 输出：9 解释：由下表所示，9 是最大的廉价数字。 x num Binary Representation Price Accumulated Price 2 1 0001 0 0 2 2 0010 1 1 2 3 0011 1 2 2 4 0100 0 2 2 5 0101 0 2 2 6 0110 1 3 2 7 0111 1 4 2 8 1000 1 5 2 9 1001 1 6 2 10 1010 2 8 提示： * 1 <= k <= 1015 * 1 <= x <= 8
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找来找到最大的廉价数字。对于每个中间值，计算其累加价值，并根据累加价值调整二分查找的范围。

算法步骤:
1. 初始化二分查找的左右边界。
2. 在二分查找的过程中，计算中间值的累加价值。
3. 根据累加价值调整二分查找的范围，直到找到最大的廉价数字。

关键点:
- 使用位运算来高效计算每个数字的价值。
- 通过二分查找来减少搜索空间。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log(n) * log(n))，其中 n 是可能的最大值（即 10^15），每次二分查找需要 O(log(n)) 次迭代，每次迭代需要 O(log(n)) 时间来计算累加价值。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(k: int, x: int) -> int:
    """
    函数式接口 - 返回最大的廉价数字
    """
    def calculate_price(num: int) -> int:
        price = 0
        for i in range(x, 64, x):
            if (num & (1 << i)) != 0:
                price += 1
        return price

    def accumulate_price(num: int) -> int:
        total_price = 0
        for i in range(1, num + 1):
            total_price += calculate_price(i)
        return total_price

    left, right = 0, 10**15
    while left < right:
        mid = (left + right + 1) // 2
        if accumulate_price(mid) <= k:
            left = mid
        else:
            right = mid - 1
    return left


Solution = create_solution(solution_function_name)