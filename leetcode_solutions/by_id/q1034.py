# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1034
标题: Subarrays with K Different Integers
难度: hard
链接: https://leetcode.cn/problems/subarrays-with-k-different-integers/
题目类型: 数组、哈希表、计数、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
992. K 个不同整数的子数组 - 给定一个正整数数组 nums和一个整数 k，返回 nums 中 「好子数组」 的数目。 如果 nums 的某个子数组中不同整数的个数恰好为 k，则称 nums 的这个连续、不一定不同的子数组为 「好子数组 」。 * 例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。 子数组 是数组的 连续 部分。 示例 1： 输入：nums = [1,2,1,2,3], k = 2 输出：7 解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]. 示例 2： 输入：nums = [1,2,1,3,4], k = 3 输出：3 解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4]. 提示： * 1 <= nums.length <= 2 * 104 * 1 <= nums[i], k <= nums.length
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口技术来解决这个问题。我们需要找到恰好有 k 个不同整数的子数组数量。可以通过计算最多有 k 个不同整数的子数组数量减去最多有 k-1 个不同整数的子数组数量来得到结果。

算法步骤:
1. 定义一个辅助函数 `at_most_k_distinct` 来计算最多有 k 个不同整数的子数组数量。
2. 使用两个指针 left 和 right 来表示当前窗口的左右边界。
3. 使用一个哈希表来记录当前窗口内每个整数的出现次数。
4. 当窗口内的不同整数数量超过 k 时，移动左指针并更新哈希表。
5. 计算最多有 k 个不同整数的子数组数量。
6. 返回 `at_most_k_distinct(nums, k) - at_most_k_distinct(nums, k-1)`。

关键点:
- 使用滑动窗口技术来维护当前窗口内的不同整数数量。
- 通过两次调用 `at_most_k_distinct` 函数来计算结果。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组的长度。每个元素最多被处理两次（一次作为右指针，一次作为左指针）。
空间复杂度: O(k)，哈希表的大小最多为 k。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def at_most_k_distinct(nums: List[int], k: int) -> int:
    count = {}
    left = 0
    result = 0
    
    for right in range(len(nums)):
        if nums[right] not in count:
            count[nums[right]] = 0
        count[nums[right]] += 1
        
        while len(count) > k:
            count[nums[left]] -= 1
            if count[nums[left]] == 0:
                del count[nums[left]]
            left += 1
        
        result += right - left + 1
    
    return result


def solution_function_name(nums: List[int], k: int) -> int:
    """
    函数式接口 - 计算恰好有 k 个不同整数的子数组数量
    """
    return at_most_k_distinct(nums, k) - at_most_k_distinct(nums, k-1)


Solution = create_solution(solution_function_name)