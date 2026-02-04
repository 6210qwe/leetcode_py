# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2051
标题: Longest Common Subpath
难度: hard
链接: https://leetcode.cn/problems/longest-common-subpath/
题目类型: 数组、二分查找、后缀数组、哈希函数、滚动哈希
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1923. 最长公共子路径 - 一个国家由 n 个编号为 0 到 n - 1 的城市组成。在这个国家里，每两个 城市之间都有一条道路连接。 总共有 m 个编号为 0 到 m - 1 的朋友想在这个国家旅游。他们每一个人的路径都会包含一些城市。每条路径都由一个整数数组表示，每个整数数组表示一个朋友按顺序访问过的城市序列。同一个城市在一条路径中可能 重复 出现，但同一个城市在一条路径中不会连续出现。 给你一个整数 n 和二维数组 paths ，其中 paths[i] 是一个整数数组，表示第 i 个朋友走过的路径，请你返回 每一个 朋友都走过的 最长公共子路径 的长度，如果不存在公共子路径，请你返回 0 。 一个 子路径 指的是一条路径中连续的城市序列。 示例 1： 输入：n = 5, paths = [[0,1,2,3,4], [2,3,4], [4,0,1,2,3]] 输出：2 解释：最长公共子路径为 [2,3] 。 示例 2： 输入：n = 3, paths = [[0],[1],[2]] 输出：0 解释：三条路径没有公共子路径。 示例 3： 输入：n = 5, paths = [[0,1,2,3,4], [4,3,2,1,0]] 输出：1 解释：最长公共子路径为 [0]，[1]，[2]，[3] 和 [4] 。它们长度都为 1 。 提示： * 1 <= n <= 105 * m == paths.length * 2 <= m <= 105 * sum(paths[i].length) <= 105 * 0 <= paths[i][j] < n * paths[i] 中同一个城市不会连续重复出现。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找和滚动哈希来找到最长的公共子路径。

算法步骤:
1. 初始化二分查找的左右边界 `left` 和 `right`，分别为 1 和最短路径的长度。
2. 在二分查找的过程中，使用滚动哈希来检查当前长度 `mid` 是否存在所有路径中。
3. 如果存在，则更新左边界 `left` 为 `mid + 1`，否则更新右边界 `right` 为 `mid - 1`。
4. 最终返回 `right` 作为最长公共子路径的长度。

关键点:
- 使用滚动哈希来高效地计算子路径的哈希值，并进行比较。
- 通过二分查找来优化查找过程，减少不必要的计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * log(min_path_length) * max_path_length)，其中 m 是路径的数量，min_path_length 是最短路径的长度，max_path_length 是最长路径的长度。
空间复杂度: O(m * max_path_length)，用于存储路径的哈希值。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def solution_function_name(n: int, paths: List[List[int]]) -> int:
    def get_hash(path: List[int], length: int) -> set:
        base = 1000000007
        mod = 10**9 + 7
        hash_value = 0
        power = 1
        hashes = set()

        for i in range(length):
            hash_value = (hash_value * base + path[i]) % mod
            power = (power * base) % mod

        hashes.add(hash_value)

        for i in range(length, len(path)):
            hash_value = (hash_value * base - path[i - length] * power + path[i]) % mod
            hashes.add(hash_value)

        return hashes

    def is_common_subpath(length: int) -> bool:
        hashes = get_hash(paths[0], length)
        for path in paths[1:]:
            if not hashes & get_hash(path, length):
                return False
        return True

    left, right = 1, min(len(path) for path in paths)
    while left <= right:
        mid = (left + right) // 2
        if is_common_subpath(mid):
            left = mid + 1
        else:
            right = mid - 1

    return right

Solution = create_solution(solution_function_name)