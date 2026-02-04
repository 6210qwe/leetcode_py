# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1875
标题: Tree of Coprimes
难度: hard
链接: https://leetcode.cn/problems/tree-of-coprimes/
题目类型: 树、深度优先搜索、数组、数学、数论
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1766. 互质树 - 给你一个 n 个节点的树（也就是一个无环连通无向图），节点编号从 0 到 n - 1 ，且恰好有 n - 1 条边，每个节点有一个值。树的 根节点 为 0 号点。 给你一个整数数组 nums 和一个二维数组 edges 来表示这棵树。nums[i] 表示第 i 个点的值，edges[j] = [uj, vj] 表示节点 uj 和节点 vj 在树中有一条边。 当 gcd(x, y) == 1 ，我们称两个数 x 和 y 是 互质的 ，其中 gcd(x, y) 是 x 和 y 的 最大公约数 。 从节点 i 到 根 最短路径上的点都是节点 i 的祖先节点。一个节点 不是 它自己的祖先节点。 请你返回一个大小为 n 的数组 ans ，其中 ans[i]是离节点 i 最近的祖先节点且满足 nums[i] 和 nums[ans[i]] 是 互质的 ，如果不存在这样的祖先节点，ans[i] 为 -1 。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/02/20/untitled-diagram.png] 输入：nums = [2,3,3,2], edges = [[0,1],[1,2],[1,3]] 输出：[-1,0,0,1] 解释：上图中，每个节点的值在括号中表示。 - 节点 0 没有互质祖先。 - 节点 1 只有一个祖先节点 0 。它们的值是互质的（gcd(2,3) == 1）。 - 节点 2 有两个祖先节点，分别是节点 1 和节点 0 。节点 1 的值与它的值不是互质的（gcd(3,3) == 3）但节点 0 的值是互质的(gcd(2,3) == 1)，所以节点 0 是最近的符合要求的祖先节点。 - 节点 3 有两个祖先节点，分别是节点 1 和节点 0 。它与节点 1 互质（gcd(3,2) == 1），所以节点 1 是离它最近的符合要求的祖先节点。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/02/20/untitled-diagram1.png] 输入：nums = [5,6,10,2,3,6,15], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]] 输出：[-1,0,-1,0,0,0,-1] 提示： * nums.length == n * 1 <= nums[i] <= 50 * 1 <= n <= 105 * edges.length == n - 1 * edges[j].length == 2 * 0 <= uj, vj < n * uj != vj
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来遍历树，并维护一个字典来记录每个值的最近祖先节点。

算法步骤:
1. 构建树的邻接表表示。
2. 初始化结果数组 `ans` 和一个字典 `ancestors` 来记录每个值的最近祖先节点。
3. 使用 DFS 遍历树，对于每个节点：
   - 更新 `ancestors` 字典，移除当前节点的值。
   - 找到当前节点的最近互质祖先节点。
   - 更新 `ancestors` 字典，添加当前节点的值。
4. 返回结果数组 `ans`。

关键点:
- 使用字典 `ancestors` 来记录每个值的最近祖先节点，以 O(1) 时间复杂度找到最近互质祖先。
- 使用 DFS 遍历树，确保每个节点的祖先节点都被正确处理。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * log(max(nums)))，其中 n 是节点数，log(max(nums)) 是计算最大公约数的时间复杂度。
空间复杂度: O(n + max(nums))，其中 n 是节点数，max(nums) 是节点值的最大值。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import math

def getCoprimes(nums: List[int], edges: List[List[int]]) -> List[int]:
    def gcd(a, b):
        return math.gcd(a, b)

    def dfs(node, parent, depth):
        if node in ancestors[nums[node]]:
            result[node] = ancestors[nums[node]][-1]
        for value in ancestors:
            if gcd(value, nums[node]) == 1 and ancestors[value]:
                result[node] = max(result[node], ancestors[value][-1])

        ancestors[nums[node]].append((node, depth))
        for neighbor in graph[node]:
            if neighbor != parent:
                dfs(neighbor, node, depth + 1)
        ancestors[nums[node]].pop()

    n = len(nums)
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    result = [-1] * n
    ancestors = {value: [] for value in range(1, 51)}
    dfs(0, -1, 0)
    return result

Solution = create_solution(getCoprimes)