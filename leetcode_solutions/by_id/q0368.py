# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 368
标题: Largest Divisible Subset
难度: medium
链接: https://leetcode.cn/problems/largest-divisible-subset/
题目类型: 数组、数学、动态规划、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
368. 最大整除子集 - 给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[j]) 都应当满足： * answer[i] % answer[j] == 0 ，或 * answer[j] % answer[i] == 0 如果存在多个有效解子集，返回其中任何一个均可。 示例 1： 输入：nums = [1,2,3] 输出：[1,2] 解释：[1,3] 也会被视为正确答案。 示例 2： 输入：nums = [1,2,4,8] 输出：[1,2,4,8] 提示： * 1 <= nums.length <= 1000 * 1 <= nums[i] <= 2 * 109 * nums 中的所有整数 互不相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 动态规划+排序

算法步骤:
1. 先对数组排序
2. dp[i]表示以nums[i]结尾的最大整除子集长度
3. parent[i]记录前驱节点，用于回溯
4. 对于每个i，遍历j<i，如果nums[i]%nums[j]==0，更新dp[i]
5. 找到最大长度，回溯构造结果

关键点:
- 需要排序保证整除关系的传递性
- 使用parent数组回溯构造结果
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2) - n为数组长度
空间复杂度: O(n) - dp和parent数组
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def largest_divisible_subset(nums: List[int]) -> List[int]:
    """
    函数式接口 - 最大整除子集
    
    实现思路:
    使用动态规划，先排序，然后找到最长整除子序列。
    
    Args:
        nums: 无重复正整数数组
        
    Returns:
        最大整除子集
        
    Example:
        >>> largest_divisible_subset([1,2,3])
        [1, 2]
    """
    if not nums:
        return []
    
    nums.sort()
    n = len(nums)
    dp = [1] * n
    parent = [-1] * n
    
    max_len = 1
    max_idx = 0
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
        
        if dp[i] > max_len:
            max_len = dp[i]
            max_idx = i
    
    # 回溯构造结果
    result = []
    idx = max_idx
    while idx != -1:
        result.append(nums[idx])
        idx = parent[idx]
    
    return result[::-1]


# 自动生成Solution类（无需手动编写）
Solution = create_solution(largest_divisible_subset)
