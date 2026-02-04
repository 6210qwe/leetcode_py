# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 989
标题: Largest Component Size by Common Factor
难度: hard
链接: https://leetcode.cn/problems/largest-component-size-by-common-factor/
题目类型: 并查集、数组、哈希表、数学、数论
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
952. 按公因数计算最大组件大小 - 给定一个由不同正整数的组成的非空数组 nums ，考虑下面的图： * 有 nums.length 个节点，按从 nums[0] 到 nums[nums.length - 1] 标记； * 只有当 nums[i] 和 nums[j] 共用一个大于 1 的公因数时，nums[i] 和 nums[j]之间才有一条边。 返回 图中最大连通组件的大小 。 示例 1： [https://assets.leetcode.com/uploads/2018/12/01/ex1.png] 输入：nums = [4,6,15,35] 输出：4 示例 2： [https://assets.leetcode.com/uploads/2018/12/01/ex2.png] 输入：nums = [20,50,9,63] 输出：2 示例 3： [https://assets.leetcode.com/uploads/2018/12/01/ex3.png] 输入：nums = [2,3,6,7,4,12,21,39] 输出：8 提示： * 1 <= nums.length <= 2 * 104 * 1 <= nums[i] <= 105 * nums 中所有值都 不同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来连接具有共同因子的数字，并找到最大的连通分量。

算法步骤:
1. 初始化并查集。
2. 对每个数字进行质因数分解，并将这些质因数连接到并查集中。
3. 遍历所有数字，找到每个数字所属的连通分量，并统计每个连通分量的大小。
4. 返回最大的连通分量的大小。

关键点:
- 使用质因数分解来找到共同因子。
- 使用并查集来高效地管理连通分量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * sqrt(max(nums)))，其中 n 是 nums 的长度，max(nums) 是 nums 中的最大值。
空间复杂度: O(n + max(nums))，用于存储并查集和质因数分解的结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import math

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.max_size = 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            self.max_size = max(self.max_size, self.size[root_x])

def largestComponentSize(nums: List[int]) -> int:
    n = len(nums)
    uf = UnionFind(max(nums) + 1)

    for num in nums:
        for factor in range(2, int(math.sqrt(num)) + 1):
            if num % factor == 0:
                uf.union(num, factor)
                uf.union(num, num // factor)

    count = [0] * (max(nums) + 1)
    max_size = 0
    for num in nums:
        root = uf.find(num)
        count[root] += 1
        max_size = max(max_size, count[root])

    return max_size

Solution = create_solution(largestComponentSize)