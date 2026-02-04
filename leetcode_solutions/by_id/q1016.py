# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1016
标题: Subarray Sums Divisible by K
难度: medium
链接: https://leetcode.cn/problems/subarray-sums-divisible-by-k/
题目类型: 数组、哈希表、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
974. 和可被 K 整除的子数组 - 给定一个整数数组 nums 和一个整数 k ，返回其中元素之和可被 k 整除的非空 子数组 的数目。 子数组 是数组中 连续 的部分。 示例 1： 输入：nums = [4,5,0,-2,-3,1], k = 5 输出：7 解释： 有 7 个子数组满足其元素之和可被 k = 5 整除： [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3] 示例 2: 输入: nums = [5], k = 9 输出: 0 提示: * 1 <= nums.length <= 3 * 104 * -104 <= nums[i] <= 104 * 2 <= k <= 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和与哈希表来记录前缀和的余数出现的次数，从而快速找到满足条件的子数组。

算法步骤:
1. 初始化一个哈希表 `prefix_sum_count` 来记录前缀和的余数出现的次数，并将 `prefix_sum_count[0]` 设为 1。
2. 遍历数组 `nums`，计算当前前缀和 `current_sum`，并计算 `current_sum % k` 的余数 `mod`。
3. 如果 `mod` 已经在 `prefix_sum_count` 中，则说明存在一个或多个子数组的和可以被 `k` 整除，将 `prefix_sum_count[mod]` 加到结果中。
4. 更新 `prefix_sum_count[mod]` 的计数。
5. 返回结果。

关键点:
- 使用哈希表记录前缀和的余数出现的次数，避免重复计算。
- 通过前缀和的余数来判断子数组的和是否能被 `k` 整除。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组 `nums` 的长度。我们只需要遍历数组一次。
空间复杂度: O(k)，哈希表 `prefix_sum_count` 最多存储 k 个不同的余数。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def subarraysDivByK(nums: List[int], k: int) -> int:
    """
    函数式接口 - 计算和可被 K 整除的子数组数量
    """
    prefix_sum_count = {0: 1}
    current_sum = 0
    count = 0
    
    for num in nums:
        current_sum += num
        mod = current_sum % k
        if mod < 0:
            mod += k
        
        if mod in prefix_sum_count:
            count += prefix_sum_count[mod]
        
        if mod in prefix_sum_count:
            prefix_sum_count[mod] += 1
        else:
            prefix_sum_count[mod] = 1
    
    return count


Solution = create_solution(subarraysDivByK)