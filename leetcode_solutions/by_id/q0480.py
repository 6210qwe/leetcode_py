# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 480
标题: Sliding Window Median
难度: hard
链接: https://leetcode.cn/problems/sliding-window-median/
题目类型: 数组、哈希表、滑动窗口、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
480. 滑动窗口中位数 - 中位数是有序序列最中间的那个数。如果序列的长度是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。 例如： * [2,3,4]，中位数是 3 * [2,3]，中位数是 (2 + 3) / 2 = 2.5 给你一个数组 nums，有一个长度为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1 位。你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。 示例： 给出 nums = [1,3,-1,-3,5,3,6,7]，以及 k = 3。 窗口位置 中位数 --------------- ----- [1 3 -1] -3 5 3 6 7 1 1 [3 -1 -3] 5 3 6 7 -1 1 3 [-1 -3 5] 3 6 7 -1 1 3 -1 [-3 5 3] 6 7 3 1 3 -1 -3 [5 3 6] 7 5 1 3 -1 -3 5 [3 6 7] 6 因此，返回该滑动窗口的中位数数组 [1,-1,-1,3,5,6]。 提示： * 你可以假设 k 始终有效，即：k 始终小于等于输入的非空数组的元素个数。 * 与真实值误差在 10 ^ -5 以内的答案将被视作正确答案。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个堆（大顶堆和小顶堆）维护中位数

算法步骤:
1. 使用大顶堆存储较小的一半，小顶堆存储较大的一半
2. 保持两个堆大小平衡（差不超过1）
3. 滑动窗口时，删除旧元素，添加新元素，重新平衡

关键点:
- 双堆维护中位数
- 延迟删除优化
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log k) - n为数组长度，k为窗口大小
空间复杂度: O(k) - 堆空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
import heapq
from collections import defaultdict
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def sliding_window_median(nums: List[int], k: int) -> List[float]:
    """
    函数式接口 - 滑动窗口中位数
    
    实现思路:
    使用双堆维护中位数，支持滑动窗口。
    
    Args:
        nums: 数组
        k: 窗口大小
        
    Returns:
        中位数数组
        
    Example:
        >>> sliding_window_median([1,3,-1,-3,5,3,6,7], 3)
        [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
    """
    class DualHeap:
        def __init__(self, k):
            self.small = []  # 大顶堆，存储较小的一半（负数）
            self.large = []  # 小顶堆，存储较大的一半
            self.small_size = 0
            self.large_size = 0
            self.delayed = defaultdict(int)  # 延迟删除
        
        def prune(self, heap, is_small):
            """清理堆顶的已删除元素"""
            while heap:
                num = -heap[0] if is_small else heap[0]
                if num in self.delayed and self.delayed[num] > 0:
                    self.delayed[num] -= 1
                    heapq.heappop(heap)
                    if is_small:
                        self.small_size -= 1
                    else:
                        self.large_size -= 1
                else:
                    break
        
        def make_balance(self):
            """平衡两个堆"""
            if self.small_size > self.large_size + 1:
                heapq.heappush(self.large, -self.small[0])
                heapq.heappop(self.small)
                self.small_size -= 1
                self.large_size += 1
                self.prune(self.small, True)
            elif self.small_size < self.large_size:
                heapq.heappush(self.small, -self.large[0])
                heapq.heappop(self.large)
                self.small_size += 1
                self.large_size -= 1
                self.prune(self.large, False)
        
        def insert(self, num):
            if not self.small or num <= -self.small[0]:
                heapq.heappush(self.small, -num)
                self.small_size += 1
            else:
                heapq.heappush(self.large, num)
                self.large_size += 1
            self.make_balance()
        
        def erase(self, num):
            self.delayed[num] += 1
            if num <= -self.small[0]:
                self.small_size -= 1
                if num == -self.small[0]:
                    self.prune(self.small, True)
            else:
                self.large_size -= 1
                if num == self.large[0]:
                    self.prune(self.large, False)
            self.make_balance()
        
        def get_median(self):
            if k % 2 == 1:
                return float(-self.small[0])
            else:
                return (-self.small[0] + self.large[0]) / 2.0
    
    dh = DualHeap(k)
    for i in range(k):
        dh.insert(nums[i])
    
    result = [dh.get_median()]
    
    for i in range(k, len(nums)):
        dh.erase(nums[i - k])
        dh.insert(nums[i])
        result.append(dh.get_median())
    
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(sliding_window_median)
