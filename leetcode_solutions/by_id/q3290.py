# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3290
标题: Number of Subarrays That Match a Pattern II
难度: hard
链接: https://leetcode.cn/problems/number-of-subarrays-that-match-a-pattern-ii/
题目类型: 数组、字符串匹配、哈希函数、滚动哈希
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3036. 匹配模式数组的子数组数目 II - 给你一个下标从 0 开始长度为 n 的整数数组 nums ，和一个下标从 0 开始长度为 m 的整数数组 pattern ，pattern 数组只包含整数 -1 ，0 和 1 。 大小为 m + 1 的子数组 nums[i..j] 如果对于每个元素 pattern[k] 都满足以下条件，那么我们说这个子数组匹配模式数组 pattern ： * 如果 pattern[k] == 1 ，那么 nums[i + k + 1] > nums[i + k] * 如果 pattern[k] == 0 ，那么 nums[i + k + 1] == nums[i + k] * 如果 pattern[k] == -1 ，那么 nums[i + k + 1] < nums[i + k] 请你返回匹配 pattern 的 nums 子数组的 数目 。 示例 1： 输入：nums = [1,2,3,4,5,6], pattern = [1,1] 输出：4 解释：模式 [1,1] 说明我们要找的子数组是长度为 3 且严格上升的。在数组 nums 中，子数组 [1,2,3] ，[2,3,4] ，[3,4,5] 和 [4,5,6] 都匹配这个模式。 所以 nums 中总共有 4 个子数组匹配这个模式。 示例 2： 输入：nums = [1,4,4,1,3,5,5,3], pattern = [1,0,-1] 输出：2 解释：这里，模式数组 [1,0,-1] 说明我们需要找的子数组中，第一个元素小于第二个元素，第二个元素等于第三个元素，第三个元素大于第四个元素。在 nums 中，子数组 [1,4,4,1] 和 [3,5,5,3] 都匹配这个模式。 所以 nums 中总共有 2 个子数组匹配这个模式。 提示： * 2 <= n == nums.length <= 106 * 1 <= nums[i] <= 109 * 1 <= m == pattern.length < n * -1 <= pattern[i] <= 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滚动哈希来快速匹配子数组。

算法步骤:
1. 将 nums 转换为一个新的数组 diff，其中 diff[i] 表示 nums[i+1] 与 nums[i] 的关系（1, 0, -1）。
2. 使用滚动哈希将 pattern 转换为一个哈希值。
3. 在 diff 数组上滑动窗口，计算每个窗口的哈希值，并与 pattern 的哈希值进行比较。
4. 如果哈希值匹配，则进一步验证子数组是否完全匹配 pattern。

关键点:
- 使用滚动哈希可以高效地进行子数组匹配。
- 滚动哈希需要处理哈希冲突的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def get_diff(nums: List[int]) -> List[int]:
    """将 nums 转换为 diff 数组"""
    return [1 if nums[i + 1] > nums[i] else (0 if nums[i + 1] == nums[i] else -1) for i in range(len(nums) - 1)]

def hash_pattern(pattern: List[int], base: int, mod: int) -> int:
    """计算 pattern 的哈希值"""
    hash_val = 0
    for num in pattern:
        hash_val = (hash_val * base + (num + 1)) % mod
    return hash_val

def match_pattern(diff: List[int], pattern: List[int], base: int, mod: int) -> int:
    """在 diff 数组上滑动窗口，匹配 pattern"""
    n, m = len(diff), len(pattern)
    pattern_hash = hash_pattern(pattern, base, mod)
    window_hash = hash_pattern(diff[:m], base, mod)
    
    count = 0
    if window_hash == pattern_hash and diff[:m] == pattern:
        count += 1
    
    power = pow(base, m, mod)
    
    for i in range(m, n):
        window_hash = (window_hash * base - (diff[i - m] + 1) * power + (diff[i] + 1)) % mod
        if window_hash == pattern_hash and diff[i - m + 1:i + 1] == pattern:
            count += 1
    
    return count

def solution_function_name(nums: List[int], pattern: List[int]) -> int:
    """
    函数式接口 - 计算匹配 pattern 的子数组数目
    """
    diff = get_diff(nums)
    base, mod = 101, 10**9 + 7
    return match_pattern(diff, pattern, base, mod)

Solution = create_solution(solution_function_name)