# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000323
标题: 数据流中的第 K 大元素
难度: easy
链接: https://leetcode.cn/problems/jBjn9C/
题目类型: 树、设计、二叉搜索树、二叉树、数据流、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 059. 数据流中的第 K 大元素 - 设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。 请实现 KthLargest 类： * KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。 * int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。 示例： 输入： ["KthLargest", "add", "add", "add", "add", "add"] [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]] 输出： [null, 4, 5, 5, 8, 8] 解释： KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]); kthLargest.add(3); // return 4 kthLargest.add(5); // return 5 kthLargest.add(10); // return 5 kthLargest.add(9); // return 8 kthLargest.add(4); // return 8 提示： * 1 <= k <= 104 * 0 <= nums.length <= 104 * -104 <= nums[i] <= 104 * -104 <= val <= 104 * 最多调用 add 方法 104 次 * 题目数据保证，在查找第 k 大元素时，数组中至少有 k 个元素 注意：本题与主站 703 题相同： https://leetcode.cn/problems/kth-largest-element-in-a-stream/ [https://leetcode.cn/problems/kth-largest-element-in-a-stream/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用最小堆来维护数据流中的前 k 大元素。

算法步骤:
1. 初始化时，将初始数据流中的前 k 大元素放入最小堆。
2. 在每次添加新元素时，如果新元素大于堆顶元素，则替换堆顶元素，并重新调整堆。
3. 堆顶元素即为当前数据流中的第 k 大元素。

关键点:
- 使用 Python 的 heapq 库来实现最小堆。
- 维护堆的大小不超过 k，以确保堆顶元素始终是第 k 大元素。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log k) - 每次插入操作的时间复杂度。
空间复杂度: O(k) - 堆的最大大小。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)
        return self.min_heap[0]

# 测试用例
if __name__ == "__main__":
    kth_largest = KthLargest(3, [4, 5, 8, 2])
    print(kth_largest.add(3))  # 输出 4
    print(kth_largest.add(5))  # 输出 5
    print(kth_largest.add(10)) # 输出 5
    print(kth_largest.add(9))  # 输出 8
    print(kth_largest.add(4))  # 输出 8