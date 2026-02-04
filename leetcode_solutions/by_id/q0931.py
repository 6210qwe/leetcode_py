# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 931
标题: Maximum Frequency Stack
难度: hard
链接: https://leetcode.cn/problems/maximum-frequency-stack/
题目类型: 栈、设计、哈希表、有序集合
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
895. 最大频率栈 - 设计一个类似堆栈的数据结构，将元素推入堆栈，并从堆栈中弹出出现频率最高的元素。 实现 FreqStack 类: * FreqStack() 构造一个空的堆栈。 * void push(int val) 将一个整数 val 压入栈顶。 * int pop() 删除并返回堆栈中出现频率最高的元素。 * 如果出现频率最高的元素不只一个，则移除并返回最接近栈顶的元素。 示例 1： 输入： ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"], [[],[5],[7],[5],[7],[4],[5],[],[],[],[]] 输出：[null,null,null,null,null,null,null,5,7,5,4] 解释： FreqStack = new FreqStack(); freqStack.push (5);//堆栈为 [5] freqStack.push (7);//堆栈是 [5,7] freqStack.push (5);//堆栈是 [5,7,5] freqStack.push (7);//堆栈是 [5,7,5,7] freqStack.push (4);//堆栈是 [5,7,5,7,4] freqStack.push (5);//堆栈是 [5,7,5,7,4,5] freqStack.pop ();//返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,5,7,4]。 freqStack.pop ();//返回 7 ，因为 5 和 7 出现频率最高，但7最接近顶部。堆栈变成 [5,7,5,4]。 freqStack.pop ();//返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,4]。 freqStack.pop ();//返回 4 ，因为 4, 5 和 7 出现频率最高，但 4 是最接近顶部的。堆栈变成 [5,7]。 提示： * 0 <= val <= 109 * push 和 pop 的操作数不大于 2 * 104。 * 输入保证在调用 pop 之前堆栈中至少有一个元素。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个字典来维护每个元素的频率和频率对应的栈。一个字典 `freq` 用于记录每个元素的频率，另一个字典 `group` 用于存储每个频率对应的栈。

算法步骤:
1. 初始化时，创建两个字典 `freq` 和 `group`，以及一个变量 `max_freq` 来记录当前最大频率。
2. 在 `push` 操作中，更新 `freq` 字典中对应元素的频率，并将该元素添加到 `group` 字典中对应频率的栈中。如果该频率大于 `max_freq`，则更新 `max_freq`。
3. 在 `pop` 操作中，从 `group` 字典中 `max_freq` 对应的栈中弹出一个元素，并更新 `freq` 字典中该元素的频率。如果该频率的栈为空，则减少 `max_freq`。

关键点:
- 使用两个字典分别维护频率和频率对应的栈，可以高效地实现 `push` 和 `pop` 操作。
- 通过 `max_freq` 变量快速找到当前频率最高的栈。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - `push` 和 `pop` 操作的时间复杂度都是 O(1)。
空间复杂度: O(n) - 其中 n 是操作数，需要存储所有元素及其频率。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class FreqStack:

    def __init__(self):
        self.freq = {}  # 记录每个元素的频率
        self.group = {}  # 记录每个频率对应的栈
        self.max_freq = 0  # 当前最大频率

    def push(self, val: int) -> None:
        # 更新频率
        self.freq[val] = self.freq.get(val, 0) + 1
        # 将元素添加到对应频率的栈中
        if self.freq[val] not in self.group:
            self.group[self.freq[val]] = []
        self.group[self.freq[val]].append(val)
        # 更新最大频率
        self.max_freq = max(self.max_freq, self.freq[val])

    def pop(self) -> int:
        # 从最大频率的栈中弹出一个元素
        val = self.group[self.max_freq].pop()
        # 更新频率
        self.freq[val] -= 1
        # 如果该频率的栈为空，则减少最大频率
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return val


Solution = create_solution(FreqStack)