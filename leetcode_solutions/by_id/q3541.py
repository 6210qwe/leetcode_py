# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3541
标题: Report Spam Message
难度: medium
链接: https://leetcode.cn/problems/report-spam-message/
题目类型: 数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3295. 举报垃圾信息 - 给你一个字符串数组 message 和一个字符串数组 bannedWords。 如果数组中 至少 存在两个单词与 bannedWords 中的任一单词 完全相同，则该数组被视为 垃圾信息。 如果数组 message 是垃圾信息，则返回 true；否则返回 false。 示例 1： 输入： message = ["hello","world","leetcode"], bannedWords = ["world","hello"] 输出： true 解释： 数组 message 中的 "hello" 和 "world" 都出现在数组 bannedWords 中。 示例 2： 输入： message = ["hello","programming","fun"], bannedWords = ["world","programming","leetcode"] 输出： false 解释： 数组 message 中只有一个单词（"programming"）出现在数组 bannedWords 中。 提示： * 1 <= message.length, bannedWords.length <= 105 * 1 <= message[i].length, bannedWords[i].length <= 15 * message[i] 和 bannedWords[i] 都只由小写英文字母组成。
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
