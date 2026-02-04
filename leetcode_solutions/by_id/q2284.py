# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2284
标题: Smallest Value of the Rearranged Number
难度: medium
链接: https://leetcode.cn/problems/smallest-value-of-the-rearranged-number/
题目类型: 数学、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2165. 重排数字的最小值 - 给你一个整数 num 。重排 num 中的各位数字，使其值 最小化 且不含 任何 前导零。 返回不含前导零且值最小的重排数字。 注意，重排各位数字后，num 的符号不会改变。 示例 1： 输入：num = 310 输出：103 解释：310 中各位数字的可行排列有：013、031、103、130、301、310 。 不含任何前导零且值最小的重排数字是 103 。 示例 2： 输入：num = -7605 输出：-7650 解释：-7605 中各位数字的部分可行排列为：-7650、-6705、-5076、-0567。 不含任何前导零且值最小的重排数字是 -7650 。 提示： * -1015 <= num <= 1015
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 将数字的各位数字分离，然后根据正负号进行排序，最后重组数字。

算法步骤:
1. 将数字转换为字符串，以便逐位处理。
2. 分离出所有非零数字和零数字。
3. 对于正数，将非零数字按升序排序，并将第一个非零数字放在最前面，其余零数字放在后面。
4. 对于负数，将所有数字按降序排序。
5. 重组数字并返回结果。

关键点:
- 处理前导零时，确保第一个数字是非零数字。
- 负数时，直接按降序排序以获得最大值（即最小的负数）。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(d log d)，其中 d 是数字的位数。排序操作的时间复杂度为 O(d log d)。
空间复杂度: O(d)，存储分离的数字需要 O(d) 的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def smallest_value_rearranged(num: int) -> int:
    """
    函数式接口 - 重排数字的最小值
    """
    if num == 0:
        return 0

    is_negative = num < 0
    num_str = str(abs(num))
    
    # 分离非零数字和零数字
    non_zero_digits = [d for d in num_str if d != '0']
    zero_digits = [d for d in num_str if d == '0']
    
    # 排序
    if is_negative:
        non_zero_digits.sort(reverse=True)
    else:
        non_zero_digits.sort()
        non_zero_digits[0], non_zero_digits[-1] = non_zero_digits[-1], non_zero_digits[0]
    
    # 重组数字
    result_str = ''.join(non_zero_digits + zero_digits)
    result = int(result_str)
    
    return -result if is_negative else result


Solution = create_solution(smallest_value_rearranged)