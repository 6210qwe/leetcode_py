# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 963
标题: Three Equal Parts
难度: hard
链接: https://leetcode.cn/problems/three-equal-parts/
题目类型: 数组、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
927. 三等分 - 给定一个由 0 和 1 组成的数组 arr ，将数组分成 3 个非空的部分 ，使得所有这些部分表示相同的二进制值。 如果可以做到，请返回任何 [i, j]，其中 i+1 < j，这样一来： * arr[0], arr[1], ..., arr[i] 为第一部分； * arr[i + 1], arr[i + 2], ..., arr[j - 1] 为第二部分； * arr[j], arr[j + 1], ..., arr[arr.length - 1] 为第三部分。 * 这三个部分所表示的二进制值相等。 如果无法做到，就返回 [-1, -1]。 注意，在考虑每个部分所表示的二进制时，应当将其看作一个整体。例如，[1,1,0] 表示十进制中的 6，而不会是 3。此外，前导零也是被允许的，所以 [0,1,1] 和 [1,1] 表示相同的值。 示例 1： 输入：arr = [1,0,1,0,1] 输出：[0,3] 示例 2： 输入：arr = [1,1,0,1,1] 输出：[-1,-1] 示例 3: 输入：arr = [1,1,0,0,1] 输出：[0,2] 提示： * 3 <= arr.length <= 3 * 104 * arr[i] 是 0 或 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过统计数组中 1 的位置来确定三个部分的划分点，并验证这些部分是否相等。

算法步骤:
1. 计算数组中 1 的总数。
2. 如果 1 的总数不是 3 的倍数，直接返回 [-1, -1]。
3. 找到每部分的第一个 1 的位置。
4. 比较三部分的二进制值是否相等。
5. 如果相等，返回划分点；否则返回 [-1, -1]。

关键点:
- 通过 1 的位置来确定划分点。
- 验证三部分的二进制值是否相等。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(arr: List[int]) -> List[int]:
    """
    函数式接口 - 将数组分成三个相等的二进制部分
    """
    n = len(arr)
    ones = [i for i, x in enumerate(arr) if x == 1]
    num_ones = len(ones)

    if num_ones % 3 != 0:
        return [-1, -1]

    if num_ones == 0:
        return [0, n - 1]

    part_length = num_ones // 3
    first_part_start = ones[0]
    second_part_start = ones[part_length]
    third_part_start = ones[2 * part_length]

    if (n - third_part_start) < (second_part_start - first_part_start):
        return [-1, -1]

    for i in range(part_length):
        if arr[first_part_start + i] != arr[second_part_start + i] or arr[first_part_start + i] != arr[third_part_start + i]:
            return [-1, -1]

    return [first_part_start + part_length - 1, second_part_start + part_length]


Solution = create_solution(solution_function_name)