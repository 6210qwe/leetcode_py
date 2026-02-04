# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1756
标题: Minimum Deletions to Make String Balanced
难度: medium
链接: https://leetcode.cn/problems/minimum-deletions-to-make-string-balanced/
题目类型: 栈、字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1653. 使字符串平衡的最少删除次数 - 给你一个字符串 s ，它仅包含字符 'a' 和 'b' 。 你可以删除 s 中任意数目的字符，使得 s 平衡 。当不存在下标对 (i,j) 满足 i < j ，且 s[i] = 'b' 的同时 s[j]= 'a' ，此时认为 s 是 平衡 的。 请你返回使 s 平衡 的 最少 删除次数。 示例 1： 输入：s = "aababbab" 输出：2 解释：你可以选择以下任意一种方案： 下标从 0 开始，删除第 2 和第 6 个字符（"aababbab" -> "aaabbb"）， 下标从 0 开始，删除第 3 和第 6 个字符（"aababbab" -> "aabbbb"）。 示例 2： 输入：s = "bbaaaaabb" 输出：2 解释：唯一的最优解是删除最前面两个字符。 提示： * 1 <= s.length <= 105 * s[i] 要么是 'a' 要么是 'b' 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来计算最小删除次数。我们需要维护两个计数器：一个用于记录到目前为止遇到的 'b' 的数量，另一个用于记录需要删除的字符数量。

算法步骤:
1. 初始化两个变量：`b_count` 用于记录当前遇到的 'b' 的数量，`min_deletions` 用于记录最小删除次数。
2. 遍历字符串 `s`：
   - 如果当前字符是 'b'，则增加 `b_count`。
   - 如果当前字符是 'a'，则更新 `min_deletions` 为 `min(min_deletions + 1, b_count)`。
3. 返回 `min_deletions` 作为结果。

关键点:
- 动态规划的思想在于通过维护 `b_count` 和 `min_deletions` 来逐步计算最小删除次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串 s 的长度。我们只需要遍历字符串一次。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def minimum_deletions_to_make_string_balanced(s: str) -> int:
    """
    函数式接口 - 计算使字符串平衡的最少删除次数
    """
    b_count = 0
    min_deletions = 0
    
    for char in s:
        if char == 'b':
            b_count += 1
        elif char == 'a':
            min_deletions = min(min_deletions + 1, b_count)
    
    return min_deletions


Solution = create_solution(minimum_deletions_to_make_string_balanced)