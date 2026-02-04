# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2527
标题: Count Subarrays With Fixed Bounds
难度: hard
链接: https://leetcode.cn/problems/count-subarrays-with-fixed-bounds/
题目类型: 队列、数组、滑动窗口、单调队列
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2444. 统计定界子数组的数目 - 给你一个整数数组 nums 和两个整数 minK 以及 maxK 。 nums 的定界子数组是满足下述条件的一个子数组： * 子数组中的 最小值 等于 minK 。 * 子数组中的 最大值 等于 maxK 。 返回定界子数组的数目。 子数组是数组中的一个连续部分。 示例 1： 输入：nums = [1,3,5,2,7,5], minK = 1, maxK = 5 输出：2 解释：定界子数组是 [1,3,5] 和 [1,3,5,2] 。 示例 2： 输入：nums = [1,1,1,1], minK = 1, maxK = 1 输出：10 解释：nums 的每个子数组都是一个定界子数组。共有 10 个子数组。 提示： * 2 <= nums.length <= 105 * 1 <= nums[i], minK, maxK <= 106
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口来维护当前子数组，并记录最近一次出现的 minK 和 maxK 的位置。

算法步骤:
1. 初始化变量：left 为左边界，right 为右边界，min_pos 为 minK 最近出现的位置，max_pos 为 maxK 最近出现的位置。
2. 遍历数组：
   - 如果当前元素不在 [minK, maxK] 范围内，更新左边界 left 到 right + 1。
   - 更新 min_pos 和 max_pos。
   - 计算当前子数组中定界子数组的数量。
3. 返回结果。

关键点:
- 使用滑动窗口来维护当前子数组。
- 记录最近一次出现的 minK 和 maxK 的位置，以便快速计算定界子数组的数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组的长度。每个元素最多被处理两次（一次作为右边界，一次作为左边界）。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_subarrays_with_fixed_bounds(nums: List[int], minK: int, maxK: int) -> int:
    """
    函数式接口 - 统计定界子数组的数目
    """
    left = 0
    right = 0
    min_pos = -1
    max_pos = -1
    count = 0
    
    while right < len(nums):
        if nums[right] < minK or nums[right] > maxK:
            left = right + 1
            min_pos = -1
            max_pos = -1
        else:
            if nums[right] == minK:
                min_pos = right
            if nums[right] == maxK:
                max_pos = right
            if min_pos != -1 and max_pos != -1:
                count += min(min_pos, max_pos) - left + 1
        
        right += 1
    
    return count


Solution = create_solution(count_subarrays_with_fixed_bounds)