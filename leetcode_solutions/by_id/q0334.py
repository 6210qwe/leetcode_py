# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 334
标题: Increasing Triplet Subsequence
难度: medium
链接: https://leetcode.cn/problems/increasing-triplet-subsequence/
题目类型: 贪心、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
334. 递增的三元子序列 - 给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。 如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，返回 true ；否则，返回 false 。 示例 1： 输入：nums = [1,2,3,4,5] 输出：true 解释：任何 i < j < k 的三元组都满足题意 示例 2： 输入：nums = [5,4,3,2,1] 输出：false 解释：不存在满足题意的三元组 示例 3： 输入：nums = [2,1,5,0,4,6] 输出：true 解释：其中一个满足题意的三元组是 (1, 4, 5)，因为 nums[1] == 1 < nums[4] == 4 < nums[5] == 6 提示： * 1 <= nums.length <= 5 * 105 * -231 <= nums[i] <= 231 - 1 进阶：你能实现时间复杂度为 O(n) ，空间复杂度为 O(1) 的解决方案吗？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 贪心，维护两个最小值

算法步骤:
1. 维护first和second两个最小值
2. 如果当前值>second，找到三元组
3. 否则更新first或second

关键点:
- 贪心策略
- 时间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 遍历数组一次
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def increasing_triplet(nums: List[int]) -> bool:
    """
    函数式接口 - 递增的三元子序列
    
    实现思路:
    贪心：维护两个最小值。
    
    Args:
        nums: 整数数组
        
    Returns:
        是否存在递增三元子序列
        
    Example:
        >>> increasing_triplet([1,2,3,4,5])
        True
    """
    first = second = float('inf')
    
    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    
    return False


# 自动生成Solution类（无需手动编写）
Solution = create_solution(increasing_triplet)
