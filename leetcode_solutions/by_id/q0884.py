# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 884
标题: K-Similar Strings
难度: hard
链接: https://leetcode.cn/problems/k-similar-strings/
题目类型: 广度优先搜索、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
854. 相似度为 K 的字符串 - 对于某些非负整数 k ，如果交换 s1 中两个字母的位置恰好 k 次，能够使结果字符串等于 s2 ，则认为字符串 s1 和 s2 的 相似度为 k 。 给你两个字母异位词 s1 和 s2 ，返回 s1 和 s2 的相似度 k 的最小值。 示例 1： 输入：s1 = "ab", s2 = "ba" 输出：1 示例 2： 输入：s1 = "abc", s2 = "bca" 输出：2 提示： * 1 <= s1.length <= 20 * s2.length == s1.length * s1 和 s2 只包含集合 {'a', 'b', 'c', 'd', 'e', 'f'} 中的小写字母 * s2 是 s1 的一个字母异位词
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）来找到从 s1 到 s2 的最短转换路径。

算法步骤:
1. 初始化队列，将 s1 加入队列，并记录已访问的字符串。
2. 开始 BFS：
   - 从队列中取出一个字符串 cur。
   - 如果 cur 等于 s2，返回当前步数。
   - 找到第一个不匹配的字符位置 i。
   - 尝试交换 cur[i] 与后续所有可能的字符，生成新的字符串 new_str。
   - 如果 new_str 未被访问过，将其加入队列并标记为已访问。
3. 重复上述过程直到找到 s2 或队列为空。

关键点:
- 使用 BFS 保证找到的路径是最短的。
- 通过剪枝减少不必要的交换操作。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n!)，其中 n 是字符串的长度。在最坏情况下，每个字符都需要尝试交换。
空间复杂度: O(n!)，队列和已访问集合在最坏情况下需要存储 n! 个字符串。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def kSimilarity(s1: str, s2: str) -> int:
    """
    函数式接口 - 返回 s1 和 s2 的最小相似度 k
    """
    if s1 == s2:
        return 0

    def get_next_strings(s: str, target: str):
        i = 0
        while s[i] == target[i]:
            i += 1
        for j in range(i + 1, len(s)):
            if s[j] == target[i] and s[j] != target[j]:
                yield s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]

    from collections import deque
    queue = deque([(s1, 0)])
    visited = {s1}

    while queue:
        cur, steps = queue.popleft()
        if cur == s2:
            return steps
        for next_str in get_next_strings(cur, s2):
            if next_str not in visited:
                visited.add(next_str)
                queue.append((next_str, steps + 1))


Solution = create_solution(kSimilarity)