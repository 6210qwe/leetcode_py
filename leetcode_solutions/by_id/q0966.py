# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 966
标题: Binary Subarrays With Sum
难度: medium
链接: https://leetcode.cn/problems/binary-subarrays-with-sum/
题目类型: 数组、哈希表、前缀和、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
930. 和相同的二元子数组 - 给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。 子数组 是数组的一段连续部分。 示例 1： 输入：nums = [1,0,1,0,1], goal = 2 输出：4 解释： 有 4 个满足题目要求的子数组：[1,0,1]、[1,0,1,0]、[0,1,0,1]、[1,0,1] 示例 2： 输入：nums = [0,0,0,0,0], goal = 0 输出：15 提示： * 1 <= nums.length <= 3 * 104 * nums[i] 不是 0 就是 1 * 0 <= goal <= nums.length
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和 + 哈希表来记录前缀和出现的次数，从而快速找到和为 goal 的子数组。

算法步骤:
1. 初始化前缀和 `prefix_sum` 为 0，以及一个哈希表 `prefix_count`，其中 `prefix_count[0] = 1`。
2. 遍历数组 `nums`，更新前缀和 `prefix_sum`。
3. 对于每个位置 `i`，计算 `prefix_sum - goal`，如果这个值在 `prefix_count` 中存在，则说明存在和为 `goal` 的子数组，将 `prefix_count[prefix_sum - goal]` 加到结果中。
4. 更新 `prefix_count`，增加当前前缀和 `prefix_sum` 的计数。

关键点:
- 使用前缀和可以快速计算任意子数组的和。
- 使用哈希表记录前缀和出现的次数，可以在 O(1) 时间内找到和为 `goal` 的子数组。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组 `nums` 的长度。我们只需要遍历数组一次。
空间复杂度: O(n)，哈希表 `prefix_count` 在最坏情况下需要存储 n 个不同的前缀和。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(nums: List[int], goal: int) -> int:
    """
    函数式接口 - 返回和为 goal 的非空子数组的数量
    """
    prefix_sum = 0
    prefix_count = {0: 1}
    result = 0
    
    for num in nums:
        prefix_sum += num
        if prefix_sum - goal in prefix_count:
            result += prefix_count[prefix_sum - goal]
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
    
    return result


Solution = create_solution(solution_function_name)