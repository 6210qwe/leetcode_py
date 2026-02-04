# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3438
标题: Peaks in Array
难度: hard
链接: https://leetcode.cn/problems/peaks-in-array/
题目类型: 树状数组、线段树、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3187. 数组中的峰值 - 数组 arr 中 大于 前面和后面相邻元素的元素被称为 峰值 元素。 给你一个整数数组 nums 和一个二维整数数组 queries 。 你需要处理以下两种类型的操作： * queries[i] = [1, li, ri] ，求出子数组 nums[li..ri] 中 峰值 元素的数目。 * queries[i] = [2, indexi, vali] ，将 nums[indexi] 变为 vali 。 请你返回一个数组 answer ，它依次包含每一个第一种操作的答案。 注意： * 子数组中 第一个 和 最后一个 元素都 不是 峰值元素。 示例 1： 输入：nums = [3,1,4,2,5], queries = [[2,3,4],[1,0,4]] 输出：[0] 解释： 第一个操作：我们将 nums[3] 变为 4 ，nums 变为 [3,1,4,4,5] 。 第二个操作：[3,1,4,4,5] 中峰值元素的数目为 0 。 示例 2： 输入：nums = [4,1,4,2,1,5], queries = [[2,2,4],[1,0,2],[1,0,4]] 输出：[0,1] 解释： 第一个操作：nums[2] 变为 4 ，它已经是 4 了，所以保持不变。 第二个操作：[4,1,4] 中峰值元素的数目为 0 。 第三个操作：第二个 4 是 [4,1,4,2,1] 中的峰值元素。 提示： * 3 <= nums.length <= 105 * 1 <= nums[i] <= 105 * 1 <= queries.length <= 105 * queries[i][0] == 1 或者 queries[i][0] == 2 * 对于所有的 i ，都有： * queries[i][0] == 1 ：0 <= queries[i][1] <= queries[i][2] <= nums.length - 1 * queries[i][0] == 2 ：0 <= queries[i][1] <= nums.length - 1, 1 <= queries[i][2] <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用线段树来高效处理区间查询和单点更新。

算法步骤:
1. 初始化线段树，记录每个区间的峰值数量。
2. 对于每种查询：
   - 如果是更新操作，更新线段树中的相应节点。
   - 如果是查询操作，查询线段树中指定区间的峰值数量。

关键点:
- 线段树的构建和维护。
- 区间查询和单点更新的实现。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n) 对于每次查询和更新操作。
空间复杂度: O(n) 用于存储线段树。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build_tree(nums, 0, 0, self.n - 1)

    def build_tree(self, nums, tree_index, lo, hi):
        if lo == hi:
            self.tree[tree_index] = 1 if (lo > 0 and nums[lo] > nums[lo - 1]) and (lo < self.n - 1 and nums[lo] > nums[lo + 1]) else 0
            return
        mid = (lo + hi) // 2
        self.build_tree(nums, 2 * tree_index + 1, lo, mid)
        self.build_tree(nums, 2 * tree_index + 2, mid + 1, hi)
        self.tree[tree_index] = self.tree[2 * tree_index + 1] + self.tree[2 * tree_index + 2]

    def update(self, index, value, nums, tree_index, lo, hi):
        if lo == hi:
            self.tree[tree_index] = 1 if (lo > 0 and nums[lo] > nums[lo - 1]) and (lo < self.n - 1 and nums[lo] > nums[lo + 1]) else 0
            return
        mid = (lo + hi) // 2
        if index <= mid:
            self.update(index, value, nums, 2 * tree_index + 1, lo, mid)
        else:
            self.update(index, value, nums, 2 * tree_index + 2, mid + 1, hi)
        self.tree[tree_index] = self.tree[2 * tree_index + 1] + self.tree[2 * tree_index + 2]

    def query(self, tree_index, lo, hi, query_lo, query_hi):
        if query_lo > hi or query_hi < lo:
            return 0
        if query_lo <= lo and hi <= query_hi:
            return self.tree[tree_index]
        mid = (lo + hi) // 2
        left_sum = self.query(2 * tree_index + 1, lo, mid, query_lo, query_hi)
        right_sum = self.query(2 * tree_index + 2, mid + 1, hi, query_lo, query_hi)
        return left_sum + right_sum

def handle_queries(nums: List[int], queries: List[List[int]]) -> List[int]:
    n = len(nums)
    segment_tree = SegmentTree(nums)
    result = []
    for query in queries:
        if query[0] == 1:
            result.append(segment_tree.query(0, 0, n - 1, query[1], query[2]))
        elif query[0] == 2:
            index, value = query[1], query[2]
            nums[index] = value
            segment_tree.update(index, value, nums, 0, 0, n - 1)
    return result

Solution = create_solution(handle_queries)