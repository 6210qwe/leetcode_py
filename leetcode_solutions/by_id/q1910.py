# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1910
标题: Check if Binary String Has at Most One Segment of Ones
难度: easy
链接: https://leetcode.cn/problems/check-if-binary-string-has-at-most-one-segment-of-ones/
题目类型: 字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1784. 检查二进制字符串字段 - 给你一个二进制字符串 s ，该字符串 不含前导零 。 如果 s 包含 零个或一个由连续的 '1' 组成的字段 ，返回 true 。否则，返回 false 。 示例 1： 输入：s = "1001" 输出：false 解释：由连续若干个 '1' 组成的字段数量为 2，返回 false 示例 2： 输入：s = "110" 输出：true 提示： * 1 <= s.length <= 100 * s[i] 为 '0' 或 '1' * s[0] 为 '1'
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过遍历字符串来检查是否存在多于一个由连续 '1' 组成的段。

算法步骤:
1. 初始化一个标志变量 `found_one_segment` 为 False。
2. 遍历字符串，如果遇到 '1'，检查 `found_one_segment` 是否为 True，如果是则返回 False。
3. 如果遇到 '0' 且 `found_one_segment` 为 True，则将 `found_one_segment` 置为 False。
4. 遍历结束后，返回 True。

关键点:
- 只需要一次遍历来检查是否存在多于一个由连续 '1' 组成的段。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串 s 的长度。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def check_ones_segment(s: str) -> bool:
    """
    函数式接口 - 检查二进制字符串是否包含最多一个由连续 '1' 组成的段。
    """
    found_one_segment = False
    
    for char in s:
        if char == '1':
            if found_one_segment:
                return False
            found_one_segment = True
        elif char == '0' and found_one_segment:
            found_one_segment = False
    
    return True


Solution = create_solution(check_ones_segment)