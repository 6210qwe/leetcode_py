# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 485
标题: Max Consecutive Ones
难度: easy
链接: https://leetcode.cn/problems/max-consecutive-ones/
题目类型: 数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
485. 最大连续 1 的个数 - 给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。 示例 1： 输入：nums = [1,1,0,1,1,1] 输出：3 解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3. 示例 2: 输入：nums = [1,0,1,1,0,1] 输出：2 提示： * 1 <= nums.length <= 105 * nums[i] 不是 0 就是 1.
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过一次遍历数组，记录当前连续 1 的个数，并更新最大连续 1 的个数。

算法步骤:
1. 初始化两个变量 `current_count` 和 `max_count`，分别用于记录当前连续 1 的个数和最大连续 1 的个数。
2. 遍历数组 `nums`：
   - 如果当前元素为 1，则增加 `current_count`。
   - 如果当前元素为 0，则重置 `current_count` 为 0。
   - 每次更新 `max_count` 为 `max(max_count, current_count)`。
3. 返回 `max_count`。

关键点:
- 注意边界条件，确保在遍历结束时更新 `max_count`。
- 优化时间和空间复杂度，时间复杂度为 O(n)，空间复杂度为 O(1)。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要遍历整个数组一次
空间复杂度: O(1) - 只使用了常数级的额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_consecutive_ones(nums: List[int]) -> int:
    """
    函数式接口 - 计算二进制数组中最大连续 1 的个数
    
    实现思路:
    通过一次遍历数组，记录当前连续 1 的个数，并更新最大连续 1 的个数。
    
    Args:
        nums (List[int]): 二进制数组
        
    Returns:
        int: 最大连续 1 的个数
        
    Example:
        >>> max_consecutive_ones([1,1,0,1,1,1])
        3
    """
    current_count = 0
    max_count = 0
    
    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    
    return max_count


# 自动生成Solution类（无需手动编写）
Solution = create_solution(max_consecutive_ones)