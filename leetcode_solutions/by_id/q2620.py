# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2620
标题: Find Consecutive Integers from a Data Stream
难度: medium
链接: https://leetcode.cn/problems/find-consecutive-integers-from-a-data-stream/
题目类型: 设计、队列、哈希表、计数、数据流
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2526. 找到数据流中的连续整数 - 给你一个整数数据流，请你实现一个数据结构，检查数据流中最后 k 个整数是否 等于 给定值 value 。 请你实现 DataStream 类： * DataStream(int value, int k) 用两个整数 value 和 k 初始化一个空的整数数据流。 * boolean consec(int num) 将 num 添加到整数数据流。如果后 k 个整数都等于 value ，返回 true ，否则返回 false 。如果少于 k 个整数，条件不满足，所以也返回 false 。 示例 1： 输入： ["DataStream", "consec", "consec", "consec", "consec"] [[4, 3], [4], [4], [4], [3]] 输出： [null, false, false, true, false] 解释： DataStream dataStream = new DataStream(4, 3); // value = 4, k = 3 dataStream.consec(4); // 数据流中只有 1 个整数，所以返回 False 。 dataStream.consec(4); // 数据流中只有 2 个整数 // 由于 2 小于 k ，返回 False 。 dataStream.consec(4); // 数据流最后 3 个整数都等于 value， 所以返回 True 。 dataStream.consec(3); // 最后 k 个整数分别是 [4,4,3] 。 // 由于 3 不等于 value ，返回 False 。 提示： * 1 <= value, num <= 109 * 1 <= k <= 105 * 至多调用 consec 次数为 105 次。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个队列来存储最近的 k 个整数，并维护一个计数器来记录当前连续的 value 数量。

算法步骤:
1. 初始化一个队列和一个计数器。
2. 在每次调用 `consec` 方法时，将新的整数添加到队列中。
3. 如果队列长度超过 k，则移除队列头部的元素，并更新计数器。
4. 检查队列中的所有元素是否都等于 value，并返回相应的布尔值。

关键点:
- 使用队列来维护最近的 k 个整数。
- 使用计数器来优化对队列中元素的检查。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 每次调用 `consec` 方法的时间复杂度是常数级别的。
空间复杂度: O(k) - 队列最多存储 k 个整数。
"""

# ============================================================================
# 代码实现
# ============================================================================

from collections import deque


class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.queue = deque()
        self.count = 0

    def consec(self, num: int) -> bool:
        # 将新整数添加到队列中
        self.queue.append(num)
        
        # 更新计数器
        if num == self.value:
            self.count += 1
        else:
            self.count = 0
        
        # 如果队列长度超过 k，则移除队列头部的元素
        if len(self.queue) > self.k:
            removed_num = self.queue.popleft()
            if removed_num == self.value:
                self.count -= 1
        
        # 检查队列中的所有元素是否都等于 value
        return self.count == self.k


# 示例
if __name__ == "__main__":
    dataStream = DataStream(4, 3)
    print(dataStream.consec(4))  # 输出: False
    print(dataStream.consec(4))  # 输出: False
    print(dataStream.consec(4))  # 输出: True
    print(dataStream.consec(3))  # 输出: False