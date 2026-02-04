# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 691
标题: Stickers to Spell Word
难度: hard
链接: https://leetcode.cn/problems/stickers-to-spell-word/
题目类型: 位运算、记忆化搜索、数组、哈希表、字符串、动态规划、回溯、状态压缩
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
691. 贴纸拼词 - 我们有 n 种不同的贴纸。每个贴纸上都有一个小写的英文单词。 您想要拼写出给定的字符串 target ，方法是从收集的贴纸中切割单个字母并重新排列它们。如果你愿意，你可以多次使用每个贴纸，每个贴纸的数量是无限的。 返回你需要拼出 target 的最小贴纸数量。如果任务不可能，则返回 -1 。 注意：在所有的测试用例中，所有的单词都是从 1000 个最常见的美国英语单词中随机选择的，并且 target 被选择为两个随机单词的连接。 示例 1： 输入：stickers = ["with","example","science"], target = "thehat" 输出：3 解释： 我们可以使用 2 个 "with" 贴纸，和 1 个 "example" 贴纸。 把贴纸上的字母剪下来并重新排列后，就可以形成目标 “thehat“ 了。 此外，这是形成目标字符串所需的最小贴纸数量。 示例 2: 输入：stickers = ["notice","possible"], target = "basicbasic" 输出：-1 解释：我们不能通过剪切给定贴纸的字母来形成目标“basicbasic”。 提示: * n == stickers.length * 1 <= n <= 50 * 1 <= stickers[i].length <= 10 * 1 <= target.length <= 15 * stickers[i] 和 target 由小写英文单词组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用记忆化搜索（带备忘录的递归）来解决这个问题。我们将目标字符串的状态表示为一个掩码，然后尝试使用每张贴纸来减少这个掩码中的字符需求。

算法步骤:
1. 将目标字符串转换为字符计数。
2. 对于每张贴纸，计算它可以提供的字符。
3. 使用记忆化搜索来尝试使用每张贴纸来减少目标字符串的需求。
4. 如果目标字符串的所有字符都被满足，返回使用的贴纸数量；否则返回 -1。

关键点:
- 使用掩码来表示目标字符串的状态。
- 记忆化搜索避免重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^m * n)，其中 m 是 target 的长度，n 是 stickers 的长度。因为每个状态最多有 2^m 种可能，每种状态需要遍历 n 张贴纸。
空间复杂度: O(2^m)，因为我们需要存储每个状态的结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_stickers(stickers: List[str], target: str) -> int:
    from collections import Counter
    from functools import lru_cache

    # 将目标字符串转换为字符计数
    target_count = Counter(target)
    sticker_counts = [Counter(sticker) for sticker in stickers]

    # 过滤掉对目标字符串没有贡献的贴纸
    useful_stickers = [sticker for sticker in sticker_counts if any(char in target_count for char in sticker)]

    # 如果没有有用的贴纸，直接返回 -1
    if not useful_stickers:
        return -1

    # 定义记忆化搜索函数
    @lru_cache(None)
    def dp(mask):
        if mask == 0:
            return 0

        min_stickers_needed = float('inf')
        for sticker in useful_stickers:
            new_mask = mask
            for char, count in sticker.items():
                if char in target_count:
                    needed = (mask >> (ord(char) - ord('a'))) & 1
                    if needed:
                        new_mask &= ~(1 << (ord(char) - ord('a')))
                        if new_mask < mask:
                            break

            if new_mask < mask:
                min_stickers_needed = min(min_stickers_needed, 1 + dp(new_mask))

        return min_stickers_needed

    initial_mask = sum(1 << (ord(char) - ord('a')) for char in target)
    result = dp(initial_mask)

    return result if result != float('inf') else -1


Solution = create_solution(min_stickers)