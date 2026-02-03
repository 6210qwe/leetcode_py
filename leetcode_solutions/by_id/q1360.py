# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1360
标题: Maximum Length of a Concatenated String with Unique Characters
难度: medium
链接: https://leetcode.cn/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
题目类型: 位运算、数组、字符串、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1239. 串联字符串的最大长度 - 给定一个字符串数组 arr，字符串 s 是将 arr 的含有 不同字母 的 子序列 字符串 连接 所得的字符串。 请返回所有可行解 s 中最长长度。 子序列 是一种可以从另一个数组派生而来的数组，通过删除某些元素或不删除元素而不改变其余元素的顺序。 示例 1： 输入：arr = ["un","iq","ue"] 输出：4 解释：所有可能的串联组合是： - "" - "un" - "iq" - "ue" - "uniq" ("un" + "iq") - "ique" ("iq" + "ue") 最大长度为 4。 示例 2： 输入：arr = ["cha","r","act","ers"] 输出：6 解释：可能的解答有 "chaers" 和 "acters"。 示例 3： 输入：arr = ["abcdefghijklmnopqrstuvwxyz"] 输出：26 提示： * 1 <= arr.length <= 16 * 1 <= arr[i].length <= 26 * arr[i] 中只含有小写英文字母
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
