# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2319
标题: Longest Substring of One Repeating Character
难度: hard
链接: https://leetcode.cn/problems/longest-substring-of-one-repeating-character/
题目类型: 线段树、数组、字符串、有序集合
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2213. 由单个字符重复的最长子字符串 - 给你一个下标从 0 开始的字符串 s 。另给你一个下标从 0 开始、长度为 k 的字符串 queryCharacters ，一个下标从 0 开始、长度也是 k 的整数 下标 数组 queryIndices ，这两个都用来描述 k 个查询。 第 i 个查询会将 s 中位于下标 queryIndices[i] 的字符更新为 queryCharacters[i] 。 返回一个长度为 k 的数组 lengths ，其中 lengths[i] 是在执行第 i 个查询 之后 s 中仅由 单个字符重复 组成的 最长子字符串 的 长度 。 示例 1： 输入：s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3] 输出：[3,3,4] 解释： - 第 1 次查询更新后 s = "bbbacc" 。由单个字符重复组成的最长子字符串是 "bbb" ，长度为 3 。 - 第 2 次查询更新后 s = "bbbccc" 。由单个字符重复组成的最长子字符串是 "bbb" 或 "ccc"，长度为 3 。 - 第 3 次查询更新后 s = "bbbbcc" 。由单个字符重复组成的最长子字符串是 "bbbb" ，长度为 4 。 因此，返回 [3,3,4] 。 示例 2： 输入：s = "abyzz", queryCharacters = "aa", queryIndices = [2,1] 输出：[2,3] 解释： - 第 1 次查询更新后 s = "abazz" 。由单个字符重复组成的最长子字符串是 "zz" ，长度为 2 。 - 第 2 次查询更新后 s = "aaazz" 。由单个字符重复组成的最长子字符串是 "aaa" ，长度为 3 。 因此，返回 [2,3] 。 提示： * 1 <= s.length <= 105 * s 由小写英文字母组成 * k == queryCharacters.length == queryIndices.length * 1 <= k <= 105 * queryCharacters 由小写英文字母组成 * 0 <= queryIndices[i] < s.length
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用线段树来维护每个区间的最长连续相同字符子串的长度。

算法步骤:
1. 初始化线段树，构建初始字符串 s 的线段树。
2. 对于每个查询，更新线段树中对应位置的字符，并重新计算受影响区间的最长连续相同字符子串的长度。
3. 查询线段树以获取当前最长连续相同字符子串的长度。

关键点:
- 线段树的节点存储该区间内的最长连续相同字符子串的长度。
- 更新操作时，需要递归地更新受影响的区间。
- 查询操作时，需要合并左右子树的结果。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(k log n)，其中 k 是查询的数量，n 是字符串 s 的长度。每次更新和查询的时间复杂度都是 O(log n)。
空间复杂度: O(n)，线段树的空间复杂度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

class SegmentTree:
    def __init__(self, s: str):
        self.n = len(s)
        self.tree = [0] * (4 * self.n)
        self.build_tree(s, 0, 0, self.n - 1)

    def build_tree(self, s: str, node: int, start: int, end: int):
        if start == end:
            self.tree[node] = 1
            return
        mid = (start + end) // 2
        self.build_tree(s, 2 * node + 1, start, mid)
        self.build_tree(s, 2 * node + 2, mid + 1, end)
        self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2], s, mid, mid + 1)

    def update(self, s: str, node: int, start: int, end: int, idx: int, val: str):
        if start == end:
            s = s[:idx] + val + s[idx + 1:]
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(s, 2 * node + 1, start, mid, idx, val)
        else:
            self.update(s, 2 * node + 2, mid + 1, end, idx, val)
        self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2], s, mid, mid + 1)

    def merge(self, left: int, right: int, s: str, mid: int, next_mid: int) -> int:
        if s[mid] == s[next_mid]:
            return left + right
        return max(left, right)

def solution_function_name(s: str, query_characters: str, query_indices: List[int]) -> List[int]:
    """
    函数式接口 - 使用线段树来解决最长连续相同字符子串的问题
    """
    n = len(s)
    segment_tree = SegmentTree(s)
    result = []
    for i in range(len(query_characters)):
        char = query_characters[i]
        idx = query_indices[i]
        segment_tree.update(s, 0, 0, n - 1, idx, char)
        result.append(segment_tree.tree[0])
    return result

Solution = create_solution(solution_function_name)