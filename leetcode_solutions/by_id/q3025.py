# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3025
标题: Minimum Operations to Form Subsequence With Target Sum
难度: hard
链接: https://leetcode.cn/problems/minimum-operations-to-form-subsequence-with-target-sum/
题目类型: 贪心、位运算、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2835. 使子序列的和等于目标的最少操作次数 - 给你一个下标从 0 开始的数组 nums ，它包含 非负 整数，且全部为 2 的幂，同时给你一个整数 target 。 一次操作中，你必须对数组做以下修改： * 选择数组中一个元素 nums[i] ，满足 nums[i] > 1 。 * 将 nums[i] 从数组中删除。 * 在 nums 的 末尾 添加 两个 数，值都为 nums[i] / 2 。 你的目标是让 nums 的一个 子序列 的元素和等于 target ，请你返回达成这一目标的 最少操作次数 。如果无法得到这样的子序列，请你返回 -1 。 数组中一个 子序列 是通过删除原数组中一些元素，并且不改变剩余元素顺序得到的剩余数组。 示例 1： 输入：nums = [1,2,8], target = 7 输出：1 解释：第一次操作中，我们选择元素 nums[2] 。数组变为 nums = [1,2,4,4] 。 这时候，nums 包含子序列 [1,2,4] ，和为 7 。 无法通过更少的操作得到和为 7 的子序列。 示例 2： 输入：nums = [1,32,1,2], target = 12 输出：2 解释：第一次操作中，我们选择元素 nums[1] 。数组变为 nums = [1,1,2,16,16] 。 第二次操作中，我们选择元素 nums[3] 。数组变为 nums = [1,1,2,16,8,8] 。 这时候，nums 包含子序列 [1,1,2,8] ，和为 12 。 无法通过更少的操作得到和为 12 的子序列。 示例 3： 输入：nums = [1,32,1], target = 35 输出：-1 解释：无法得到和为 35 的子序列。 提示： * 1 <= nums.length <= 1000 * 1 <= nums[i] <= 230 * nums 只包含非负整数，且均为 2 的幂。 * 1 <= target < 231
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和位运算来计算最少操作次数。

算法步骤:
1. 统计每个 2 的幂在 `nums` 中出现的次数。
2. 从低位到高位检查 `target` 的每一位是否可以在 `nums` 中找到对应的 2 的幂。
3. 如果当前位需要的 2 的幂不足，则从更高位借位，并记录操作次数。
4. 如果最终无法满足 `target`，则返回 -1。

关键点:
- 使用位运算来高效地处理 2 的幂。
- 贪心地从低位到高位处理 `target` 的每一位。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + log(target))
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_operations(nums: List[int], target: int) -> int:
    """
    计算使子序列的和等于目标的最少操作次数。
    """
    # 统计每个 2 的幂在 nums 中出现的次数
    count = [0] * 31
    for num in nums:
        count[num.bit_length() - 1] += 1

    # 计算总和
    total_sum = sum(nums)

    if total_sum < target:
        return -1

    operations = 0
    current_sum = 0

    for i in range(31):
        if (target >> i) & 1:
            # 当前位需要 2^i
            if count[i] > 0:
                count[i] -= 1
                current_sum += 1 << i
            else:
                # 从更高位借位
                j = i + 1
                while j < 31 and count[j] == 0:
                    j += 1
                if j == 31:
                    return -1
                operations += j - i
                count[j] -= 1
                for k in range(i, j):
                    count[k] += 1
                current_sum += 1 << i

    return operations


Solution = create_solution(min_operations)