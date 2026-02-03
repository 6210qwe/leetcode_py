# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000237
标题: 两数之和 II - 输入有序数组
难度: easy
链接: https://leetcode.cn/problems/kLl5u1/
题目类型: 数组、双指针、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 006. 两数之和 II - 输入有序数组 - 给定一个已按照 升序排列 的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。 函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 0 开始计数 ，所以答案数组应当满足 0 <= answer[0] < answer[1] < numbers.length 。 假设数组中存在且只存在一对符合条件的数字，同时一个数字不能使用两次。 示例 1： 输入：numbers = [1,2,4,6,10], target = 8 输出：[1,3] 解释：2 与 6 之和等于目标数 8 。因此 index1 = 1, index2 = 3 。 示例 2： 输入：numbers = [2,3,4], target = 6 输出：[0,2] 示例 3： 输入：numbers = [-1,0], target = -1 输出：[0,1] 提示： * 2 <= numbers.length <= 3 * 104 * -1000 <= numbers[i] <= 1000 * numbers 按 非递减顺序 排列 * -1000 <= target <= 1000 * 仅存在一个有效答案 注意：本题与主站 167 题相似（下标起点不同）：https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/ [https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 有序数组 + 双指针

算法步骤:
1. 定义两个指针 left = 0, right = len(numbers) - 1
2. 当 left < right 时：
   - 计算当前和 s = numbers[left] + numbers[right]
   - 若 s == target，返回 [left, right]
   - 若 s < target，left += 1（需要更大）
   - 若 s > target，right -= 1（需要更小）
3. 题目保证一定有且仅有一个解，所以循环内必然返回

关键点:
- 数组已按非递减顺序排序，双指针能在 O(n) 时间内找到目标
- 下标要求从 0 开始且 left < right
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - n 为数组长度
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def two_sum(numbers: List[int], target: int) -> List[int]:
    """
    函数式接口 - 两数之和 II（输入有序数组，下标从 0 开始）
    """
    left, right = 0, len(numbers) - 1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left, right]
        if s < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]


Solution = create_solution(two_sum)
