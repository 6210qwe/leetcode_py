# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2917
标题: Count Pairs Whose Sum is Less than Target
难度: easy
链接: https://leetcode.cn/problems/count-pairs-whose-sum-is-less-than-target/
题目类型: 数组、双指针、二分查找、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2824. 统计和小于目标的下标对数目 - 给你一个下标从 0 开始长度为 n 的整数数组 nums 和一个整数 target ，请你返回满足 0 <= i < j < n 且 nums[i] + nums[j] < target 的下标对 (i, j) 的数目。 示例 1： 输入：nums = [-1,1,2,3,1], target = 2 输出：3 解释：总共有 3 个下标对满足题目描述： - (0, 1) ，0 < 1 且 nums[0] + nums[1] = 0 < target - (0, 2) ，0 < 2 且 nums[0] + nums[2] = 1 < target - (0, 4) ，0 < 4 且 nums[0] + nums[4] = 0 < target 注意 (0, 3) 不计入答案因为 nums[0] + nums[3] 不是严格小于 target 。 示例 2： 输入：nums = [-6,2,5,-2,-7,-1,3], target = -2 输出：10 解释：总共有 10 个下标对满足题目描述： - (0, 1) ，0 < 1 且 nums[0] + nums[1] = -4 < target - (0, 3) ，0 < 3 且 nums[0] + nums[3] = -8 < target - (0, 4) ，0 < 4 且 nums[0] + nums[4] = -13 < target - (0, 5) ，0 < 5 且 nums[0] + nums[5] = -7 < target - (0, 6) ，0 < 6 且 nums[0] + nums[6] = -3 < target - (1, 4) ，1 < 4 且 nums[1] + nums[4] = -5 < target - (3, 4) ，3 < 4 且 nums[3] + nums[4] = -9 < target - (3, 5) ，3 < 5 且 nums[3] + nums[5] = -3 < target - (4, 5) ，4 < 5 且 nums[4] + nums[5] = -8 < target - (4, 6) ，4 < 6 且 nums[4] + nums[6] = -4 < target 提示： * 1 <= nums.length == n <= 50 * -50 <= nums[i], target <= 50
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针法，先对数组进行排序，然后使用两个指针分别从头和尾开始遍历，找到所有满足条件的下标对。

算法步骤:
1. 对数组进行排序。
2. 初始化两个指针 left 和 right，分别指向数组的起始位置和末尾位置。
3. 遍历数组，如果 nums[left] + nums[right] < target，则说明从 left 到 right-1 的所有下标对都满足条件，将这些下标对的数量加到结果中，并将 left 指针右移一位。
4. 如果 nums[left] + nums[right] >= target，则将 right 指针左移一位。
5. 重复步骤 3 和 4 直到 left 和 right 相遇。

关键点:
- 排序后使用双指针可以有效地减少不必要的比较。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是数组的长度。排序的时间复杂度是 O(n log n)，双指针遍历的时间复杂度是 O(n)。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_pairs(nums: List[int], target: int) -> int:
    """
    函数式接口 - 返回满足 nums[i] + nums[j] < target 的下标对 (i, j) 的数目
    """
    # 对数组进行排序
    nums.sort()
    
    left, right = 0, len(nums) - 1
    count = 0
    
    while left < right:
        if nums[left] + nums[right] < target:
            # 从 left 到 right-1 的所有下标对都满足条件
            count += right - left
            left += 1
        else:
            right -= 1
    
    return count


Solution = create_solution(count_pairs)