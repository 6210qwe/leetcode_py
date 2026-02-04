# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1296
标题: Kth Ancestor of a Tree Node
难度: hard
链接: https://leetcode.cn/problems/kth-ancestor-of-a-tree-node/
题目类型: 位运算、树、深度优先搜索、广度优先搜索、设计、二分查找、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1483. 树节点的第 K 个祖先 - 给你一棵树，树上有 n 个节点，按从 0 到 n-1 编号。树以父节点数组的形式给出，其中 parent[i] 是节点 i 的父节点。树的根节点是编号为 0 的节点。 树节点的第 k 个祖先节点是从该节点到根节点路径上的第 k 个节点。 实现 TreeAncestor 类： * TreeAncestor（int n， int[] parent） 对树和父数组中的节点数初始化对象。 * getKthAncestor(int node, int k) 返回节点 node 的第 k 个祖先节点。如果不存在这样的祖先节点，返回 -1 。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/06/14/1528_ex1.png] 输入： ["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"] [[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]] 输出： [null,1,0,-1] 解释： TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]); treeAncestor.getKthAncestor(3, 1); // 返回 1 ，它是 3 的父节点 treeAncestor.getKthAncestor(5, 2); // 返回 0 ，它是 5 的祖父节点 treeAncestor.getKthAncestor(6, 3); // 返回 -1 因为不存在满足要求的祖先节点 提示： * 1 <= k <= n <= 5 * 104 * parent[0] == -1 表示编号为 0 的节点是根节点。 * 对于所有的 0 < i < n ，0 <= parent[i] < n 总成立 * 0 <= node < n * 至多查询 5 * 104 次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用倍增法 (Binary Lifting) 来预处理每个节点的 2^j 级祖先，从而在 O(log k) 时间内找到第 k 个祖先。

算法步骤:
1. 初始化一个二维数组 dp，其中 dp[i][j] 表示节点 i 的 2^j 级祖先。
2. 预处理 dp 数组，对于每个节点 i 和 j，计算 dp[i][j]。
3. 在查询时，通过二进制分解 k，使用 dp 数组快速找到第 k 个祖先。

关键点:
- 使用倍增法预处理祖先信息，使得每次查询的时间复杂度为 O(log k)。
- 通过二进制分解 k，可以高效地找到第 k 个祖先。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n) - 预处理的时间复杂度为 O(n log n)，每次查询的时间复杂度为 O(log k)。
空间复杂度: O(n log n) - 存储 dp 数组的空间复杂度为 O(n log n)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.log = 17  # 2^17 > 5*10^4
        self.dp = [[-1] * self.log for _ in range(n)]
        
        # 初始化每个节点的 2^0 级祖先
        for i in range(n):
            self.dp[i][0] = parent[i]
        
        # 预处理每个节点的 2^j 级祖先
        for j in range(1, self.log):
            for i in range(n):
                if self.dp[i][j-1] != -1:
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]

    def getKthAncestor(self, node: int, k: int) -> int:
        # 通过二进制分解 k，找到第 k 个祖先
        while k > 0 and node != -1:
            j = 0
            while (1 << (j + 1)) <= k:
                j += 1
            node = self.dp[node][j]
            k -= (1 << j)
        return node


# 测试用例
if __name__ == "__main__":
    obj = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
    print(obj.getKthAncestor(3, 1))  # 输出: 1
    print(obj.getKthAncestor(5, 2))  # 输出: 0
    print(obj.getKthAncestor(6, 3))  # 输出: -1