# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3535
标题: Find the Count of Monotonic Pairs I
难度: hard
链接: https://leetcode.cn/problems/find-the-count-of-monotonic-pairs-i/
题目类型: 数组、数学、动态规划、组合数学、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3250. 单调数组对的数目 I - 给你一个长度为 n 的 正 整数数组 nums 。 如果两个 非负 整数数组 (arr1, arr2) 满足以下条件，我们称它们是 单调 数组对： * 两个数组的长度都是 n 。 * arr1 是单调 非递减 的，换句话说 arr1[0] <= arr1[1] <= ... <= arr1[n - 1] 。 * arr2 是单调 非递增 的，换句话说 arr2[0] >= arr2[1] >= ... >= arr2[n - 1] 。 * 对于所有的 0 <= i <= n - 1 都有 arr1[i] + arr2[i] == nums[i] 。 请你返回所有 单调 数组对的数目。 由于答案可能很大，请你将它对 109 + 7 取余 后返回。 示例 1： 输入：nums = [2,3,2] 输出：4 解释： 单调数组对包括： 1. ([0, 1, 1], [2, 2, 1]) 2. ([0, 1, 2], [2, 2, 0]) 3. ([0, 2, 2], [2, 1, 0]) 4. ([1, 2, 2], [1, 1, 0]) 示例 2： 输入：nums = [5,5,5,5] 输出：126 提示： * 1 <= n == nums.length <= 2000 * 1 <= nums[i] <= 50
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来计算单调数组对的数量。我们需要维护两个数组 `dp_min` 和 `dp_max`，分别表示以当前元素结尾的非递减和非递增子数组的数量。

算法步骤:
1. 初始化 `dp_min` 和 `dp_max` 数组，长度为 51（因为 nums[i] 的范围是 1 到 50）。
2. 遍历数组 `nums`，对于每个元素 `num`，更新 `dp_min` 和 `dp_max`。
3. 计算最终结果时，使用前缀和来快速计算满足条件的数组对数量。

关键点:
- 使用动态规划来维护单调性。
- 使用前缀和来快速计算满足条件的数组对数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是 nums 的长度，m 是 nums 中元素的最大值（这里是 50）。
空间复杂度: O(m)，用于存储 dp_min 和 dp_max 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

MOD = 10**9 + 7

def solution_function_name(nums: List[int]) -> int:
    """
    函数式接口 - 返回所有单调数组对的数目
    """
    n = len(nums)
    dp_min = [0] * 51
    dp_max = [0] * 51
    dp_min[nums[0]] = 1
    dp_max[nums[0]] = 1
    
    for i in range(1, n):
        new_dp_min = [0] * 51
        new_dp_max = [0] * 51
        for j in range(1, 51):
            new_dp_min[j] = (new_dp_min[j-1] + dp_min[j]) % MOD
            if j <= nums[i]:
                new_dp_min[nums[i]] = (new_dp_min[nums[i]] + new_dp_min[j-1]) % MOD
            else:
                new_dp_min[nums[i]] = (new_dp_min[nums[i]] + new_dp_min[j-1] - dp_min[j-1] + MOD) % MOD
        
        for j in range(50, 0, -1):
            new_dp_max[j] = (new_dp_max[j+1] + dp_max[j]) % MOD
            if j >= nums[i]:
                new_dp_max[nums[i]] = (new_dp_max[nums[i]] + new_dp_max[j+1]) % MOD
            else:
                new_dp_max[nums[i]] = (new_dp_max[nums[i]] + new_dp_max[j+1] - dp_max[j+1] + MOD) % MOD
        
        dp_min, dp_max = new_dp_min, new_dp_max
    
    return sum(dp_min) % MOD

Solution = create_solution(solution_function_name)