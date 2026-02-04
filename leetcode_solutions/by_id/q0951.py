# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 951
标题: Partition Array into Disjoint Intervals
难度: medium
链接: https://leetcode.cn/problems/partition-array-into-disjoint-intervals/
题目类型: 数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
915. 分割数组 - 给定一个数组 nums ，将其划分为两个连续子数组 left 和 right， 使得： * left 中的每个元素都小于或等于 right 中的每个元素。 * left 和 right 都是非空的。 * left 的长度要尽可能小。 在完成这样的分组后返回 left 的 长度 。 用例可以保证存在这样的划分方法。 示例 1： 输入：nums = [5,0,3,8,6] 输出：3 解释：left = [5,0,3]，right = [8,6] 示例 2： 输入：nums = [1,1,1,0,6,12] 输出：4 解释：left = [1,1,1,0]，right = [6,12] 提示： * 2 <= nums.length <= 105 * 0 <= nums[i] <= 106 * 可以保证至少有一种方法能够按题目所描述的那样对 nums 进行划分。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个辅助数组分别记录从左到右的最大值和从右到左的最小值，然后找到第一个满足条件的分割点。

算法步骤:
1. 初始化两个辅助数组 `max_left` 和 `min_right`，分别记录从左到右的最大值和从右到左的最小值。
2. 遍历数组，填充 `max_left` 和 `min_right`。
3. 遍历数组，找到第一个满足 `max_left[i] <= min_right[i + 1]` 的索引 i，即为分割点。

关键点:
- 使用两个辅助数组来记录前缀最大值和后缀最小值，从而在 O(n) 时间内找到分割点。
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


def partition_disjoint(nums: List[int]) -> int:
    """
    函数式接口 - 将数组划分为两个连续子数组 left 和 right，使得 left 中的每个元素都小于或等于 right 中的每个元素，并返回 left 的长度。
    """
    n = len(nums)
    max_left = [0] * n
    min_right = [0] * n
    
    # 填充 max_left 数组
    max_left[0] = nums[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], nums[i])
    
    # 填充 min_right 数组
    min_right[-1] = nums[-1]
    for i in range(n - 2, -1, -1):
        min_right[i] = min(min_right[i + 1], nums[i])
    
    # 找到第一个满足条件的分割点
    for i in range(n - 1):
        if max_left[i] <= min_right[i + 1]:
            return i + 1

Solution = create_solution(partition_disjoint)