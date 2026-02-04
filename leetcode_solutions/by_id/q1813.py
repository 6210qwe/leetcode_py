# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1813
标题: Maximum Erasure Value
难度: medium
链接: https://leetcode.cn/problems/maximum-erasure-value/
题目类型: 数组、哈希表、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1695. 删除子数组的最大得分 - 给你一个正整数数组 nums ，请你从中删除一个含有 若干不同元素 的子数组。删除子数组的 得分 就是子数组各元素之 和 。 返回 只删除一个 子数组可获得的 最大得分 。 如果数组 b 是数组 a 的一个连续子序列，即如果它等于 a[l],a[l+1],...,a[r] ，那么它就是 a 的一个子数组。 示例 1： 输入：nums = [4,2,4,5,6] 输出：17 解释：最优子数组是 [2,4,5,6] 示例 2： 输入：nums = [5,2,1,2,5,2,1,2,5] 输出：8 解释：最优子数组是 [5,2,1] 或 [1,2,5] 提示： * 1 <= nums.length <= 105 * 1 <= nums[i] <= 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口和哈希表来找到具有最大和的不同元素子数组。

算法步骤:
1. 初始化两个指针 left 和 right 分别表示滑动窗口的左右边界。
2. 使用一个哈希表 seen 来记录当前窗口内的元素及其出现次数。
3. 初始化变量 max_sum 为 0，用于记录最大子数组和；current_sum 为 0，用于记录当前窗口内元素的和。
4. 移动右指针 right，扩展窗口：
   - 将 nums[right] 加入 current_sum，并更新 seen。
   - 如果 nums[right] 在 seen 中已经存在，则移动左指针 left，收缩窗口，直到 nums[right] 不再重复。
   - 更新 max_sum 为 current_sum 和 max_sum 的较大值。
5. 返回 max_sum。

关键点:
- 使用滑动窗口和哈希表来确保窗口内的元素都是不同的。
- 通过调整窗口大小来找到具有最大和的不同元素子数组。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组 nums 的长度。每个元素最多被处理两次（一次加入窗口，一次移出窗口）。
空间复杂度: O(n)，哈希表 seen 最多存储 n 个不同的元素。
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
    函数式接口 - 实现最优解法
    """
    left, right = 0, 0
    seen = {}
    max_sum = 0
    current_sum = 0
    
    while right < len(nums):
        if nums[right] in seen:
            while nums[left] != nums[right]:
                current_sum -= nums[left]
                del seen[nums[left]]
                left += 1
            left += 1
        else:
            current_sum += nums[right]
            seen[nums[right]] = True
            max_sum = max(max_sum, current_sum)
        
        right += 1
    
    return max_sum


Solution = create_solution(solution_function_name)