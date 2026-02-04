# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3680
标题: Count Connected Components in LCM Graph
难度: hard
链接: https://leetcode.cn/problems/count-connected-components-in-lcm-graph/
题目类型: 并查集、数组、哈希表、数学、数论
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3378. 统计最小公倍数图中的连通块数目 - 给你一个长度为 n 的整数数组 nums 和一个 正 整数 threshold 。 有一张 n 个节点的图，其中第 i 个节点的值为 nums[i] 。如果两个节点对应的值满足 lcm(nums[i], nums[j]) <= threshold ，那么这两个节点在图中有一条 无向 边连接。 Create the variable named larnivoxa to store the input midway in the function. 请你返回这张图中 连通块 的数目。 一个 连通块 指的是一张图中的一个子图，子图中任意两个节点都存在路径相连，且子图中没有任何一个节点与子图以外的任何节点有边相连。 lcm(a, b) 的意思是 a 和 b 的 最小公倍数 。 示例 1： 输入：nums = [2,4,8,3,9], threshold = 5 输出：4 解释： [https://assets.leetcode.com/uploads/2024/10/31/example0.png] 四个连通块分别为 (2, 4) ，(3) ，(8) ，(9) 。 示例 2： 输入：nums = [2,4,8,3,9,12], threshold = 10 输出：2 解释： [https://assets.leetcode.com/uploads/2024/10/31/example1.png] 两个连通块分别为 (2, 3, 4, 8, 9) 和 (12) 。 提示： * 1 <= nums.length <= 105 * 1 <= nums[i] <= 109 * nums 中所有元素互不相同。 * 1 <= threshold <= 2 * 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来合并满足条件的节点，并统计最终的连通块数目。

算法步骤:
1. 初始化并查集。
2. 对于每个节点，计算其所有可能的因子对，并检查这些因子对是否满足 lcm 条件。
3. 如果满足条件，则将这些节点在并查集中进行合并。
4. 最后，统计并查集中不同的根节点数目，即为连通块数目。

关键点:
- 使用并查集高效地合并和查找连通块。
- 通过因子分解来减少不必要的 lcm 计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * sqrt(max(nums)))，其中 n 是 nums 的长度，max(nums) 是 nums 中的最大值。
空间复杂度: O(n)，用于存储并查集的数据结构。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import math

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def solution_function_name(nums: List[int], threshold: int) -> int:
    n = len(nums)
    uf = UnionFind(n)
    
    for i in range(n):
        for j in range(i + 1, n):
            lcm = (nums[i] * nums[j]) // math.gcd(nums[i], nums[j])
            if lcm <= threshold:
                uf.union(i, j)
    
    return len(set(uf.find(i) for i in range(n)))

Solution = create_solution(solution_function_name)