# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3482
标题: Construct String with Minimum Cost
难度: hard
链接: https://leetcode.cn/problems/construct-string-with-minimum-cost/
题目类型: 数组、字符串、动态规划、后缀数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3213. 最小代价构造字符串 - 给你一个字符串 target、一个字符串数组 words 以及一个整数数组 costs，这两个数组长度相同。 设想一个空字符串 s。 你可以执行以下操作任意次数（包括 零 次）： * 选择一个在范围 [0, words.length - 1] 的索引 i。 * 将 words[i] 追加到 s。 * 该操作的成本是 costs[i]。 返回使 s 等于 target 的 最小 成本。如果不可能，返回 -1。 示例 1： 输入： target = "abcdef", words = ["abdef","abc","d","def","ef"], costs = [100,1,1,10,5] 输出： 7 解释： * 选择索引 1 并以成本 1 将 "abc" 追加到 s，得到 s = "abc"。 * 选择索引 2 并以成本 1 将 "d" 追加到 s，得到 s = "abcd"。 * 选择索引 4 并以成本 5 将 "ef" 追加到 s，得到 s = "abcdef"。 示例 2： 输入： target = "aaaa", words = ["z","zz","zzz"], costs = [1,10,100] 输出： -1 解释： 无法使 s 等于 target，因此返回 -1。 提示： * 1 <= target.length <= 5 * 104 * 1 <= words.length == costs.length <= 5 * 104 * 1 <= words[i].length <= target.length * 所有 words[i].length 的总和小于或等于 5 * 104 * target 和 words[i] 仅由小写英文字母组成。 * 1 <= costs[i] <= 104
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
