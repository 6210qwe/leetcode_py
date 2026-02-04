# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100329
标题: 统计目标成绩的出现次数
难度: easy
链接: https://leetcode.cn/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/
题目类型: 数组、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 172. 统计目标成绩的出现次数 - 某班级考试成绩按非严格递增顺序记录于整数数组 scores，请返回目标成绩 target 的出现次数。 示例 1： 输入: scores = [2, 2, 3, 4, 4, 4, 5, 6, 6, 8], target = 4 输出: 3 示例 2： 输入: scores = [1, 2, 3, 5, 7, 9], target = 6 输出: 0 提示： * 0 <= scores.length <= 105 * -109 <= scores[i] <= 109 * scores 是一个非递减数组 * -109 <= target <= 109 注意：本题与主站 34 题相同（仅返回值不同）：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/ [https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找找到目标成绩的起始和结束位置，然后计算出现次数。

算法步骤:
1. 使用二分查找找到目标成绩的左边界。
2. 使用二分查找找到目标成绩的右边界。
3. 计算出现次数：右边界 - 左边界 + 1。

关键点:
- 二分查找的实现需要考虑边界条件。
- 确保在找不到目标成绩时返回正确的结果。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(scores: List[int], target: int) -> int:
    """
    函数式接口 - 统计目标成绩的出现次数
    """
    def binary_search_left(nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def binary_search_right(nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    left = binary_search_left(scores, target)
    right = binary_search_right(scores, target)

    if left <= right and scores[left] == target:
        return right - left + 1
    else:
        return 0


Solution = create_solution(solution_function_name)