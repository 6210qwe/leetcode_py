# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100232
标题: Search Rotate Array LCCI
难度: medium
链接: https://leetcode.cn/problems/search-rotate-array-lcci/
题目类型: 数组、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 10.03. 搜索旋转数组 - 搜索旋转数组。给定一个排序后的数组，包含n个整数，但这个数组已被旋转过很多次了，次数不详。请编写代码找出数组中的某个元素，假设数组元素原先是按升序排列的。若有多个相同元素，返回索引值最小的一个。 示例 1： 输入：arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 5 输出：8（元素5在该数组中的索引） 示例 2： 输入：arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 11 输出：-1 （没有找到） 提示: 1. arr 长度范围在[1, 1000000]之间
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找来解决这个问题。由于数组被旋转过，我们需要处理两种情况：左半部分有序和右半部分有序。

算法步骤:
1. 初始化左右指针 left 和 right。
2. 进行二分查找：
   - 计算中间位置 mid。
   - 如果 arr[mid] == target，检查左侧是否有相同的元素，如果有则更新结果。
   - 如果左半部分有序：
     - 如果 target 在左半部分范围内，移动 right 指针。
     - 否则，移动 left 指针。
   - 如果右半部分有序：
     - 如果 target 在右半部分范围内，移动 left 指针。
     - 否则，移动 right 指针。
3. 返回结果。

关键点:
- 通过比较中间元素与左右边界元素，确定哪一部分是有序的。
- 处理重复元素时，需要向左查找以找到最小索引。
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


def search_rotated_array(arr: List[int], target: int) -> int:
    """
    函数式接口 - 搜索旋转数组
    """
    if not arr:
        return -1

    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            # 查找左侧是否有相同的元素
            while result > 0 and arr[result - 1] == target:
                result -= 1
            return result

        # 左半部分有序
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # 右半部分有序
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return result


Solution = create_solution(search_rotated_array)