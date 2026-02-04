# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 4115
标题: Minimum Distance Between Three Equal Elements I
难度: easy
链接: https://leetcode.cn/problems/minimum-distance-between-three-equal-elements-i/
题目类型: 数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3740. 三个相等元素之间的最小距离 I - 给你一个整数数组 nums。 如果满足 nums[i] == nums[j] == nums[k]，且 (i, j, k) 是 3 个 不同 下标，那么三元组 (i, j, k) 被称为 有效三元组 。 有效三元组 的 距离 被定义为 abs(i - j) + abs(j - k) + abs(k - i)，其中 abs(x) 表示 x 的 绝对值 。 返回一个整数，表示 有效三元组 的 最小 可能距离。如果不存在 有效三元组 ，返回 -1。 示例 1： 输入： nums = [1,2,1,1,3] 输出： 6 解释： 最小距离对应的有效三元组是 (0, 2, 3) 。 (0, 2, 3) 是一个有效三元组，因为 nums[0] == nums[2] == nums[3] == 1。它的距离为 abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6。 示例 2： 输入： nums = [1,1,2,3,2,1,2] 输出： 8 解释： 最小距离对应的有效三元组是 (2, 4, 6) 。 (2, 4, 6) 是一个有效三元组，因为 nums[2] == nums[4] == nums[6] == 2。它的距离为 abs(2 - 4) + abs(4 - 6) + abs(6 - 2) = 2 + 2 + 4 = 8。 示例 3： 输入： nums = [1] 输出： -1 解释： 不存在有效三元组，因此答案为 -1。 提示： * 1 <= n == nums.length <= 100 * 1 <= nums[i] <= n
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表记录每个元素的索引列表，然后遍历这些索引列表，找到最小的距离。

算法步骤:
1. 初始化一个字典 `index_map`，键为数组中的元素，值为该元素出现的所有索引。
2. 遍历 `index_map`，对于每个元素的索引列表，如果长度小于3，则跳过。
3. 对于长度大于等于3的索引列表，计算所有可能的三元组距离，并记录最小值。
4. 返回最小距离，如果没有找到有效三元组，则返回 -1。

关键点:
- 使用哈希表存储每个元素的索引，方便快速查找。
- 通过遍历索引列表，计算所有可能的三元组距离。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def minimum_distance(nums: List[int]) -> int:
    """
    函数式接口 - 计算三个相等元素之间的最小距离
    """
    index_map = {}
    
    # 构建索引映射
    for i, num in enumerate(nums):
        if num not in index_map:
            index_map[num] = []
        index_map[num].append(i)
    
    min_distance = float('inf')
    
    # 遍历索引映射，计算最小距离
    for indices in index_map.values():
        if len(indices) < 3:
            continue
        for i in range(len(indices) - 2):
            for j in range(i + 1, len(indices) - 1):
                for k in range(j + 1, len(indices)):
                    distance = abs(indices[i] - indices[j]) + abs(indices[j] - indices[k]) + abs(indices[k] - indices[i])
                    min_distance = min(min_distance, distance)
    
    return min_distance if min_distance != float('inf') else -1


Solution = create_solution(minimum_distance)