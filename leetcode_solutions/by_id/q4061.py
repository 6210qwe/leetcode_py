# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 4061
标题: Minimum Swaps to Avoid Forbidden Values
难度: hard
链接: https://leetcode.cn/problems/minimum-swaps-to-avoid-forbidden-values/
题目类型: 贪心、数组、哈希表、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3785. 避免禁用值的最小交换次数 - 给你两个长度为 n 的整数数组 nums 和 forbidden。你可以执行以下操作任意次（包括零次）： * 选择两个 不同 下标 i 和 j，然后交换 nums[i] 和 nums[j]。 返回使得对于每个下标 i，nums[i] 不等于 forbidden[i] 所需的 最小 交换次数。如果无论如何都无法满足条件，返回 -1。 示例 1： 输入： nums = [1,2,3], forbidden = [3,2,1] 输出： 1 解释： 一种最优的交换方案： * 选择 nums 中下标 i = 0 和 j = 1，交换它们，得到 nums = [2, 1, 3]。 * 交换完成后，对于每个下标 i，nums[i] 都不等于 forbidden[i]。 示例 2： 输入： nums = [4,6,6,5], forbidden = [4,6,5,5] 输出： 2 解释： 一种最优的交换方案： * 选择 nums 中下标 i = 0 和 j = 2，交换它们，得到 nums = [6, 6, 4, 5]。 * 选择 nums 中下标 i = 1 和 j = 3，交换它们，得到 nums = [6, 5, 4, 6]。 * 交换完成后，对于每个下标 i，nums[i] 都不等于 forbidden[i]。 示例 3： 输入： nums = [7,7], forbidden = [8,7] 输出： -1 解释： 无法通过任何交换使得 nums[i] 对于所有下标 i 都不等于 forbidden[i]。 示例 4： 输入： nums = [1,2], forbidden = [2,1] 输出： 0 解释： 无需交换，因为对于每个下标 i，nums[i] 已经不等于 forbidden[i]，因此答案是 0。 提示： * 1 <= n == nums.length == forbidden.length <= 105 * 1 <= nums[i], forbidden[i] <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和哈希表来记录需要交换的位置，并尽可能减少交换次数。

算法步骤:
1. 创建一个哈希表 `need` 来记录每个位置需要交换的目标值。
2. 遍历 `nums` 和 `forbidden`，将需要交换的位置及其目标值存入 `need`。
3. 如果 `need` 为空，说明不需要交换，直接返回 0。
4. 使用一个集合 `seen` 来记录已经处理过的值，避免重复处理。
5. 遍历 `need`，尝试找到可以交换的目标值，并更新 `nums` 和 `need`。
6. 如果所有需要交换的位置都处理完毕，返回交换次数；否则返回 -1。

关键点:
- 使用哈希表记录需要交换的位置及其目标值。
- 尽可能减少交换次数，通过贪心算法找到最优解。
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


def minimum_swaps_to_avoid_forbidden(nums: List[int], forbidden: List[int]) -> int:
    """
    函数式接口 - 实现避免禁用值的最小交换次数
    """
    n = len(nums)
    need = {}
    for i in range(n):
        if nums[i] == forbidden[i]:
            need[i] = forbidden[i]
    
    if not need:
        return 0
    
    seen = set()
    swaps = 0
    
    for i in list(need.keys()):
        if i in seen:
            continue
        target = need[i]
        found = False
        for j in range(i + 1, n):
            if nums[j] == target and j not in need:
                nums[i], nums[j] = nums[j], nums[i]
                swaps += 1
                found = True
                break
            elif nums[j] == target and j in need:
                if need[j] != nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    need[j] = nums[i]
                    swaps += 1
                    found = True
                    break
        
        if not found:
            return -1
        seen.add(i)
    
    return swaps


Solution = create_solution(minimum_swaps_to_avoid_forbidden)