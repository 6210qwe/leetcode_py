# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000280
标题: 不同的子序列
难度: hard
链接: https://leetcode.cn/problems/21dk04/
题目类型: 字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 097. 不同的子序列 - 给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。 字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是） 题目数据保证答案符合 32 位带符号整数范围。 示例 1： 输入：s = "rabbbit", t = "rabbit" 输出：3 解释： 如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。 rabbbit rabbbit rabbbit 示例 2： 输入：s = "babgbag", t = "bag" 输出：5 解释： 如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。 babgbag babgbag babgbag babgbag babgbag 提示： * 0 <= s.length, t.length <= 1000 * s 和 t 由英文字母组成 注意：本题与主站 115 题相同： https://leetcode.cn/problems/distinct-subsequences/ [https://leetcode.cn/problems/distinct-subsequences/]
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
