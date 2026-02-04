# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1160
标题: Letter Tile Possibilities
难度: medium
链接: https://leetcode.cn/problems/letter-tile-possibilities/
题目类型: 哈希表、字符串、回溯、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1079. 活字印刷 - 你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目。 注意：本题中，每个活字字模只能使用一次。 示例 1： 输入："AAB" 输出：8 解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。 示例 2： 输入："AAABBC" 输出：188 示例 3： 输入："V" 输出：1 提示： * 1 <= tiles.length <= 7 * tiles 由大写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用回溯法生成所有可能的排列，并通过哈希集合去重。

算法步骤:
1. 将输入字符串转换为字符列表。
2. 使用回溯法生成所有可能的排列。
3. 使用哈希集合去重，记录所有不同的排列。
4. 返回哈希集合的大小，即不同排列的数量。

关键点:
- 使用回溯法生成所有可能的排列。
- 使用哈希集合去重，确保每个排列只被计算一次。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n!)
  - n 是输入字符串的长度，最坏情况下需要生成所有可能的排列。
空间复杂度: O(n!)
  - 用于存储所有可能的排列。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def num_tile_possibilities(tiles: str) -> int:
    """
    函数式接口 - 计算可以印出的不同字母序列的数量
    """
    def backtrack(path, used):
        if path:
            seen.add(''.join(path))
        for i in range(len(tiles)):
            if not used[i]:
                used[i] = True
                path.append(tiles[i])
                backtrack(path, used)
                path.pop()
                used[i] = False

    tiles = list(tiles)
    seen = set()
    used = [False] * len(tiles)
    backtrack([], used)
    return len(seen)


Solution = create_solution(num_tile_possibilities)