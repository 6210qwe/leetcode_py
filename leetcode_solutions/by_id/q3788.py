# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3788
标题: Maximum Unique Subarray Sum After Deletion
难度: easy
链接: https://leetcode.cn/problems/maximum-unique-subarray-sum-after-deletion/
题目类型: 贪心、数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3487. 删除后的最大子数组元素和 - 给你一个整数数组 nums 。 你可以从数组 nums 中删除任意数量的元素，但不能将其变为 空 数组。执行删除操作后，选出 nums 中满足下述条件的一个子数组： 1. 子数组中的所有元素 互不相同 。 2. 最大化 子数组的元素和。 返回子数组的 最大元素和 。 子数组 是数组的一个连续、非空 的元素序列。 示例 1： 输入：nums = [1,2,3,4,5] 输出：15 解释： 不删除任何元素，选中整个数组得到最大元素和。 示例 2： 输入：nums = [1,1,0,1,1] 输出：1 解释： 删除元素 nums[0] == 1、nums[1] == 1、nums[2] == 0 和 nums[3] == 1 。选中整个数组 [1] 得到最大元素和。 示例 3： 输入：nums = [1,2,-1,-2,1,0,-1] 输出：3 解释： 删除元素 nums[2] == -1 和 nums[3] == -2 ，从 [1, 2, 1, 0, -1] 中选中子数组 [2, 1] 以获得最大元素和。 提示： * 1 <= nums.length <= 100 * -100 <= nums[i] <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口来找到包含唯一元素的最大子数组和。

算法步骤:
1. 初始化两个指针 left 和 right，分别表示滑动窗口的左右边界。
2. 使用一个集合 seen 来记录当前窗口内的元素。
3. 使用变量 current_sum 来记录当前窗口内的元素和。
4. 使用变量 max_sum 来记录最大子数组和。
5. 移动右指针 right，将 nums[right] 加入 seen 并更新 current_sum。
6. 如果 nums[right] 已经在 seen 中，则移动左指针 left，直到 nums[right] 不再在 seen 中。
7. 更新 max_sum。
8. 返回 max_sum。

关键点:
- 使用滑动窗口来维护一个包含唯一元素的子数组。
- 通过移动左指针来确保窗口内的元素都是唯一的。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组 nums 的长度。每个元素最多被访问两次（一次由右指针，一次由左指针）。
空间复杂度: O(n)，最坏情况下 seen 集合中会包含所有的元素。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def maximum_unique_subarray(nums: List[int]) -> int:
    """
    函数式接口 - 找到删除后的最大子数组元素和
    """
    left = 0
    right = 0
    seen = set()
    current_sum = 0
    max_sum = 0
    
    while right < len(nums):
        while nums[right] in seen:
            seen.remove(nums[left])
            current_sum -= nums[left]
            left += 1
        
        seen.add(nums[right])
        current_sum += nums[right]
        max_sum = max(max_sum, current_sum)
        right += 1
    
    return max_sum


Solution = create_solution(maximum_unique_subarray)