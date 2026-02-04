# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 789
标题: Kth Largest Element in a Stream
难度: easy
链接: https://leetcode.cn/problems/kth-largest-element-in-a-stream/
题目类型: 树、设计、二叉搜索树、二叉树、数据流、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
703. 数据流中的第 K 大元素 - 设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。 请实现 KthLargest 类： * KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。 * int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。 示例 1： 输入： ["KthLargest", "add", "add", "add", "add", "add"] [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]] 输出：[null, 4, 5, 5, 8, 8] 解释： KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]); kthLargest.add(3); // 返回 4 kthLargest.add(5); // 返回 5 kthLargest.add(10); // 返回 5 kthLargest.add(9); // 返回 8 kthLargest.add(4); // 返回 8 示例 2： 输入： ["KthLargest", "add", "add", "add", "add"] [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]] 输出：[null, 7, 7, 7, 8] 解释： KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]); kthLargest.add(2); // 返回 7 kthLargest.add(10); // 返回 7 kthLargest.add(9); // 返回 7 kthLargest.add(9); // 返回 8 提示： * 0 <= nums.length <= 104 * 1 <= k <= nums.length + 1 * -104 <= nums[i] <= 104 * -104 <= val <= 104 * 最多调用 add 方法 104 次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用最小堆来维护前 k 大的元素。每次插入新元素时，如果堆的大小超过 k，则弹出堆顶元素。

算法步骤:
1. 初始化时，将初始数组 `nums` 中的前 k 大元素放入最小堆。
2. 每次调用 `add` 方法时，将新元素插入堆中，并在堆的大小超过 k 时弹出堆顶元素。
3. 堆顶元素即为当前数据流中的第 k 大元素。

关键点:
- 使用 Python 的 `heapq` 模块来实现最小堆。
- 通过维护一个大小为 k 的最小堆来确保堆顶元素始终是第 k 大的元素。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log k) - 每次插入和删除操作的时间复杂度为 O(log k)。
空间复杂度: O(k) - 维护一个大小为 k 的最小堆。
"""

# ============================================================================
# 代码实现
# ============================================================================

import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]

# 工厂函数
def create_kth_largest(k: int, nums: List[int]) -> KthLargest:
    return KthLargest(k, nums)

# 示例
if __name__ == "__main__":
    kth_largest = create_kth_largest(3, [4, 5, 8, 2])
    print(kth_largest.add(3))  # 输出 4
    print(kth_largest.add(5))  # 输出 5
    print(kth_largest.add(10))  # 输出 5
    print(kth_largest.add(9))  # 输出 8
    print(kth_largest.add(4))  # 输出 8