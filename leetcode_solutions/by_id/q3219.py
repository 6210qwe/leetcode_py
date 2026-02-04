# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3219
标题: Make Lexicographically Smallest Array by Swapping Elements
难度: medium
链接: https://leetcode.cn/problems/make-lexicographically-smallest-array-by-swapping-elements/
题目类型: 并查集、数组、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2948. 交换得到字典序最小的数组 - 给你一个下标从 0 开始的 正整数 数组 nums 和一个 正整数 limit 。 在一次操作中，你可以选择任意两个下标 i 和 j，如果 满足 |nums[i] - nums[j]| <= limit ，则交换 nums[i] 和 nums[j] 。 返回执行任意次操作后能得到的 字典序最小的数组 。 如果在数组 a 和数组 b 第一个不同的位置上，数组 a 中的对应元素比数组 b 中的对应元素的字典序更小，则认为数组 a 就比数组 b 字典序更小。例如，数组 [2,10,3] 比数组 [10,2,3] 字典序更小，下标 0 处是两个数组第一个不同的位置，且 2 < 10 。 示例 1： 输入：nums = [1,5,3,9,8], limit = 2 输出：[1,3,5,8,9] 解释：执行 2 次操作： - 交换 nums[1] 和 nums[2] 。数组变为 [1,3,5,9,8] 。 - 交换 nums[3] 和 nums[4] 。数组变为 [1,3,5,8,9] 。 即便执行更多次操作，也无法得到字典序更小的数组。 注意，执行不同的操作也可能会得到相同的结果。 示例 2： 输入：nums = [1,7,6,18,2,1], limit = 3 输出：[1,6,7,18,1,2] 解释：执行 3 次操作： - 交换 nums[1] 和 nums[2] 。数组变为 [1,6,7,18,2,1] 。 - 交换 nums[0] 和 nums[4] 。数组变为 [2,6,7,18,1,1] 。 - 交换 nums[0] 和 nums[5] 。数组变为 [1,6,7,18,1,2] 。 即便执行更多次操作，也无法得到字典序更小的数组。 示例 3： 输入：nums = [1,7,28,19,10], limit = 3 输出：[1,7,28,19,10] 解释：[1,7,28,19,10] 是字典序最小的数组，因为不管怎么选择下标都无法执行操作。 提示： * 1 <= nums.length <= 105 * 1 <= nums[i] <= 109 * 1 <= limit <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集将可以互相交换的元素分组，然后对每个组内的元素进行排序。

算法步骤:
1. 初始化并查集。
2. 遍历数组，将满足条件的元素进行合并。
3. 对每个连通分量内的元素进行排序。
4. 构建结果数组。

关键点:
- 使用并查集来管理连通分量。
- 对每个连通分量内的元素进行排序以保证字典序最小。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是数组的长度。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(n)，并查集和分组所需的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def solution_function_name(nums: List[int], limit: int) -> List[int]:
    n = len(nums)
    uf = UnionFind(n)
    
    # 创建一个索引列表，并按值排序
    indexed_nums = sorted(enumerate(nums), key=lambda x: x[1])
    
    # 合并可以交换的元素
    for i in range(n - 1):
        if indexed_nums[i + 1][1] - indexed_nums[i][1] <= limit:
            uf.union(indexed_nums[i][0], indexed_nums[i + 1][0])
    
    # 分组
    groups = {}
    for i in range(n):
        root = uf.find(i)
        if root not in groups:
            groups[root] = []
        groups[root].append(i)
    
    # 对每个组内的元素进行排序
    for group in groups.values():
        group.sort(key=lambda x: nums[x])
    
    # 构建结果数组
    result = [0] * n
    for group in groups.values():
        for i, index in enumerate(group):
            result[index] = nums[group[i]]
    
    return result

Solution = create_solution(solution_function_name)