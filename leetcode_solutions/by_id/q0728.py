# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 728
标题: Self Dividing Numbers
难度: easy
链接: https://leetcode.cn/problems/self-dividing-numbers/
题目类型: 数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
728. 自除数 - 自除数 是指可以被它包含的每一位数整除的数。 * 例如，128 是一个 自除数 ，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。 自除数 不允许包含 0 。 给定两个整数 left 和 right ，返回一个列表，列表的元素是范围 [left, right]（包括两个端点）内所有的 自除数 。 示例 1： 输入：left = 1, right = 22 输出：[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22] 示例 2: 输入：left = 47, right = 85 输出：[48,55,66,77] 提示： * 1 <= left <= right <= 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 检查每个数字是否为自除数

算法步骤:
1. 定义一个辅助函数 `is_self_dividing` 来判断一个数字是否为自除数。
2. 遍历从 `left` 到 `right` 的所有数字，使用 `is_self_dividing` 函数筛选出自除数。

关键点:
- 使用字符串操作来提取数字的每一位。
- 确保数字中不包含 0。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * d)，其中 n 是区间 [left, right] 的长度，d 是数字的最大位数（最多为 5 位）。
空间复杂度: O(1)，除了输出结果外，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def is_self_dividing(num: int) -> bool:
    """
    判断一个数字是否为自除数
    """
    original_num = num
    while num > 0:
        digit = num % 10
        if digit == 0 or original_num % digit != 0:
            return False
        num //= 10
    return True


def solution_function_name(left: int, right: int) -> List[int]:
    """
    返回范围 [left, right] 内的所有自除数
    """
    result = []
    for num in range(left, right + 1):
        if is_self_dividing(num):
            result.append(num)
    return result


Solution = create_solution(solution_function_name)