# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2703
标题: Handling Sum Queries After Update
难度: hard
链接: https://leetcode.cn/problems/handling-sum-queries-after-update/
题目类型: 线段树、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2569. 更新数组后处理求和查询 - 给你两个下标从 0 开始的数组 nums1 和 nums2 ，和一个二维数组 queries 表示一些操作。总共有 3 种类型的操作： 1. 操作类型 1 为 queries[i] = [1, l, r] 。你需要将 nums1 从下标 l 到下标 r 的所有 0 反转成 1 并且所有 1 反转成 0 。l 和 r 下标都从 0 开始。 2. 操作类型 2 为 queries[i] = [2, p, 0] 。对于 0 <= i < n 中的所有下标，令 nums2[i] = nums2[i] + nums1[i] * p 。 3. 操作类型 3 为 queries[i] = [3, 0, 0] 。求 nums2 中所有元素的和。 请你返回一个 数组，包含 所有第三种操作类型 的答案。 示例 1： 输入：nums1 = [1,0,1], nums2 = [0,0,0], queries = [[1,1,1],[2,1,0],[3,0,0]] 输出：[3] 解释：第一个操作后 nums1 变为 [1,1,1] 。第二个操作后，nums2 变成 [1,1,1] ，所以第三个操作的答案为 3 。所以返回 [3] 。 示例 2： 输入：nums1 = [1], nums2 = [5], queries = [[2,0,0],[3,0,0]] 输出：[5] 解释：第一个操作后，nums2 保持不变为 [5] ，所以第二个操作的答案是 5 。所以返回 [5] 。 提示： * 1 <= nums1.length,nums2.length <= 105 * nums1.length = nums2.length * 1 <= queries.length <= 105 * queries[i].length = 3 * 0 <= l <= r <= nums1.length - 1 * 0 <= p <= 106 * 0 <= nums1[i] <= 1 * 0 <= nums2[i] <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用线段树来高效处理区间反转和区间求和。

算法步骤:
1. 初始化线段树，用于维护 nums1 的区间和。
2. 对于每种操作：
   - 操作类型 1: 使用线段树进行区间反转。
   - 操作类型 2: 计算 nums1 的区间和，并更新 nums2。
   - 操作类型 3: 计算 nums2 的当前和并记录结果。

关键点:
- 使用线段树来高效处理区间反转和区间求和。
- 通过懒惰标记来优化区间反转操作。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O((n + q) * log n)，其中 n 是数组长度，q 是查询数量。
空间复杂度: O(n)，线段树的空间开销。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [False] * (4 * n)

    def push_down(self, node, start, end):
        if self.lazy[node]:
            mid = (start + end) // 2
            self.tree[node * 2] = mid - start + 1 - self.tree[node * 2]
            self.tree[node * 2 + 1] = end - mid - self.tree[node * 2 + 1]
            self.lazy[node * 2] = not self.lazy[node * 2]
            self.lazy[node * 2 + 1] = not self.lazy[node * 2 + 1]
            self.lazy[node] = False

    def update(self, node, start, end, l, r):
        if l > end or r < start:
            return
        if l <= start and end <= r:
            self.tree[node] = end - start + 1 - self.tree[node]
            if start != end:
                self.lazy[node] = not self.lazy[node]
            return
        self.push_down(node, start, end)
        mid = (start + end) // 2
        self.update(node * 2, start, mid, l, r)
        self.update(node * 2 + 1, mid + 1, end, l, r)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def query(self, node, start, end, l, r):
        if l > end or r < start:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        self.push_down(node, start, end)
        mid = (start + end) // 2
        return self.query(node * 2, start, mid, l, r) + self.query(node * 2 + 1, mid + 1, end, l, r)


def handle_query(nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
    n = len(nums1)
    seg_tree = SegmentTree(n)
    
    for i in range(n):
        if nums1[i] == 1:
            seg_tree.update(1, 0, n - 1, i, i)
    
    result = []
    sum_nums2 = sum(nums2)
    
    for query in queries:
        if query[0] == 1:
            l, r = query[1], query[2]
            seg_tree.update(1, 0, n - 1, l, r)
        elif query[0] == 2:
            p = query[1]
            ones_count = seg_tree.query(1, 0, n - 1, 0, n - 1)
            sum_nums2 += ones_count * p
        elif query[0] == 3:
            result.append(sum_nums2)
    
    return result


Solution = create_solution(handle_query)