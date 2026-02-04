# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2466
标题: Maximum Segment Sum After Removals
难度: hard
链接: https://leetcode.cn/problems/maximum-segment-sum-after-removals/
题目类型: 并查集、数组、有序集合、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2382. 删除操作后的最大子段和 - 给你两个下标从 0 开始的整数数组 nums 和 removeQueries ，两者长度都为 n 。对于第 i 个查询，nums 中位于下标 removeQueries[i] 处的元素被删除，将 nums 分割成更小的子段。 一个 子段 是 nums 中连续 正 整数形成的序列。子段和 是子段中所有元素的和。 请你返回一个长度为 n 的整数数组 answer ，其中 answer[i]是第 i 次删除操作以后的 最大 子段和。 注意：一个下标至多只会被删除一次。 示例 1： 输入：nums = [1,2,5,6,1], removeQueries = [0,3,2,4,1] 输出：[14,7,2,2,0] 解释：用 0 表示被删除的元素，答案如下所示： 查询 1 ：删除第 0 个元素，nums 变成 [0,2,5,6,1] ，最大子段和为子段 [2,5,6,1] 的和 14 。 查询 2 ：删除第 3 个元素，nums 变成 [0,2,5,0,1] ，最大子段和为子段 [2,5] 的和 7 。 查询 3 ：删除第 2 个元素，nums 变成 [0,2,0,0,1] ，最大子段和为子段 [2] 的和 2 。 查询 4 ：删除第 4 个元素，nums 变成 [0,2,0,0,0] ，最大子段和为子段 [2] 的和 2 。 查询 5 ：删除第 1 个元素，nums 变成 [0,0,0,0,0] ，最大子段和为 0 ，因为没有任何子段存在。 所以，我们返回 [14,7,2,2,0] 。 示例 2： 输入：nums = [3,2,11,1], removeQueries = [3,2,1,0] 输出：[16,5,3,0] 解释：用 0 表示被删除的元素，答案如下所示： 查询 1 ：删除第 3 个元素，nums 变成 [3,2,11,0] ，最大子段和为子段 [3,2,11] 的和 16 。 查询 2 ：删除第 2 个元素，nums 变成 [3,2,0,0] ，最大子段和为子段 [3,2] 的和 5 。 查询 3 ：删除第 1 个元素，nums 变成 [3,0,0,0] ，最大子段和为子段 [3] 的和 3 。 查询 5 ：删除第 0 个元素，nums 变成 [0,0,0,0] ，最大子段和为 0 ，因为没有任何子段存在。 所以，我们返回 [16,5,3,0] 。 提示： * n == nums.length == removeQueries.length * 1 <= n <= 105 * 1 <= nums[i] <= 109 * 0 <= removeQueries[i] < n * removeQueries 中所有数字 互不相同 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来维护子段，并使用有序集合来快速找到当前的最大子段和。

算法步骤:
1. 计算前缀和数组 prefix_sum，用于快速计算任意子段的和。
2. 初始化并查集 union_find，用于合并和查找子段。
3. 初始化有序集合 max_heap，用于存储当前的最大子段和。
4. 逆序遍历 removeQueries，模拟删除操作：
   - 将当前删除位置标记为已删除。
   - 更新并查集和有序集合。
   - 记录当前的最大子段和。
5. 返回结果数组。

关键点:
- 使用并查集来高效地合并和查找子段。
- 使用有序集合来快速找到当前的最大子段和。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 nums 的长度。主要由有序集合的操作决定。
空间复杂度: O(n)，并查集和有序集合的空间开销。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import collections
import heapq

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.max_size = [0] * n
    
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
            self.max_size[root_x] = max(self.max_size[root_x], self.max_size[root_y])

def maximum_segment_sum(nums: List[int], removeQueries: List[int]) -> List[int]:
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    
    union_find = UnionFind(n)
    max_heap = []
    deleted = [False] * n
    result = [0] * n
    
    for i in range(n - 1, -1, -1):
        idx = removeQueries[i]
        deleted[idx] = True
        
        left = right = idx
        if idx > 0 and deleted[idx - 1]:
            left = union_find.find(idx - 1)
            union_find.union(left, idx)
        if idx < n - 1 and deleted[idx + 1]:
            right = union_find.find(idx + 1)
            union_find.union(right, idx)
        
        root = union_find.find(idx)
        segment_sum = prefix_sum[right + 1] - prefix_sum[left]
        union_find.max_size[root] = segment_sum
        heapq.heappush(max_heap, (-segment_sum, root))
        
        while max_heap and union_find.max_size[max_heap[0][1]] != -max_heap[0][0]:
            heapq.heappop(max_heap)
        
        if max_heap:
            result[i] = -max_heap[0][0]
    
    return result

Solution = create_solution(maximum_segment_sum)