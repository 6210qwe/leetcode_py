# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3707
标题: Find the Most Common Response
难度: medium
链接: https://leetcode.cn/problems/find-the-most-common-response/
题目类型: 数组、哈希表、字符串、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3527. 找到最常见的回答 - 给你一个二维字符串数组 responses，其中每个 responses[i] 是一个字符串数组，表示第 i 天调查的回答结果。 请返回在对每个 responses[i] 中的回答 去重 后，所有天数中 最常见 的回答。如果有多个回答出现频率相同，则返回 字典序最小 的那个回答。 示例 1： 输入： responses = [["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]] 输出： "good" 解释： * 每个列表去重后，得到 responses = [["good", "ok"], ["ok", "bad", "good"], ["good"], ["bad"]]。 * "good" 出现了 3 次，"ok" 出现了 2 次，"bad" 也出现了 2 次。 * 返回 "good"，因为它出现的频率最高。 示例 2： 输入： responses = [["good","ok","good"],["ok","bad"],["bad","notsure"],["great","good"]] 输出： "bad" 解释： * 每个列表去重后，responses = [["good", "ok"], ["ok", "bad"], ["bad", "notsure"], ["great", "good"]]。 * "bad"、"good" 和 "ok" 都出现了 2 次。 * 返回 "bad"，因为它在这些最高频率的词中字典序最小。 提示： * 1 <= responses.length <= 1000 * 1 <= responses[i].length <= 1000 * 1 <= responses[i][j].length <= 10 * responses[i][j] 仅由小写英文字母组成
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
