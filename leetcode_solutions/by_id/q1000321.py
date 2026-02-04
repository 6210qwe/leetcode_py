# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000321
标题: 存在重复元素 III
难度: medium
链接: https://leetcode.cn/problems/7WqeDu/
题目类型: 数组、桶排序、有序集合、排序、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 057. 存在重复元素 III - 给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。 如果存在则返回 true，不存在返回 false。 示例 1： 输入：nums = [1,2,3,1], k = 3, t = 0 输出：true 示例 2： 输入：nums = [1,0,1,1], k = 1, t = 2 输出：true 示例 3： 输入：nums = [1,5,9,1,5,9], k = 2, t = 3 输出：false 提示： * 0 <= nums.length <= 2 * 104 * -231 <= nums[i] <= 231 - 1 * 0 <= k <= 104 * 0 <= t <= 231 - 1 注意：本题与主站 220 题相同： https://leetcode.cn/problems/contains-duplicate-iii/ [https://leetcode.cn/problems/contains-duplicate-iii/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用桶排序的思想来解决这个问题。我们将每个元素放入一个桶中，桶的大小为 t + 1。这样，如果两个元素在同一个桶中，或者相邻的桶中，那么它们的差值一定小于等于 t。

算法步骤:
1. 初始化一个字典来存储桶。
2. 遍历数组中的每个元素，计算其应该放入的桶的编号。
3. 检查当前桶及其相邻桶中是否有元素，如果有，则返回 True。
4. 将当前元素放入对应的桶中。
5. 如果当前索引超过 k，则从桶中移除过期的元素。

关键点:
- 桶的大小为 t + 1，确保桶内的元素差值不超过 t。
- 只保留最近 k 个元素的桶，以确保索引差值不超过 k。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(min(n, k))
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def contains_nearby_almost_duplicate(nums: List[int], k: int, t: int) -> bool:
    """
    函数式接口 - 判断是否存在两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= t 且 abs(i - j) <= k
    """
    if t < 0:
        return False
    
    bucket = {}
    bucket_size = t + 1
    
    for i, num in enumerate(nums):
        bucket_key = num // bucket_size
        
        if bucket_key in bucket:
            return True
        if (bucket_key - 1) in bucket and abs(num - bucket[bucket_key - 1]) <= t:
            return True
        if (bucket_key + 1) in bucket and abs(num - bucket[bucket_key + 1]) <= t:
            return True
        
        bucket[bucket_key] = num
        
        if i >= k:
            del bucket[nums[i - k] // bucket_size]
    
    return False


Solution = create_solution(contains_nearby_almost_duplicate)