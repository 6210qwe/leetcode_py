# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3948
标题: Maximum Number of Subsequences After One Inserting
难度: medium
链接: https://leetcode.cn/problems/maximum-number-of-subsequences-after-one-inserting/
题目类型: 贪心、字符串、动态规划、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3628. 插入一个字母的最大子序列数 - 给你一个由大写英文字母组成的字符串 s。 你可以在字符串的 任意 位置（包括字符串的开头或结尾）最多插入一个 大写英文字母。 返回在 最多插入一个字母 后，字符串中可以形成的 "LCT" 子序列的 最大 数量。 子序列 是从另一个字符串中删除某些字符（可以不删除）且不改变剩余字符顺序后得到的一个 非空 字符串。 示例 1： 输入： s = "LMCT" 输出： 2 解释： 可以在字符串 s 的开头插入一个 "L"，变为 "LLMCT"，其中包含 2 个子序列，分别位于下标 [0, 3, 4] 和 [1, 3, 4]。 示例 2： 输入： s = "LCCT" 输出： 4 解释： 可以在字符串 s 的开头插入一个 "L"，变为 "LLCCT"，其中包含 4 个子序列，分别位于下标 [0, 2, 4]、[0, 3, 4]、[1, 2, 4] 和 [1, 3, 4]。 示例 3： 输入： s = "L" 输出： 0 解释： 插入一个字母无法获得子序列 "LCT"，结果为 0。 提示： * 1 <= s.length <= 105 * s 仅由大写英文字母组成。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和来计算 "LCT" 子序列的数量，并考虑在不同位置插入字母的影响。

算法步骤:
1. 计算原字符串中 "L" 和 "C" 的前缀和。
2. 遍历字符串，计算在每个位置插入 "L"、"C" 和 "T" 后的 "LCT" 子序列数量。
3. 选择最大值作为结果。

关键点:
- 使用前缀和快速计算 "L" 和 "C" 的数量。
- 在遍历过程中，考虑插入 "L"、"C" 和 "T" 的影响。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_subsequences_after_inserting(s: str) -> int:
    """
    函数式接口 - 计算在最多插入一个字母后，字符串中可以形成的 "LCT" 子序列的最大数量。
    """
    n = len(s)
    if n < 3:
        return 0

    # 计算 "L" 和 "C" 的前缀和
    l_prefix = [0] * (n + 1)
    c_prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        l_prefix[i] = l_prefix[i - 1] + (s[i - 1] == 'L')
        c_prefix[i] = c_prefix[i - 1] + (s[i - 1] == 'C')

    # 计算原字符串中的 "LCT" 子序列数量
    original_count = 0
    t_count = 0
    for i in range(n - 1, -1, -1):
        if s[i] == 'T':
            t_count += 1
        elif s[i] == 'C':
            original_count += l_prefix[i] * t_count

    # 计算在不同位置插入 "L"、"C" 和 "T" 后的 "LCT" 子序列数量
    max_count = original_count
    for i in range(n + 1):
        if i == 0 or s[i - 1] != 'L':
            max_count = max(max_count, (l_prefix[i] + 1) * (c_prefix[n] - c_prefix[i]) * t_count)
        if i == n or s[i] != 'C':
            max_count = max(max_count, l_prefix[i] * (c_prefix[i] + 1) * t_count)
        if i == n or s[i] != 'T':
            max_count = max(max_count, l_prefix[i] * (c_prefix[n] - c_prefix[i]) * (t_count + 1))

    return max_count


Solution = create_solution(max_subsequences_after_inserting)