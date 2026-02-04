# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000484
标题: Hello LeetCode!
难度: hard
链接: https://leetcode.cn/problems/rMeRt2/
题目类型: 位运算、数组、字符串、动态规划、状态压缩
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 69. Hello LeetCode! - 力扣嘉年华同样准备了纪念品展位，参观者只需要集齐 `helloleetcode` 的 `13` 张字母卡片即可获得力扣纪念章。 在展位上有一些由字母卡片拼成的单词，`words[i][j]` 表示第 `i` 个单词的第 `j` 个字母。 你可以从这些单词中取出一些卡片，但每次拿取卡片都需要消耗游戏代币，规则如下： - 从一个单词中取一个字母所需要的代币数量，为该字母左边和右边字母数量之积 - 可以从一个单词中多次取字母，每个字母仅可被取一次 > 例如：从 `example` 中取出字母 `a`，需要消耗代币 `2*4=8`，字母取出后单词变为 `exmple`； 再从中取出字母 `m`，需要消耗代币 `2*3=6`，字母取出后单词变为 `exple`； 请返回取得 `helloleetcode` 这些字母需要消耗代币的 **最少** 数量。如果无法取得，返回 `-1`。 **注意：** - 取出字母的顺序没有要求 - 取出的所有字母恰好可以拼成 `helloleetcode` **示例 1：** >输入：`words = ["hold","engineer","cost","level"]` > >输出：`5` > >解释：最优方法为： >从 `hold` 依次取出 `h`、`o`、`l`、`d`， 代价均为 `0` >从 `engineer` 依次取出第 `1` 个 `e` 与最后一个 `e`， 代价为 `0` 和 `5*1=5` >从 `cost` 取出 `c`、`o`、`t`， 代价均为 `0` >从 `level` 依次取出 `l`、`l`、`e`、`e`， 代价均为 `0` >所有字母恰好可以拼成 `helloleetcode`，因此最小的代价为 `5` **示例 2：** >输入：`words = ["hello","leetcode"]` > >输出：`0` **提示：** + `n == words.length` + `m == words[i].length` + `1 <= n <= 24` + `1 <= m <= 8` + `words[i][j]` 仅为小写字母
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和状态压缩来解决这个问题。我们用一个二进制掩码来表示当前已经收集到的字母，并使用动态规划来记录在当前状态下所需的最小代价。

算法步骤:
1. 定义一个二维数组 dp，其中 dp[mask] 表示当前已经收集到的字母状态为 mask 时的最小代价。
2. 初始化 dp 数组，dp[0] = 0，其他值设为无穷大。
3. 遍历每个单词，对于每个单词中的每个字母，计算其左边和右边字母的数量。
4. 更新 dp 数组，考虑从当前单词中取出字母后的状态转移。
5. 最终返回 dp[(1 << 13) - 1]，即收集完所有字母的最小代价。如果该值仍为无穷大，则返回 -1。

关键点:
- 使用二进制掩码来表示当前已经收集到的字母状态。
- 动态规划的状态转移方程要考虑从当前单词中取出字母后的代价。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m * 2^13)，其中 n 是单词的数量，m 是单词的最大长度，2^13 是状态数。
空间复杂度: O(2^13)，用于存储 dp 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(words: List[str]) -> int:
    """
    函数式接口 - 实现
    """
    target = "helloleetcode"
    char_count = [0] * 26
    for c in target:
        char_count[ord(c) - ord('a')] += 1

    n = len(words)
    m = max(len(word) for word in words)
    dp = [float('inf')] * (1 << 13)
    dp[0] = 0

    def get_mask(state):
        mask = 0
        for i in range(26):
            if state[i] > 0:
                mask |= (1 << i)
        return mask

    for i in range(n):
        word = words[i]
        for j in range(len(word)):
            left = j
            right = len(word) - j - 1
            cost = left * right
            for mask in range((1 << 13) - 1, -1, -1):
                new_state = char_count[:]
                for k in range(26):
                    if (mask >> k) & 1:
                        new_state[k] -= 1
                new_state[ord(word[j]) - ord('a')] += 1
                new_mask = get_mask(new_state)
                if new_mask < (1 << 13):
                    dp[new_mask] = min(dp[new_mask], dp[mask] + cost)

    result = dp[(1 << 13) - 1]
    return result if result != float('inf') else -1


Solution = create_solution(solution_function_name)