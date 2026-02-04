# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2632
标题: Apply Bitwise Operations to Make Strings Equal
难度: medium
链接: https://leetcode.cn/problems/apply-bitwise-operations-to-make-strings-equal/
题目类型: 位运算、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2546. 执行逐位运算使字符串相等 - 给你两个下标从 0 开始的 二元 字符串 s 和 target ，两个字符串的长度均为 n 。你可以对 s 执行下述操作 任意 次： * 选择两个 不同 的下标 i 和 j ，其中 0 <= i, j < n 。 * 同时，将 s[i] 替换为 (s[i] OR s[j]) ，s[j] 替换为 (s[i] XOR s[j]) 。 例如，如果 s = "0110" ，你可以选择 i = 0 和 j = 2，然后同时将 s[0] 替换为 (s[0] OR s[2] = 0 OR 1 = 1)，并将 s[2] 替换为 (s[0] XOR s[2] = 0 XOR 1 = 1)，最终得到 s = "1110" 。 如果可以使 s 等于 target ，返回 true ，否则，返回 false 。 示例 1： 输入：s = "1010", target = "0110" 输出：true 解释：可以执行下述操作： - 选择 i = 2 和 j = 0 ，得到 s = "0010". - 选择 i = 2 和 j = 1 ，得到 s = "0110". 可以使 s 等于 target ，返回 true 。 示例 2： 输入：s = "11", target = "00" 输出：false 解释：执行任意次操作都无法使 s 等于 target 。 提示： * n == s.length == target.length * 2 <= n <= 105 * s 和 target 仅由数字 0 和 1 组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过观察可以发现，只要 s 和 target 中至少有一个 1，那么可以通过一系列操作将 s 转换为 target。如果 s 和 target 中都没有 1，则必须两者都为全 0。

算法步骤:
1. 检查 s 和 target 中是否至少有一个 1。
2. 如果 s 和 target 中至少有一个 1，则返回 True。
3. 如果 s 和 target 中都没有 1，则检查 s 和 target 是否都为全 0，如果是则返回 True，否则返回 False。

关键点:
- 只要 s 和 target 中至少有一个 1，就可以通过操作将 s 转换为 target。
- 如果 s 和 target 中都没有 1，则必须两者都为全 0。
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


def can_make_strings_equal(s: str, target: str) -> bool:
    """
    函数式接口 - 判断是否可以通过位运算使字符串 s 等于 target
    """
    # 检查 s 和 target 中是否至少有一个 1
    has_one_in_s = '1' in s
    has_one_in_target = '1' in target

    # 如果 s 和 target 中至少有一个 1，则可以转换
    if has_one_in_s or has_one_in_target:
        return has_one_in_s and has_one_in_target

    # 如果 s 和 target 中都没有 1，则必须两者都为全 0
    return s == target


Solution = create_solution(can_make_strings_equal)