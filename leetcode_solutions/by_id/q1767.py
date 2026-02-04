# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1767
标题: Design Front Middle Back Queue
难度: medium
链接: https://leetcode.cn/problems/design-front-middle-back-queue/
题目类型: 设计、队列、数组、链表、数据流、双向链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1670. 设计前中后队列 - 请你设计一个队列，支持在前，中，后三个位置的 push 和 pop 操作。 请你完成 FrontMiddleBack 类： * FrontMiddleBack() 初始化队列。 * void pushFront(int val) 将 val 添加到队列的 最前面 。 * void pushMiddle(int val) 将 val 添加到队列的 正中间 。 * void pushBack(int val) 将 val 添加到队里的 最后面 。 * int popFront() 将 最前面 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 -1 。 * int popMiddle() 将 正中间 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 -1 。 * int popBack() 将 最后面 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 -1 。 请注意当有 两个 中间位置的时候，选择靠前面的位置进行操作。比方说： * 将 6 添加到 [1, 2, 3, 4, 5] 的中间位置，结果数组为 [1, 2, 6, 3, 4, 5] 。 * 从 [1, 2, 3, 4, 5, 6] 的中间位置弹出元素，返回 3 ，数组变为 [1, 2, 4, 5, 6] 。 示例 1： 输入： ["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"] [[], [1], [2], [3], [4], [], [], [], [], []] 输出： [null, null, null, null, null, 1, 3, 4, 2, -1] 解释： FrontMiddleBackQueue q = new FrontMiddleBackQueue(); q.pushFront(1); // [1] q.pushBack(2); // [1, 2] q.pushMiddle(3); // [1, 3, 2] q.pushMiddle(4); // [1, 4, 3, 2] q.popFront(); // 返回 1 -> [4, 3, 2] q.popMiddle(); // 返回 3 -> [4, 2] q.popMiddle(); // 返回 4 -> [2] q.popBack(); // 返回 2 -> [] q.popFront(); // 返回 -1 -> [] （队列为空） 提示： * 1 <= val <= 109 * 最多调用 1000 次 pushFront， pushMiddle， pushBack， popFront， popMiddle 和 popBack 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个双端队列来实现前中后队列的操作。一个队列存储前半部分，另一个队列存储后半部分。

算法步骤:
1. 维护两个双端队列 front 和 back，确保 front 的长度始终不小于 back 的长度，并且两者长度差不超过 1。
2. 在 push 和 pop 操作时，根据需要调整 front 和 back 的长度，以保持平衡。

关键点:
- 使用双端队列可以高效地在两端进行插入和删除操作。
- 通过维护两个队列的长度平衡，可以保证所有操作的时间复杂度为 O(1)。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1)
空间复杂度: O(n)，其中 n 是队列中的元素数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from collections import deque


class FrontMiddleBackQueue:

    def __init__(self):
        self.front = deque()
        self.back = deque()

    def pushFront(self, val: int) -> None:
        self.front.appendleft(val)
        self._balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())
        self.front.append(val)

    def pushBack(self, val: int) -> None:
        self.back.append(val)
        self._balance()

    def popFront(self) -> int:
        if not self.front and not self.back:
            return -1
        if self.front:
            val = self.front.popleft()
        else:
            val = self.back.popleft()
        self._balance()
        return val

    def popMiddle(self) -> int:
        if not self.front and not self.back:
            return -1
        if len(self.front) == len(self.back):
            val = self.front.pop()
        else:
            val = self.back.popleft()
        self._balance()
        return val

    def popBack(self) -> int:
        if not self.front and not self.back:
            return -1
        if self.back:
            val = self.back.pop()
        else:
            val = self.front.pop()
        self._balance()
        return val

    def _balance(self) -> None:
        while len(self.front) < len(self.back):
            self.front.append(self.back.popleft())
        while len(self.front) > len(self.back) + 1:
            self.back.appendleft(self.front.pop())


# 测试代码
if __name__ == "__main__":
    q = FrontMiddleBackQueue()
    q.pushFront(1)  # [1]
    q.pushBack(2)   # [1, 2]
    q.pushMiddle(3) # [1, 3, 2]
    q.pushMiddle(4) # [1, 4, 3, 2]
    print(q.popFront())  # 1, [4, 3, 2]
    print(q.popMiddle()) # 3, [4, 2]
    print(q.popMiddle()) # 4, [2]
    print(q.popBack())   # 2, []
    print(q.popFront())  # -1, []