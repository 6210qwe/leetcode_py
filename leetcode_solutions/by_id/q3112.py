# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3112
标题: Count Valid Paths in a Tree
难度: hard
链接: https://leetcode.cn/problems/count-valid-paths-in-a-tree/
题目类型: 树、深度优先搜索、数学、动态规划、数论
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2867. 统计树中的合法路径数目 - 给你一棵 n 个节点的无向树，节点编号为 1 到 n 。给你一个整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ui, vi] 表示节点 ui 和 vi 在树中有一条边。 请你返回树中的 合法路径数目 。 如果在节点 a 到节点 b 之间 恰好有一个 节点的编号是质数，那么我们称路径 (a, b) 是 合法的 。 注意： * 路径 (a, b) 指的是一条从节点 a 开始到节点 b 结束的一个节点序列，序列中的节点 互不相同 ，且相邻节点之间在树上有一条边。 * 路径 (a, b) 和路径 (b, a) 视为 同一条 路径，且只计入答案 一次 。 示例 1： [https://assets.leetcode.com/uploads/2023/08/27/example1.png] 输入：n = 5, edges = [[1,2],[1,3],[2,4],[2,5]] 输出：4 解释：恰好有一个质数编号的节点路径有： - (1, 2) 因为路径 1 到 2 只包含一个质数 2 。 - (1, 3) 因为路径 1 到 3 只包含一个质数 3 。 - (1, 4) 因为路径 1 到 4 只包含一个质数 2 。 - (2, 4) 因为路径 2 到 4 只包含一个质数 2 。 只有 4 条合法路径。 示例 2： [https://assets.leetcode.com/uploads/2023/08/27/example2.png] 输入：n = 6, edges = [[1,2],[1,3],[2,4],[3,5],[3,6]] 输出：6 解释：恰好有一个质数编号的节点路径有： - (1, 2) 因为路径 1 到 2 只包含一个质数 2 。 - (1, 3) 因为路径 1 到 3 只包含一个质数 3 。 - (1, 4) 因为路径 1 到 4 只包含一个质数 2 。 - (1, 6) 因为路径 1 到 6 只包含一个质数 3 。 - (2, 4) 因为路径 2 到 4 只包含一个质数 2 。 - (3, 6) 因为路径 3 到 6 只包含一个质数 3 。 只有 6 条合法路径。 提示： * 1 <= n <= 105 * edges.length == n - 1 * edges[i].length == 2 * 1 <= ui, vi <= n * 输入保证 edges 形成一棵合法的树。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
- 使用深度优先搜索 (DFS) 来遍历树，并记录每个节点的子树大小。
- 使用埃拉托色尼筛法生成所有质数。
- 在 DFS 过程中，计算每个质数节点的贡献。

算法步骤:
1. 生成所有质数。
2. 构建树的邻接表表示。
3. 使用 DFS 计算每个节点的子树大小。
4. 在 DFS 过程中，计算每个质数节点的贡献。

关键点:
- 使用埃拉托色尼筛法高效生成质数。
- 在 DFS 过程中，通过子树大小和质数节点来计算路径数目。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log log n + n) - 生成质数的时间复杂度为 O(n log log n)，DFS 的时间复杂度为 O(n)。
空间复杂度: O(n) - 存储树的邻接表和子树大小。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import math

def count_valid_paths(n: int, edges: List[List[int]]) -> int:
    def sieve_of_eratosthenes(limit):
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(math.sqrt(limit)) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False
        return [i for i in range(limit + 1) if is_prime[i]]

    def dfs(node, parent):
        size = 1
        nonlocal valid_paths
        prime_count = 0
        composite_count = 0

        for neighbor in tree[node]:
            if neighbor != parent:
                sub_size, sub_prime, sub_composite = dfs(neighbor, node)
                size += sub_size
                if is_prime[neighbor]:
                    prime_count += sub_size
                    valid_paths += sub_size * composite_count
                else:
                    composite_count += sub_size
                    valid_paths += sub_size * prime_count

        if is_prime[node]:
            valid_paths += composite_count
            return size, prime_count + 1, 0
        else:
            return size, prime_count, composite_count

    # 生成质数
    primes = sieve_of_eratosthenes(n)
    is_prime = [False] * (n + 1)
    for prime in primes:
        is_prime[prime] = True

    # 构建树的邻接表
    tree = [[] for _ in range(n + 1)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    valid_paths = 0
    dfs(1, -1)
    return valid_paths

Solution = create_solution(count_valid_paths)