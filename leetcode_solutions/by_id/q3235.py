# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3235
标题: Minimum Cost to Convert String I
难度: medium
链接: https://leetcode.cn/problems/minimum-cost-to-convert-string-i/
题目类型: 图、数组、字符串、最短路
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2976. 转换字符串的最小成本 I - 给你两个下标从 0 开始的字符串 source 和 target ，它们的长度均为 n 并且由 小写 英文字母组成。 另给你两个下标从 0 开始的字符数组 original 和 changed ，以及一个整数数组 cost ，其中 cost[i] 代表将字符 original[i] 更改为字符 changed[i] 的成本。 你从字符串 source 开始。在一次操作中，如果 存在 任意 下标 j 满足 cost[j] == z 、original[j] == x 以及 changed[j] == y 。你就可以选择字符串中的一个字符 x 并以 z 的成本将其更改为字符 y 。 返回将字符串 source 转换为字符串 target 所需的 最小 成本。如果不可能完成转换，则返回 -1 。 注意，可能存在下标 i 、j 使得 original[j] == original[i] 且 changed[j] == changed[i] 。 示例 1： 输入：source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20] 输出：28 解释：将字符串 "abcd" 转换为字符串 "acbe" ： - 更改下标 1 处的值 'b' 为 'c' ，成本为 5 。 - 更改下标 2 处的值 'c' 为 'e' ，成本为 1 。 - 更改下标 2 处的值 'e' 为 'b' ，成本为 2 。 - 更改下标 3 处的值 'd' 为 'e' ，成本为 20 。 产生的总成本是 5 + 1 + 2 + 20 = 28 。 可以证明这是可能的最小成本。 示例 2： 输入：source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2] 输出：12 解释：要将字符 'a' 更改为 'b'： - 将字符 'a' 更改为 'c'，成本为 1 - 将字符 'c' 更改为 'b'，成本为 2 产生的总成本是 1 + 2 = 3。 将所有 'a' 更改为 'b'，产生的总成本是 3 * 4 = 12 。 示例 3： 输入：source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000] 输出：-1 解释：无法将 source 字符串转换为 target 字符串，因为下标 3 处的值无法从 'd' 更改为 'e' 。 提示： * 1 <= source.length == target.length <= 105 * source、target 均由小写英文字母组成 * 1 <= cost.length== original.length == changed.length <= 2000 * original[i]、changed[i] 是小写英文字母 * 1 <= cost[i] <= 106 * original[i] != changed[i]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Floyd-Warshall 算法计算所有字符之间的最短路径，然后根据这些路径计算转换成本。

算法步骤:
1. 初始化一个 26x26 的距离矩阵，表示每个字符到其他字符的转换成本。
2. 使用给定的 `original` 和 `changed` 更新距离矩阵。
3. 使用 Floyd-Warshall 算法计算所有字符之间的最短路径。
4. 遍历 `source` 和 `target`，计算总的转换成本。
5. 如果某个字符无法转换，则返回 -1。

关键点:
- 使用 Floyd-Warshall 算法计算所有字符之间的最短路径。
- 通过距离矩阵快速查找转换成本。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(26^3 + n) = O(1) + O(n)，其中 n 是字符串的长度，26 是字母表的大小。
空间复杂度: O(26^2) = O(1)，用于存储距离矩阵。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def minimum_cost_to_convert_string(source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
    # 初始化距离矩阵
    dist = [[float('inf')] * 26 for _ in range(26)]
    for i in range(26):
        dist[i][i] = 0

    # 更新距离矩阵
    for orig, chng, c in zip(original, changed, cost):
        u, v = ord(orig) - ord('a'), ord(chng) - ord('a')
        dist[u][v] = min(dist[u][v], c)

    # Floyd-Warshall 算法计算所有字符之间的最短路径
    for k in range(26):
        for i in range(26):
            for j in range(26):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # 计算总的转换成本
    total_cost = 0
    for s, t in zip(source, target):
        u, v = ord(s) - ord('a'), ord(t) - ord('a')
        if dist[u][v] == float('inf'):
            return -1
        total_cost += dist[u][v]

    return total_cost

Solution = create_solution(minimum_cost_to_convert_string)