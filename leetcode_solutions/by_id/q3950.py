# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3950
标题: Maximum K to Sort a Permutation
难度: medium
链接: https://leetcode.cn/problems/maximum-k-to-sort-a-permutation/
题目类型: 位运算、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3644. 排序排列 - 给你一个长度为 n 的整数数组 nums，其中 nums 是范围 [0..n - 1] 内所有数字的一个 排列 。 你可以在满足条件 nums[i] AND nums[j] == k 的情况下交换下标 i 和 j 的元素，其中 AND 表示按位与操作，k 是一个非负整数。 返回可以使数组按 非递减 顺序排序的最大值 k（允许进行任意次这样的交换）。如果 nums 已经是有序的，返回 0。 排列 是数组所有元素的一种重新排列。 示例 1： 输入：nums = [0,3,2,1] 输出：1 解释： 选择 k = 1。交换 nums[1] = 3 和 nums[3] = 1，因为 nums[1] AND nums[3] == 1，从而得到一个排序后的排列：[0, 1, 2, 3]。 示例 2： 输入：nums = [0,1,3,2] 输出：2 解释： 选择 k = 2。交换 nums[2] = 3 和 nums[3] = 2，因为 nums[2] AND nums[3] == 2，从而得到一个排序后的排列：[0, 1, 2, 3]。 示例 3： 输入：nums = [3,2,1,0] 输出：0 解释： 只有当 k = 0 时，才能进行排序，因为没有更大的 k 能够满足 nums[i] AND nums[j] == k 的交换条件。 提示： * 1 <= n == nums.length <= 105 * 0 <= nums[i] <= n - 1 * nums 是从 0 到 n - 1 的一个排列。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用位运算和贪心算法找到最大可能的 k 值。

算法步骤:
1. 检查数组是否已经排序，如果是则返回 0。
2. 构建一个字典，记录每个元素的位置。
3. 从最高位到最低位遍历每一位，尝试找到可以交换的 k 值。
4. 如果找到一个 k 值使得数组可以排序，则返回该 k 值。

关键点:
- 使用位运算来检查和交换元素。
- 通过贪心算法找到最大的 k 值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是数组的长度。需要遍历每一位，并且在最坏情况下需要对每一位进行检查。
空间复杂度: O(n)，需要额外的空间来存储每个元素的位置。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(nums: List[int]) -> int:
    """
    函数式接口 - 找到可以使数组按非递减顺序排序的最大值 k
    """
    n = len(nums)
    if nums == list(range(n)):
        return 0

    # 构建位置字典
    pos = {num: i for i, num in enumerate(nums)}

    # 从最高位到最低位遍历每一位
    for bit in range(17, -1, -1):
        k = 0
        for i in range(bit, -1, -1):
            if (1 << i) & k == 0:
                k |= 1 << i
                new_nums = [num for num in nums]
                for j in range(n):
                    if (new_nums[j] & k) != (j & k):
                        new_pos = pos[(j & k) ^ (new_nums[j] & k)]
                        new_nums[j], new_nums[new_pos] = new_nums[new_pos], new_nums[j]
                        pos[new_nums[j]], pos[new_nums[new_pos]] = pos[new_nums[new_pos]], pos[new_nums[j]]
                if new_nums == list(range(n)):
                    return k
    return 0


Solution = create_solution(solution_function_name)