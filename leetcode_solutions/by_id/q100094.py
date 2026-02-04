# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100094
标题: Coin Bonus
难度: hard
链接: https://leetcode.cn/problems/coin-bonus/
题目类型: 树状数组、线段树、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 05. 发 LeetCoin - 力扣决定给一个刷题团队发LeetCoin作为奖励。同时，为了监控给大家发了多少LeetCoin，力扣有时候也会进行查询。 该刷题团队的管理模式可以用一棵树表示： 1. 团队只有一个负责人，编号为1。除了该负责人外，每个人有且仅有一个领导（负责人没有领导）； 2. 不存在循环管理的情况，如A管理B，B管理C，C管理A。 力扣想进行的操作有以下三种： 1. 给团队的一个成员（也可以是负责人）发一定数量的LeetCoin； 2. 给团队的一个成员（也可以是负责人），以及他/她管理的所有人（即他/她的下属、他/她下属的下属，……），发一定数量的LeetCoin； 3. 查询某一个成员（也可以是负责人），以及他/她管理的所有人被发到的LeetCoin之和。 输入： 1. N表示团队成员的个数（编号为1～N，负责人为1）； 2. leadership是大小为(N - 1) * 2的二维数组，其中每个元素[a, b]代表b是a的下属； 3. operations是一个长度为Q的二维数组，代表以时间排序的操作，格式如下： 1. operations[i][0] = 1: 代表第一种操作，operations[i][1]代表成员的编号，operations[i][2]代表LeetCoin的数量； 2. operations[i][0] = 2: 代表第二种操作，operations[i][1]代表成员的编号，operations[i][2]代表LeetCoin的数量； 3. operations[i][0] = 3: 代表第三种操作，operations[i][1]代表成员的编号； 输出： 返回一个数组，数组里是每次查询的返回值（发LeetCoin的操作不需要任何返回值）。由于发的LeetCoin很多，请把每次查询的结果模1e9+7 (1000000007)。 示例 1： 输入：N = 6, leadership = [[1, 2], [1, 6], [2, 3], [2, 5], [1, 4]], operations = [[1, 1, 500], [2, 2, 50], [3, 1], [2, 6, 15], [3, 1]] 输出：[650, 665] 解释：团队的管理关系见下图。 第一次查询时，每个成员得到的LeetCoin的数量分别为（按编号顺序）：500, 50, 50, 0, 50, 0; 第二次查询时，每个成员得到的LeetCoin的数量分别为（按编号顺序）：500, 50, 50, 0, 50, 15. [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/09/09/coin_example_1.jpg] 限制： 1. 1 <= N <= 50000 2. 1 <= Q <= 50000 3. operations[i][0] != 3 时，1 <= operations[i][2] <= 5000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用线段树来处理区间更新和查询操作。

算法步骤:
1. 构建树结构，并记录每个节点的子树大小。
2. 初始化线段树，用于处理区间更新和查询。
3. 对于每种操作：
   - 操作1：直接更新线段树中对应节点的值。
   - 操作2：更新线段树中对应节点及其子树的值。
   - 操作3：查询线段树中对应节点及其子树的值。

关键点:
- 使用线段树可以高效地处理区间更新和查询操作。
- 通过DFS遍历树，记录每个节点的子树大小，以便在线段树中进行区间更新。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O((N + Q) log N)，其中N是节点数，Q是操作数。每次更新和查询的时间复杂度为O(log N)。
空间复杂度: O(N)，存储树结构和线段树。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

MOD = 1000000007

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
    
    def update(self, index, value, node=1, start=0, end=None):
        if end is None:
            end = self.n - 1
        if start == end:
            self.tree[node] += value
            self.tree[node] %= MOD
            return
        mid = (start + end) // 2
        if index <= mid:
            self.update(index, value, 2 * node, start, mid)
        else:
            self.update(index, value, 2 * node + 1, mid + 1, end)
        self.tree[node] = (self.tree[2 * node] + self.tree[2 * node + 1]) % MOD
    
    def query(self, left, right, node=1, start=0, end=None):
        if end is None:
            end = self.n - 1
        if left > end or right < start:
            return 0
        if left <= start and right >= end:
            return self.tree[node]
        mid = (start + end) // 2
        return (self.query(left, right, 2 * node, start, mid) + 
                self.query(left, right, 2 * node + 1, mid + 1, end)) % MOD

def dfs(node, parent, tree, subtree_size, depth):
    subtree_size[node] = 1
    for child in tree[node]:
        if child != parent:
            subtree_size[node] += dfs(child, node, tree, subtree_size, depth + 1)
    return subtree_size[node]

def solution_function_name(N: int, leadership: List[List[int]], operations: List[List[int]]) -> List[int]:
    # 构建树结构
    tree = [[] for _ in range(N)]
    for a, b in leadership:
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)
    
    # 记录每个节点的子树大小
    subtree_size = [0] * N
    dfs(0, -1, tree, subtree_size, 0)
    
    # 初始化线段树
    segment_tree = SegmentTree(N)
    
    # 处理操作
    results = []
    for op in operations:
        if op[0] == 1:
            # 更新单个节点
            segment_tree.update(op[1] - 1, op[2])
        elif op[0] == 2:
            # 更新节点及其子树
            segment_tree.update(op[1] - 1, op[2] * subtree_size[op[1] - 1])
        elif op[0] == 3:
            # 查询节点及其子树
            results.append(segment_tree.query(op[1] - 1, op[1] - 1))
    
    return results

Solution = create_solution(solution_function_name)