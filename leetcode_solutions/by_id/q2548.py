# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2548
标题: Destroy Sequential Targets
难度: medium
链接: https://leetcode.cn/problems/destroy-sequential-targets/
题目类型: 数组、哈希表、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2453. 摧毁一系列目标 - 给你一个下标从 0 开始的数组 nums ，它包含若干正整数，表示数轴上你需要摧毁的目标所在的位置。同时给你一个整数 space 。 你有一台机器可以摧毁目标。给机器 输入 nums[i] ，这台机器会摧毁所有位置在 nums[i] + c * space 的目标，其中 c 是任意非负整数。你想摧毁 nums 中 尽可能多 的目标。 请你返回在摧毁数目最多的前提下，nums[i] 的 最小值 。 示例 1： 输入：nums = [3,7,8,1,1,5], space = 2 输出：1 解释：如果我们输入 nums[3] ，我们可以摧毁位于 1,3,5,7,9,... 这些位置的目标。 这种情况下， 我们总共可以摧毁 5 个目标（除了 nums[2]）。 没有办法摧毁多于 5 个目标，所以我们返回 nums[3] 。 示例 2： 输入：nums = [1,3,5,2,4,6], space = 2 输出：1 解释：输入 nums[0] 或者 nums[3] 都会摧毁 3 个目标。 没有办法摧毁多于 3 个目标。 由于 nums[0] 是最小的可以摧毁 3 个目标的整数，所以我们返回 1 。 示例 3： 输入：nums = [6,2,5], space = 100 输出：2 解释：无论我们输入哪个数字，都只能摧毁 1 个目标。输入的最小整数是 nums[1] 。 提示： * 1 <= nums.length <= 105 * 1 <= nums[i] <= 109 * 1 <= space <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表统计每个余数出现的次数，找到出现次数最多的余数对应的最小值。

算法步骤:
1. 计算每个 nums[i] 对 space 取模的结果，并统计每个余数出现的次数。
2. 找到出现次数最多的余数。
3. 在所有具有该余数的 nums[i] 中，找到最小的 nums[i]。

关键点:
- 使用哈希表高效统计余数出现的次数。
- 找到出现次数最多的余数后，再找到对应最小的 nums[i]。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(nums: List[int], space: int) -> int:
    """
    函数式接口 - 实现最优解法
    """
    # 统计每个余数出现的次数
    remainder_count = {}
    for num in nums:
        remainder = num % space
        if remainder not in remainder_count:
            remainder_count[remainder] = []
        remainder_count[remainder].append(num)

    # 找到出现次数最多的余数
    max_count = 0
    best_remainder = None
    for remainder, count in remainder_count.items():
        if len(count) > max_count:
            max_count = len(count)
            best_remainder = remainder

    # 在具有最多余数的 nums[i] 中找到最小的 nums[i]
    return min(remainder_count[best_remainder])


Solution = create_solution(solution_function_name)