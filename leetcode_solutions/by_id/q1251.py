# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1251
标题: Longest Chunked Palindrome Decomposition
难度: hard
链接: https://leetcode.cn/problems/longest-chunked-palindrome-decomposition/
题目类型: 贪心、双指针、字符串、动态规划、哈希函数、滚动哈希
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1147. 段式回文 - 你会得到一个字符串 text 。你应该把它分成 k 个子字符串 (subtext1, subtext2，…， subtextk) ，要求满足: * subtexti 是 非空 字符串 * 所有子字符串的连接等于 text ( 即subtext1 + subtext2 + ... + subtextk == text ) * 对于所有 i 的有效值( 即 1 <= i <= k ) ，subtexti == subtextk - i + 1 均成立 返回k可能最大值。 示例 1： 输入：text = "ghiabcdefhelloadamhelloabcdefghi" 输出：7 解释：我们可以把字符串拆分成 "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)"。 示例 2： 输入：text = "merchant" 输出：1 解释：我们可以把字符串拆分成 "(merchant)"。 示例 3： 输入：text = "antaprezatepzapreanta" 输出：11 解释：我们可以把字符串拆分成 "(a)(nt)(a)(pre)(za)(tep)(za)(pre)(a)(nt)(a)"。 提示： * 1 <= text.length <= 1000 * text 仅由小写英文字符组成
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
