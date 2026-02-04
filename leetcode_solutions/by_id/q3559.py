# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3559
标题: Minimum Number of Valid Strings to Form Target I
难度: medium
链接: https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-i/
题目类型: 字典树、线段树、数组、字符串、二分查找、动态规划、字符串匹配、哈希函数、滚动哈希
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3291. 形成目标字符串需要的最少字符串数 I - 给你一个字符串数组 words 和一个字符串 target。 如果字符串 x 是 words 中 任意 字符串的 前缀，则认为 x 是一个 有效 字符串。 现计划通过 连接 有效字符串形成 target ，请你计算并返回需要连接的 最少 字符串数量。如果无法通过这种方式形成 target，则返回 -1。 示例 1： 输入： words = ["abc","aaaaa","bcdef"], target = "aabcdabc" 输出： 3 解释： target 字符串可以通过连接以下有效字符串形成： * words[1] 的长度为 2 的前缀，即 "aa"。 * words[2] 的长度为 3 的前缀，即 "bcd"。 * words[0] 的长度为 3 的前缀，即 "abc"。 示例 2： 输入： words = ["abababab","ab"], target = "ababaababa" 输出： 2 解释： target 字符串可以通过连接以下有效字符串形成： * words[0] 的长度为 5 的前缀，即 "ababa"。 * words[0] 的长度为 5 的前缀，即 "ababa"。 示例 3： 输入： words = ["abcdef"], target = "xyz" 输出： -1 提示： * 1 <= words.length <= 100 * 1 <= words[i].length <= 5 * 103 * 输入确保 sum(words[i].length) <= 105。 * words[i] 只包含小写英文字母。 * 1 <= target.length <= 5 * 103 * target 只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们定义 dp[i] 表示形成 target[:i] 所需的最少字符串数量。对于每个位置 i，我们尝试使用 words 中的每个字符串作为前缀，并更新 dp 数组。

算法步骤:
1. 初始化 dp 数组，dp[0] = 0，其他位置初始化为无穷大。
2. 遍历 target 的每个字符，对于每个字符，遍历 words 中的每个字符串，检查其是否是当前子字符串的前缀。
3. 更新 dp 数组，如果可以使用某个字符串作为前缀，则更新 dp[i + len(word)]。
4. 最后，返回 dp[len(target)]，如果其值为无穷大，说明无法形成 target，返回 -1。

关键点:
- 使用动态规划来记录形成 target 每个前缀所需的最少字符串数量。
- 遍历 words 中的每个字符串，检查其是否是当前子字符串的前缀。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m * k)，其中 n 是 target 的长度，m 是 words 的长度，k 是 words 中最长字符串的长度。
空间复杂度: O(n)，其中 n 是 target 的长度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_valid_strings_to_form_target(words: List[str], target: str) -> int:
    """
    函数式接口 - 计算形成目标字符串所需的最少字符串数量
    """
    n = len(target)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(n):
        for word in words:
            if target[i:i+len(word)] == word:
                dp[i + len(word)] = min(dp[i + len(word)], dp[i] + 1)

    return dp[n] if dp[n] != float('inf') else -1


Solution = create_solution(min_valid_strings_to_form_target)