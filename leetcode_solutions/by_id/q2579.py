# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2579
标题: Minimum Split Into Subarrays With GCD Greater Than One
难度: medium
链接: https://leetcode.cn/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/
题目类型: 贪心、数组、数学、动态规划、数论
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2436. 使子数组最大公约数大于一的最小分割数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，尽量将具有公共因子的数放在同一个子数组中。

算法步骤:
1. 初始化一个计数器 `count` 为 0，表示当前子数组的数量。
2. 遍历数组 `nums`，对于每个元素 `num`：
   - 如果 `num` 是 1，则必须将其单独作为一个子数组，因为 1 与任何数的最大公约数都是 1。
   - 否则，检查当前子数组的最大公约数 `gcd` 是否大于 1。如果是，则将 `num` 加入当前子数组，并更新 `gcd`。
   - 如果 `gcd` 小于等于 1，则开始一个新的子数组，并将 `num` 加入其中。
3. 返回 `count` 作为结果。

关键点:
- 使用 `math.gcd` 函数计算两个数的最大公约数。
- 尽量将具有公共因子的数放在同一个子数组中，以减少子数组的数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log(max(nums)))，其中 n 是数组 `nums` 的长度，`log(max(nums))` 是计算最大公约数的时间复杂度。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import math
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(nums: List[int]) -> int:
    """
    函数式接口 - 使子数组最大公约数大于一的最小分割数
    """
    if not nums:
        return 0

    count = 0
    current_gcd = 0
    for num in nums:
        if num == 1:
            count += 1
            current_gcd = 0
        else:
            if current_gcd == 0:
                count += 1
                current_gcd = num
            else:
                current_gcd = math.gcd(current_gcd, num)

    return count


Solution = create_solution(solution_function_name)