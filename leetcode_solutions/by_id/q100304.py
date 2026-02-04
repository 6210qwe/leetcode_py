# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100304
标题: 连续天数的最高销售额
难度: easy
链接: https://leetcode.cn/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/
题目类型: 数组、分治、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 161. 连续天数的最高销售额 - 某公司每日销售额记于整数数组 sales，请返回所有 连续 一或多天销售额总和的最大值。 要求实现时间复杂度为 O(n) 的算法。 示例 1： 输入：sales = [-2,1,-3,4,-1,2,1,-5,4] 输出：6 解释：[4,-1,2,1] 此连续四天的销售总额最高，为 6。 示例 2： 输入：sales = [5,4,-1,7,8] 输出：23 解释：[5,4,-1,7,8] 此连续五天的销售总额最高，为 23。 提示： * 1 <= arr.length <= 10^5 * -100 <= arr[i] <= 100 注意：本题与主站 53 题相同：https://leetcode.cn/problems/maximum-subarray/ [https://leetcode.cn/problems/maximum-subarray/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用Kadane算法来找到最大子数组和。

算法步骤:
1. 初始化两个变量：当前子数组和 `current_sum` 和最大子数组和 `max_sum`。
2. 遍历数组，对于每个元素，更新 `current_sum` 为当前元素和 `current_sum + 当前元素` 中的较大值。
3. 更新 `max_sum` 为 `max_sum` 和 `current_sum` 中的较大值。
4. 返回 `max_sum`。

关键点:
- Kadane算法的时间复杂度为O(n)，空间复杂度为O(1)。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(sales: List[int]) -> int:
    """
    函数式接口 - 使用Kadane算法找到最大子数组和
    """
    if not sales:
        return 0

    current_sum = max_sum = sales[0]

    for i in range(1, len(sales)):
        current_sum = max(sales[i], current_sum + sales[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


Solution = create_solution(solution_function_name)