# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2628
标题: Minimize the Maximum of Two Arrays
难度: medium
链接: https://leetcode.cn/problems/minimize-the-maximum-of-two-arrays/
题目类型: 数学、二分查找、数论
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2513. 最小化两个数组中的最大值 - 给你两个数组 arr1 和 arr2 ，它们一开始都是空的。你需要往它们中添加正整数，使它们满足以下条件： * arr1 包含 uniqueCnt1 个 互不相同 的正整数，每个整数都 不能 被 divisor1 整除 。 * arr2 包含 uniqueCnt2 个 互不相同 的正整数，每个整数都 不能 被 divisor2 整除 。 * arr1 和 arr2 中的元素 互不相同 。 给你 divisor1 ，divisor2 ，uniqueCnt1 和 uniqueCnt2 ，请你返回两个数组中 最大元素 的 最小值 。 示例 1： 输入：divisor1 = 2, divisor2 = 7, uniqueCnt1 = 1, uniqueCnt2 = 3 输出：4 解释： 我们可以把前 4 个自然数划分到 arr1 和 arr2 中。 arr1 = [1] 和 arr2 = [2,3,4] 。 可以看出两个数组都满足条件。 最大值是 4 ，所以返回 4 。 示例 2： 输入：divisor1 = 3, divisor2 = 5, uniqueCnt1 = 2, uniqueCnt2 = 1 输出：3 解释： arr1 = [1,2] 和 arr2 = [3] 满足所有条件。 最大值是 3 ，所以返回 3 。 示例 3： 输入：divisor1 = 2, divisor2 = 4, uniqueCnt1 = 8, uniqueCnt2 = 2 输出：15 解释： 最终数组为 arr1 = [1,3,5,7,9,11,13,15] 和 arr2 = [2,6] 。 上述方案是满足所有条件的最优解。 提示： * 2 <= divisor1, divisor2 <= 105 * 1 <= uniqueCnt1, uniqueCnt2 < 109 * 2 <= uniqueCnt1 + uniqueCnt2 <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找来找到满足条件的最大值的最小值。

算法步骤:
1. 定义一个辅助函数 `is_valid` 来检查给定的最大值是否可以满足条件。
2. 使用二分查找来找到最小的最大值。
3. 在每次迭代中，计算中间值并使用 `is_valid` 函数来验证。

关键点:
- 使用二分查找来优化搜索过程。
- 计算不能被 divisor1 或 divisor2 整除的数的数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log(max(divisor1, divisor2) * (uniqueCnt1 + uniqueCnt2)))
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def is_valid(max_val, divisor1, divisor2, unique_cnt1, unique_cnt2):
    """
    检查给定的最大值是否可以满足条件。
    """
    count1 = max_val - max_val // divisor1
    count2 = max_val - max_val // divisor2
    common_count = max_val - max_val // (divisor1 * divisor2 // gcd(divisor1, divisor2))
    return count1 + count2 - common_count >= unique_cnt1 + unique_cnt2


def gcd(a, b):
    """
    计算两个数的最大公约数。
    """
    while b:
        a, b = b, a % b
    return a


def solution_function_name(divisor1, divisor2, unique_cnt1, unique_cnt2):
    """
    函数式接口 - 使用二分查找来找到满足条件的最大值的最小值。
    """
    left, right = 1, 10 ** 9
    while left < right:
        mid = (left + right) // 2
        if is_valid(mid, divisor1, divisor2, unique_cnt1, unique_cnt2):
            right = mid
        else:
            left = mid + 1
    return left


Solution = create_solution(solution_function_name)