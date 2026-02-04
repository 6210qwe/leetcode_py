# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3582
标题: Find Indices of Stable Mountains
难度: easy
链接: https://leetcode.cn/problems/find-indices-of-stable-mountains/
题目类型: 数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3285. 找到稳定山的下标 - 有 n 座山排成一列，每座山都有一个高度。给你一个整数数组 height ，其中 height[i] 表示第 i 座山的高度，再给你一个整数 threshold 。 对于下标不为 0 的一座山，如果它左侧相邻的山的高度 严格大于 threshold ，那么我们称它是 稳定 的。我们定义下标为 0 的山 不是 稳定的。 请你返回一个数组，包含所有 稳定 山的下标，你可以以 任意 顺序返回下标数组。 示例 1： 输入：height = [1,2,3,4,5], threshold = 2 输出：[3,4] 解释： * 下标为 3 的山是稳定的，因为 height[2] == 3 大于 threshold == 2 。 * 下标为 4 的山是稳定的，因为 height[3] == 4 大于 threshold == 2. 示例 2： 输入：height = [10,1,10,1,10], threshold = 3 输出：[1,3] 示例 3： 输入：height = [10,1,10,1,10], threshold = 10 输出：[] 提示： * 2 <= n == height.length <= 100 * 1 <= height[i] <= 100 * 1 <= threshold <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过一次遍历数组来找到所有满足条件的稳定山的下标。

算法步骤:
1. 初始化一个空列表 `stable_indices` 用于存储稳定山的下标。
2. 从下标 1 开始遍历数组 `height`，检查每个山的左侧相邻山的高度是否大于 `threshold`。
3. 如果满足条件，则将当前山的下标添加到 `stable_indices` 中。
4. 返回 `stable_indices` 列表。

关键点:
- 从下标 1 开始遍历，避免处理下标 0 的特殊情况。
- 仅使用常数级额外空间。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组 `height` 的长度。我们只需要一次遍历数组。
空间复杂度: O(1)，除了返回结果外，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_stable_mountain_indices(height: List[int], threshold: int) -> List[int]:
    """
    函数式接口 - 找到所有稳定山的下标
    """
    stable_indices = []
    for i in range(1, len(height)):
        if height[i - 1] > threshold:
            stable_indices.append(i)
    return stable_indices


Solution = create_solution(find_stable_mountain_indices)