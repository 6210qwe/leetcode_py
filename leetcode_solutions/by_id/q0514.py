# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 514
标题: Freedom Trail
难度: hard
链接: https://leetcode.cn/problems/freedom-trail/
题目类型: 深度优先搜索、广度优先搜索、字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
514. 自由之路 - 电子游戏“辐射4”中，任务 “通向自由” 要求玩家到达名为 “Freedom Trail Ring” 的金属表盘，并使用表盘拼写特定关键词才能开门。 给定一个字符串 ring ，表示刻在外环上的编码；给定另一个字符串 key ，表示需要拼写的关键词。您需要算出能够拼写关键词中所有字符的最少步数。 最初，ring 的第一个字符与 12:00 方向对齐。您需要顺时针或逆时针旋转 ring 以使 key 的一个字符在 12:00 方向对齐，然后按下中心按钮，以此逐个拼写完 key 中的所有字符。 旋转 ring 拼出 key 字符 key[i] 的阶段中： 1. 您可以将 ring 顺时针或逆时针旋转 一个位置 ，计为1步。旋转的最终目的是将字符串 ring 的一个字符与 12:00 方向对齐，并且这个字符必须等于字符 key[i] 。 2. 如果字符 key[i] 已经对齐到12:00方向，您需要按下中心按钮进行拼写，这也将算作 1 步。按完之后，您可以开始拼写 key 的下一个字符（下一阶段）, 直至完成所有拼写。 示例 1： [https://assets.leetcode.com/uploads/2018/10/22/ring.jpg] 输入: ring = "godding", key = "gd" 输出: 4 解释: 对于 key 的第一个字符 'g'，已经在正确的位置, 我们只需要1步来拼写这个字符。 对于 key 的第二个字符 'd'，我们需要逆时针旋转 ring "godding" 2步使它变成 "ddinggo"。 当然, 我们还需要1步进行拼写。 因此最终的输出是 4。 示例 2: 输入: ring = "godding", key = "godding" 输出: 13 提示： * 1 <= ring.length, key.length <= 100 * ring 和 key 只包含小写英文字母 * 保证 字符串 key 一定可以由字符串 ring 旋转拼出
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和记忆化搜索来解决这个问题。我们可以通过预处理记录每个字符在 ring 中出现的位置，然后使用递归加记忆化搜索来计算从当前字符到下一个字符的最小步数。

算法步骤:
1. 预处理 ring，记录每个字符在 ring 中出现的位置。
2. 定义一个递归函数 `dp(i, j)` 表示从 key 的第 i 个字符开始，ring 的第 j 个字符对齐时的最小步数。
3. 在递归函数中，遍历 key 的下一个字符在 ring 中的所有位置，计算从当前字符到下一个字符的最小步数。
4. 使用记忆化搜索来避免重复计算。

关键点:
- 预处理 ring 中每个字符的位置。
- 使用递归加记忆化搜索来计算最小步数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m * k)，其中 n 是 key 的长度，m 是 ring 的长度，k 是 ring 中每个字符出现的最大次数。
空间复杂度: O(n * m)，记忆化搜索的缓存空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
from functools import lru_cache

def find_rotate_steps(ring: str, key: str) -> int:
    """
    计算拼写关键词所需的最少步数。
    """
    # 预处理 ring，记录每个字符在 ring 中出现的位置
    char_positions = {}
    for i, char in enumerate(ring):
        if char not in char_positions:
            char_positions[char] = []
        char_positions[char].append(i)

    @lru_cache(None)
    def dp(i: int, j: int) -> int:
        if i == len(key):
            return 0
        min_steps = float('inf')
        for next_pos in char_positions[key[i]]:
            # 计算从 j 到 next_pos 的最小步数
            steps = min(abs(next_pos - j), len(ring) - abs(next_pos - j))
            # 递归计算从下一个字符开始的最小步数
            min_steps = min(min_steps, steps + 1 + dp(i + 1, next_pos))
        return min_steps

    return dp(0, 0)

Solution = create_solution(find_rotate_steps)