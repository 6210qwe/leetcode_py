# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100291
标题: 训练计划 I
难度: easy
链接: https://leetcode.cn/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/
题目类型: 数组、双指针、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 139. 训练计划 I - 教练使用整数数组 actions 记录一系列核心肌群训练项目编号。为增强训练趣味性，需要将所有奇数编号训练项目调整至偶数编号训练项目之前。请将调整后的训练项目编号以 数组 形式返回。 示例 1： 输入：actions = [1,2,3,4,5] 输出：[1,3,5,2,4] 解释：为正确答案之一 提示： * 0 <= actions.length <= 50000 * 0 <= actions[i] <= 10000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针方法，一个指针从左向右找到第一个偶数，另一个指针从右向左找到第一个奇数，然后交换这两个元素。

算法步骤:
1. 初始化两个指针 left 和 right，分别指向数组的起始和末尾。
2. 当 left < right 时，执行以下操作：
   - 如果 actions[left] 是奇数，left 向右移动一位。
   - 如果 actions[right] 是偶数，right 向左移动一位。
   - 如果 actions[left] 是偶数且 actions[right] 是奇数，交换它们的位置。
3. 返回调整后的数组。

关键点:
- 使用双指针可以有效地在 O(n) 时间复杂度内完成任务。
- 仅使用常数级别的额外空间。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组的长度。每个元素最多被访问两次。
空间复杂度: O(1)，只使用了常数级别的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(actions: List[int]) -> List[int]:
    """
    函数式接口 - 实现
    """
    if not actions:
        return []

    left, right = 0, len(actions) - 1
    while left < right:
        # 移动左指针直到找到偶数
        while left < right and actions[left] % 2 == 1:
            left += 1
        # 移动右指针直到找到奇数
        while left < right and actions[right] % 2 == 0:
            right -= 1
        # 交换奇数和偶数
        if left < right:
            actions[left], actions[right] = actions[right], actions[left]
            left += 1
            right -= 1

    return actions


Solution = create_solution(solution_function_name)