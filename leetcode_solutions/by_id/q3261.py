# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3261
标题: Minimize OR of Remaining Elements Using Operations
难度: hard
链接: https://leetcode.cn/problems/minimize-or-of-remaining-elements-using-operations/
题目类型: 贪心、位运算、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3022. 给定操作次数内使剩余元素的或值最小 - 给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。 一次操作中，你可以选择 nums 中满足 0 <= i < nums.length - 1 的一个下标 i ，并将 nums[i] 和 nums[i + 1] 替换为数字 nums[i] & nums[i + 1] ，其中 & 表示按位 AND 操作。 请你返回 至多 k 次操作以内，使 nums 中所有剩余元素按位 OR 结果的 最小值 。 示例 1： 输入：nums = [3,5,3,2,7], k = 2 输出：3 解释：执行以下操作： 1. 将 nums[0] 和 nums[1] 替换为 (nums[0] & nums[1]) ，得到 nums 为 [1,3,2,7] 。 2. 将 nums[2] 和 nums[3] 替换为 (nums[2] & nums[3]) ，得到 nums 为 [1,3,2] 。 最终数组的按位或值为 3 。 3 是 k 次操作以内，可以得到的剩余元素的最小按位或值。 示例 2： 输入：nums = [7,3,15,14,2,8], k = 4 输出：2 解释：执行以下操作： 1. 将 nums[0] 和 nums[1] 替换为 (nums[0] & nums[1]) ，得到 nums 为 [3,15,14,2,8] 。 2. 将 nums[0] 和 nums[1] 替换为 (nums[0] & nums[1]) ，得到 nums 为 [3,14,2,8] 。 3. 将 nums[0] 和 nums[1] 替换为 (nums[0] & nums[1]) ，得到 nums 为 [2,2,8] 。 4. 将 nums[1] 和 nums[2] 替换为 (nums[1] & nums[2]) ，得到 nums 为 [2,0] 。 最终数组的按位或值为 2 。 2 是 k 次操作以内，可以得到的剩余元素的最小按位或值。 示例 3： 输入：nums = [10,7,10,3,9,14,9,4], k = 1 输出：15 解释：不执行任何操作，nums 的按位或值为 15 。 15 是 k 次操作以内，可以得到的剩余元素的最小按位或值。 提示： * 1 <= nums.length <= 105 * 0 <= nums[i] < 230 * 0 <= k < nums.length
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过贪心算法和位运算来最小化剩余元素的或值。

算法步骤:
1. 初始化一个变量 `result` 为 0，用于存储最终结果。
2. 从高位到低位（从第 29 位到第 0 位）遍历每一位。
3. 对于每一位，尝试将当前位设置为 0，并检查是否可以通过至多 k 次操作使得该位为 0。
4. 如果可以，则将 `result` 的当前位设为 0；否则，保持为 1。
5. 返回 `result`。

关键点:
- 使用位运算来逐位处理，确保在至多 k 次操作内尽可能减少或值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(30 * n) = O(n)，其中 n 是 nums 的长度。因为我们需要检查每一位（最多 30 位），并且每次检查需要遍历整个数组。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def minimize_or_of_remaining_elements(nums: List[int], k: int) -> int:
    """
    函数式接口 - 实现最优解法
    """
    result = 0
    for bit in range(29, -1, -1):
        count = 0
        new_nums = []
        for num in nums:
            if num & (1 << bit):
                count += 1
            else:
                if new_nums and count > 0:
                    new_nums[-1] &= num
                    count -= 1
                else:
                    new_nums.append(num)
        if count > 0:
            new_nums.extend([0] * count)
        if len(new_nums) > k + 1:
            result |= (1 << bit)
        nums = new_nums
    return result


Solution = create_solution(minimize_or_of_remaining_elements)