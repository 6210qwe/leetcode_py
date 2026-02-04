# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3885
标题: Count Special Triplets
难度: medium
链接: https://leetcode.cn/problems/count-special-triplets/
题目类型: 数组、哈希表、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3583. 统计特殊三元组 - 给你一个整数数组 nums。 特殊三元组 定义为满足以下条件的下标三元组 (i, j, k)： * 0 <= i < j < k < n，其中 n = nums.length * nums[i] == nums[j] * 2 * nums[k] == nums[j] * 2 返回数组中 特殊三元组 的总数。 由于答案可能非常大，请返回结果对 109 + 7 取余数后的值。 示例 1： 输入： nums = [6,3,6] 输出： 1 解释： 唯一的特殊三元组是 (i, j, k) = (0, 1, 2)，其中： * nums[0] = 6, nums[1] = 3, nums[2] = 6 * nums[0] = nums[1] * 2 = 3 * 2 = 6 * nums[2] = nums[1] * 2 = 3 * 2 = 6 示例 2： 输入： nums = [0,1,0,0] 输出： 1 解释： 唯一的特殊三元组是 (i, j, k) = (0, 2, 3)，其中： * nums[0] = 0, nums[2] = 0, nums[3] = 0 * nums[0] = nums[2] * 2 = 0 * 2 = 0 * nums[3] = nums[2] * 2 = 0 * 2 = 0 示例 3： 输入： nums = [8,4,2,8,4] 输出： 2 解释： 共有两个特殊三元组： * (i, j, k) = (0, 1, 3) * nums[0] = 8, nums[1] = 4, nums[3] = 8 * nums[0] = nums[1] * 2 = 4 * 2 = 8 * nums[3] = nums[1] * 2 = 4 * 2 = 8 * (i, j, k) = (1, 2, 4) * nums[1] = 4, nums[2] = 2, nums[4] = 4 * nums[1] = nums[2] * 2 = 2 * 2 = 4 * nums[4] = nums[2] * 2 = 2 * 2 = 4 提示： * 3 <= n == nums.length <= 105 * 0 <= nums[i] <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表记录每个元素的出现次数，并通过两次遍历数组来计算特殊三元组的数量。

算法步骤:
1. 初始化两个哈希表 `count` 和 `right_count`，分别用于记录每个元素的总出现次数和右边元素的出现次数。
2. 从右向左遍历数组，填充 `right_count`。
3. 从左向右遍历数组，对于每个元素 `nums[j]`，计算其一半 `half` 和两倍 `double`。
4. 如果 `half` 和 `double` 都在 `count` 中存在，则将 `count[half] * right_count[double]` 加到结果中。
5. 更新 `count` 和 `right_count`。

关键点:
- 使用哈希表来高效地记录和查找元素的出现次数。
- 通过两次遍历数组来避免嵌套循环，从而降低时间复杂度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_special_triplets(nums: List[int]) -> int:
    MOD = 10**9 + 7
    n = len(nums)
    count = {}
    right_count = {}
    
    # 从右向左遍历数组，填充 right_count
    for num in reversed(nums):
        if num in right_count:
            right_count[num] += 1
        else:
            right_count[num] = 1
    
    result = 0
    # 从左向右遍历数组
    for i in range(n):
        half = nums[i] // 2
        double = nums[i] * 2
        
        if half in count and double in right_count:
            result = (result + count[half] * right_count[double]) % MOD
        
        # 更新 count 和 right_count
        if nums[i] in count:
            count[nums[i]] += 1
        else:
            count[nums[i]] = 1
        
        right_count[nums[i]] -= 1
        if right_count[nums[i]] == 0:
            del right_count[nums[i]]
    
    return result


Solution = create_solution(count_special_triplets)