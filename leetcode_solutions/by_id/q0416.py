# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 416
标题: Partition Equal Subset Sum
难度: medium
链接: https://leetcode.cn/problems/partition-equal-subset-sum/
题目类型: 数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
416. 分割等和子集 - 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。 示例 1： 输入：nums = [1,5,11,5] 输出：true 解释：数组可以分割成 [1, 5, 5] 和 [11] 。 示例 2： 输入：nums = [1,2,3,5] 输出：false 解释：数组不能分割成两个元素和相等的子集。 提示： * 1 <= nums.length <= 200 * 1 <= nums[i] <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 0-1 背包问题变形 —— 判断能否选出若干元素使其和恰好等于总和的一半

算法步骤:
1. 计算数组总和 total；若 total 为奇数，则不可能均分，直接返回 False
2. 目标 target = total // 2，问题转化为：是否存在子集，其元素和等于 target
3. 使用动态规划：dp[j] 表示是否能凑出和为 j 的子集（布尔数组）
   - 初始化 dp[0] = True（和为 0 总是可以实现，选空集）
   - 对每个 num，从后往前更新 dp[j] = dp[j] or dp[j - num]（避免重复使用同一元素）
4. 返回 dp[target]

关键点:
- 注意边界条件：total 为奇数时直接返回 False；target=0 时返回 True（但 nums 非空且全正，target=0 仅当 nums 为空，题目保证非空，故无需特判）
- 空间优化：使用一维滚动数组，逆序遍历避免覆盖未更新状态
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * target) - 其中 n 为数组长度，target = sum(nums)//2；最坏情况下 target ≈ 100*200/2 = 10000，可接受
空间复杂度: O(target) - 仅需一维布尔数组存储状态
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def partition_equal_subset_sum(nums: List[int]) -> bool:
    """
    函数式接口 - 判断数组能否分割成两个等和子集
    
    实现思路:
    将问题转化为 0-1 背包可行性问题：是否存在子集和等于总和的一半。
    使用一维动态规划数组 dp，dp[j] 表示能否凑出和为 j 的子集。
    
    Args:
        nums: 只包含正整数的非空数组
        
    Returns:
        bool: 若可分割为两个等和子集返回 True，否则返回 False
        
    Example:
        >>> partition_equal_subset_sum([1,5,11,5])
        True
        >>> partition_equal_subset_sum([1,2,3,5])
        False
    """
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2

    # dp[j] 表示能否凑出和为 j 的子集
    dp = [False] * (target + 1)
    dp[0] = True  # 和为 0 总是可以实现（空集）

    for num in nums:
        # 从大到小遍历，避免重复使用当前 num
        for j in range(target, num - 1, -1):
            if dp[j - num]:
                dp[j] = True

    return dp[target]


# 自动生成Solution类（无需手动编写）
Solution = create_solution(partition_equal_subset_sum)