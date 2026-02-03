# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3360
标题: Minimum Deletions to Make String K-Special
难度: medium
链接: https://leetcode.cn/problems/minimum-deletions-to-make-string-k-special/
题目类型: 贪心、哈希表、字符串、计数、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3085. 成为 K 特殊字符串需要删除的最少字符数 - 给你一个字符串 word 和一个整数 k。 如果 |freq(word[i]) - freq(word[j])| <= k 对于字符串中所有下标 i 和 j 都成立，则认为 word 是 k 特殊字符串。 此处，freq(x) 表示字符 x 在 word 中的出现频率，而 |y| 表示 y 的绝对值。 返回使 word 成为 k 特殊字符串 需要删除的字符的最小数量。 示例 1： 输入：word = "aabcaba", k = 0 输出：3 解释：可以删除 2 个 "a" 和 1 个 "c" 使 word 成为 0 特殊字符串。word 变为 "baba"，此时 freq('a') == freq('b') == 2。 示例 2： 输入：word = "dabdcbdcdcd", k = 2 输出：2 解释：可以删除 1 个 "a" 和 1 个 "d" 使 word 成为 2 特殊字符串。word 变为 "bdcbdcdcd"，此时 freq('b') == 2，freq('c') == 3，freq('d') == 4。 示例 3： 输入：word = "aaabaaa", k = 2 输出：1 解释：可以删除 1 个 "b" 使 word 成为 2特殊字符串。因此，word 变为 "aaaaaa"，此时每个字母的频率都是 6。 提示： * 1 <= word.length <= 105 * 0 <= k <= 105 * word 仅由小写英文字母组成。
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
