# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1262
标题: Online Majority Element In Subarray
难度: hard
链接: https://leetcode.cn/problems/online-majority-element-in-subarray/
题目类型: 设计、树状数组、线段树、数组、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1157. 子数组中占绝大多数的元素 - 设计一个数据结构，有效地找到给定子数组的 多数元素 。 子数组的 多数元素 是在子数组中出现 threshold 次数或次数以上的元素。 实现 MajorityChecker 类: * MajorityChecker(int[] arr) 会用给定的数组 arr 对 MajorityChecker 初始化。 * int query(int left, int right, int threshold) 返回子数组中的元素 arr[left...right] 至少出现 threshold 次数，如果不存在这样的元素则返回 -1。 示例 1： 输入: ["MajorityChecker", "query", "query", "query"] [[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]] 输出： [null, 1, -1, 2] 解释： MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]); majorityChecker.query(0,5,4); // 返回 1 majorityChecker.query(0,3,3); // 返回 -1 majorityChecker.query(2,3,2); // 返回 2 提示： * 1 <= arr.length <= 2 * 104 * 1 <= arr[i] <= 2 * 104 * 0 <= left <= right < arr.length * threshold <= right - left + 1 * 2 * threshold > right - left + 1 * 调用 query 的次数最多为 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用随机化和二分查找来高效地找到多数元素。

算法步骤:
1. 在初始化时，记录每个元素的所有出现位置。
2. 在查询时，使用随机化选择一个候选元素，并使用二分查找验证其是否为多数元素。
3. 如果验证失败，则继续随机选择其他候选元素，直到找到一个满足条件的多数元素或遍历完所有候选元素。

关键点:
- 使用随机化减少平均时间复杂度。
- 使用二分查找高效验证候选元素是否为多数元素。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n * log m)，其中 n 是数组长度，m 是调用 query 的次数。
空间复杂度: O(n)，用于存储每个元素的所有出现位置。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import random
from bisect import bisect_left, bisect_right

class MajorityChecker:
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.positions = {}
        for i, num in enumerate(arr):
            if num not in self.positions:
                self.positions[num] = []
            self.positions[num].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(20):  # 尝试 20 次随机选择
            random_index = random.randint(left, right)
            candidate = self.arr[random_index]
            if candidate in self.positions:
                pos_list = self.positions[candidate]
                count = bisect_right(pos_list, right) - bisect_left(pos_list, left)
                if count >= threshold:
                    return candidate
        return -1

# 测试代码
if __name__ == "__main__":
    obj = MajorityChecker([1, 1, 2, 2, 1, 1])
    print(obj.query(0, 5, 4))  # 输出 1
    print(obj.query(0, 3, 3))  # 输出 -1
    print(obj.query(2, 3, 2))  # 输出 2