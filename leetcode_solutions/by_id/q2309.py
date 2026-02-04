# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2309
标题: Maximize Number of Subsequences in a String
难度: medium
链接: https://leetcode.cn/problems/maximize-number-of-subsequences-in-a-string/
题目类型: 贪心、字符串、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2207. 字符串中最多数目的子序列 - 给你一个下标从 0 开始的字符串 text 和另一个下标从 0 开始且长度为 2 的字符串 pattern ，两者都只包含小写英文字母。 你可以在 text 中任意位置插入 一个 字符，这个插入的字符必须是 pattern[0] 或者 pattern[1] 。注意，这个字符可以插入在 text 开头或者结尾的位置。 请你返回插入一个字符后，text 中最多包含多少个等于 pattern 的 子序列 。 子序列 指的是将一个字符串删除若干个字符后（也可以不删除），剩余字符保持原本顺序得到的字符串。 示例 1： 输入：text = "abdcdbc", pattern = "ac" 输出：4 解释： 如果我们在 text[1] 和 text[2] 之间添加 pattern[0] = 'a' ，那么我们得到 "abadcdbc" 。那么 "ac" 作为子序列出现 4 次。 其他得到 4 个 "ac" 子序列的方案还有 "aabdcdbc" 和 "abdacdbc" 。 但是，"abdcadbc" ，"abdccdbc" 和 "abdcdbcc" 这些字符串虽然是可行的插入方案，但是只出现了 3 次 "ac" 子序列，所以不是最优解。 可以证明插入一个字符后，无法得到超过 4 个 "ac" 子序列。 示例 2： 输入：text = "aabb", pattern = "ab" 输出：6 解释： 可以得到 6 个 "ab" 子序列的部分方案为 "aaabb" ，"aaabb" 和 "aabbb" 。 提示： * 1 <= text.length <= 105 * pattern.length == 2 * text 和 pattern 都只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过计算当前文本中 pattern[0] 和 pattern[1] 的数量，并考虑在开头或结尾插入一个字符来最大化子序列的数量。

算法步骤:
1. 计算 text 中 pattern[0] 和 pattern[1] 的数量。
2. 计算当前 text 中 pattern 作为子序列出现的次数。
3. 考虑在开头或结尾插入一个字符来最大化子序列的数量。

关键点:
- 使用前缀和的思想来计算当前 text 中 pattern 作为子序列出现的次数。
- 通过在开头或结尾插入一个字符来最大化子序列的数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 text 的长度。
空间复杂度: O(1)，只需要常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def maximize_subsequences(text: str, pattern: str) -> int:
    """
    函数式接口 - 计算在 text 中插入一个字符后，最多包含多少个等于 pattern 的子序列。
    """
    # 计算 text 中 pattern[0] 和 pattern[1] 的数量
    count_p0 = 0
    count_p1 = 0
    for char in text:
        if char == pattern[0]:
            count_p0 += 1
        elif char == pattern[1]:
            count_p1 += 1
    
    # 计算当前 text 中 pattern 作为子序列出现的次数
    subsequences = 0
    p0_count = 0
    for char in text:
        if char == pattern[0]:
            p0_count += 1
        elif char == pattern[1]:
            subsequences += p0_count
    
    # 考虑在开头或结尾插入一个字符来最大化子序列的数量
    max_subsequences = subsequences + max(count_p0, count_p1)
    
    return max_subsequences


Solution = create_solution(maximize_subsequences)