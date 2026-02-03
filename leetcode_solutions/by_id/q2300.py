# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2300
标题: Construct String With Repeat Limit
难度: medium
链接: https://leetcode.cn/problems/construct-string-with-repeat-limit/
题目类型: 贪心、哈希表、字符串、计数、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2182. 构造限制重复的字符串 - 给你一个字符串 s 和一个整数 repeatLimit ，用 s 中的字符构造一个新字符串 repeatLimitedString ，使任何字母 连续 出现的次数都不超过 repeatLimit 次。你不必使用 s 中的全部字符。 返回 字典序最大的 repeatLimitedString 。 如果在字符串 a 和 b 不同的第一个位置，字符串 a 中的字母在字母表中出现时间比字符串 b 对应的字母晚，则认为字符串 a 比字符串 b 字典序更大 。如果字符串中前 min(a.length, b.length) 个字符都相同，那么较长的字符串字典序更大。 示例 1： 输入：s = "cczazcc", repeatLimit = 3 输出："zzcccac" 解释：使用 s 中的所有字符来构造 repeatLimitedString "zzcccac"。 字母 'a' 连续出现至多 1 次。 字母 'c' 连续出现至多 3 次。 字母 'z' 连续出现至多 2 次。 因此，没有字母连续出现超过 repeatLimit 次，字符串是一个有效的 repeatLimitedString 。 该字符串是字典序最大的 repeatLimitedString ，所以返回 "zzcccac" 。 注意，尽管 "zzcccca" 字典序更大，但字母 'c' 连续出现超过 3 次，所以它不是一个有效的 repeatLimitedString 。 示例 2： 输入：s = "aababab", repeatLimit = 2 输出："bbabaa" 解释： 使用 s 中的一些字符来构造 repeatLimitedString "bbabaa"。 字母 'a' 连续出现至多 2 次。 字母 'b' 连续出现至多 2 次。 因此，没有字母连续出现超过 repeatLimit 次，字符串是一个有效的 repeatLimitedString 。 该字符串是字典序最大的 repeatLimitedString ，所以返回 "bbabaa" 。 注意，尽管 "bbabaaa" 字典序更大，但字母 'a' 连续出现超过 2 次，所以它不是一个有效的 repeatLimitedString 。 提示： * 1 <= repeatLimit <= s.length <= 105 * s 由小写英文字母组成
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
