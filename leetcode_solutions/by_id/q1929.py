# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1929
标题: Maximum Value at a Given Index in a Bounded Array
难度: medium
链接: https://leetcode.cn/problems/maximum-value-at-a-given-index-in-a-bounded-array/
题目类型: 贪心、数学、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1802. 有界数组中指定下标处的最大值 - 给你三个正整数 n、index 和 maxSum 。你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）： * nums.length == n * nums[i] 是 正整数 ，其中 0 <= i < n * abs(nums[i] - nums[i+1]) <= 1 ，其中 0 <= i < n-1 * nums 中所有元素之和不超过 maxSum * nums[index] 的值被 最大化 返回你所构造的数组中的 nums[index] 。 注意：abs(x) 等于 x 的前提是 x >= 0 ；否则，abs(x) 等于 -x 。 示例 1： 输入：n = 4, index = 2, maxSum = 6 输出：2 解释：数组 [1,1,2,1] 和 [1,2,2,1] 满足所有条件。不存在其他在指定下标处具有更大值的有效数组。 示例 2： 输入：n = 6, index = 1, maxSum = 10 输出：3 提示： * 1 <= n <= maxSum <= 109 * 0 <= index < n
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找来确定 nums[index] 的最大值。

算法步骤:
1. 初始化二分查找的左右边界 left 和 right。
2. 在每次迭代中，计算中间值 mid，并尝试构造一个以 mid 为峰值的数组。
3. 如果构造的数组总和不超过 maxSum，则说明 mid 可能是一个可行解，更新左边界 left。
4. 否则，更新右边界 right。
5. 最终返回 left - 1 作为结果。

关键点:
- 使用二分查找来缩小搜索范围。
- 计算以 mid 为峰值的数组总和时，需要考虑左侧和右侧的元素数目。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log(maxSum))
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(n: int, index: int, maxSum: int) -> int:
    """
    函数式接口 - 使用二分查找来确定 nums[index] 的最大值。
    """
    def get_sum(mid: int) -> int:
        # 计算以 mid 为峰值的数组总和
        left_sum = (mid + max(mid - index, 0)) * (min(index, mid) + 1) // 2
        right_sum = (mid + max(mid - (n - index - 1), 0)) * (min(n - index, mid) + 1) // 2
        return left_sum + right_sum - mid

    left, right = 1, maxSum
    while left < right:
        mid = (left + right + 1) // 2
        if get_sum(mid) <= maxSum:
            left = mid
        else:
            right = mid - 1

    return left


Solution = create_solution(solution_function_name)