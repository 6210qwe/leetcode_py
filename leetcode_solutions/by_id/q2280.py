# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2280
标题: Count Good Triplets in an Array
难度: hard
链接: https://leetcode.cn/problems/count-good-triplets-in-an-array/
题目类型: 树状数组、线段树、数组、二分查找、分治、有序集合、归并排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2179. 统计数组中好三元组数目 - 给你两个下标从 0 开始且长度为 n 的整数数组 nums1 和 nums2 ，两者都是 [0, 1, ..., n - 1] 的 排列 。 好三元组 指的是 3 个 互不相同 的值，且它们在数组 nums1 和 nums2 中出现顺序保持一致。换句话说，如果我们将 pos1v 记为值 v 在 nums1 中出现的位置，pos2v 为值 v 在 nums2 中的位置，那么一个好三元组定义为 0 <= x, y, z <= n - 1 ，且 pos1x < pos1y < pos1z 和 pos2x < pos2y < pos2z 都成立的 (x, y, z) 。 请你返回好三元组的 总数目 。 示例 1： 输入：nums1 = [2,0,1,3], nums2 = [0,1,2,3] 输出：1 解释： 总共有 4 个三元组 (x,y,z) 满足 pos1x < pos1y < pos1z ，分别是 (2,0,1) ，(2,0,3) ，(2,1,3) 和 (0,1,3) 。 这些三元组中，只有 (0,1,3) 满足 pos2x < pos2y < pos2z 。所以只有 1 个好三元组。 示例 2： 输入：nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3] 输出：4 解释：总共有 4 个好三元组 (4,0,3) ，(4,0,2) ，(4,1,3) 和 (4,1,2) 。 提示： * n == nums1.length == nums2.length * 3 <= n <= 105 * 0 <= nums1[i], nums2[i] <= n - 1 * nums1 和 nums2 是 [0, 1, ..., n - 1] 的排列。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用树状数组（Fenwick Tree）来高效地计算满足条件的三元组数量。

算法步骤:
1. 构建一个映射，记录每个元素在 nums2 中的位置。
2. 遍历 nums1，使用树状数组来维护当前遍历到的元素之前已经出现的元素数量。
3. 对于每个元素，计算其左边和右边的元素数量，从而计算出满足条件的三元组数量。

关键点:
- 使用树状数组来高效地进行区间查询和更新。
- 通过两次遍历来分别计算左边和右边的元素数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import bisect

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= i & -i
        return result

def count_good_triplets(nums1: List[int], nums2: List[int]) -> int:
    n = len(nums1)
    pos_in_nums2 = {num: i for i, num in enumerate(nums2)}
    fenwick_tree = FenwickTree(n)
    left_counts = [0] * n
    right_counts = [0] * n

    # First pass to calculate left counts
    for i, num in enumerate(nums1):
        index_in_nums2 = pos_in_nums2[num]
        left_counts[i] = fenwick_tree.query(index_in_nums2 + 1)
        fenwick_tree.update(index_in_nums2 + 1, 1)

    fenwick_tree = FenwickTree(n)

    # Second pass to calculate right counts and the final result
    result = 0
    for i in range(n - 1, -1, -1):
        num = nums1[i]
        index_in_nums2 = pos_in_nums2[num]
        right_counts[i] = fenwick_tree.query(index_in_nums2 + 1)
        fenwick_tree.update(index_in_nums2 + 1, 1)
        result += left_counts[i] * right_counts[i]

    return result

Solution = create_solution(count_good_triplets)