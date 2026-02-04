# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1556
标题: Make Two Arrays Equal by Reversing Subarrays
难度: easy
链接: https://leetcode.cn/problems/make-two-arrays-equal-by-reversing-subarrays/
题目类型: 数组、哈希表、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1460. 通过翻转子数组使两个数组相等 - 给你两个长度相同的整数数组 target 和 arr 。每一步中，你可以选择 arr 的任意 非空子数组 并将它翻转。你可以执行此过程任意次。 如果你能让 arr 变得与 target 相同，返回 True；否则，返回 False 。 示例 1： 输入：target = [1,2,3,4], arr = [2,4,1,3] 输出：true 解释：你可以按照如下步骤使 arr 变成 target： 1- 翻转子数组 [2,4,1] ，arr 变成 [1,4,2,3] 2- 翻转子数组 [4,2] ，arr 变成 [1,2,4,3] 3- 翻转子数组 [4,3] ，arr 变成 [1,2,3,4] 上述方法并不是唯一的，还存在多种将 arr 变成 target 的方法。 示例 2： 输入：target = [7], arr = [7] 输出：true 解释：arr 不需要做任何翻转已经与 target 相等。 示例 3： 输入：target = [3,7,9], arr = [3,7,11] 输出：false 解释：arr 没有数字 9 ，所以无论如何也无法变成 target 。 提示： * target.length == arr.length * 1 <= target.length <= 1000 * 1 <= target[i] <= 1000 * 1 <= arr[i] <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过比较两个数组的元素频率来判断是否可以通过翻转子数组使两个数组相等。

算法步骤:
1. 计算 target 和 arr 中每个元素的频率。
2. 比较两个频率字典，如果它们相等，则返回 True，否则返回 False。

关键点:
- 使用 Counter 来计算元素频率。
- 比较两个频率字典。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组的长度。因为我们需要遍历数组来计算频率。
空间复杂度: O(n)，用于存储频率字典。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import Counter
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def can_be_equal(target: List[int], arr: List[int]) -> bool:
    """
    函数式接口 - 判断是否可以通过翻转子数组使两个数组相等
    """
    # 计算 target 和 arr 中每个元素的频率
    target_count = Counter(target)
    arr_count = Counter(arr)

    # 比较两个频率字典
    return target_count == arr_count


Solution = create_solution(can_be_equal)